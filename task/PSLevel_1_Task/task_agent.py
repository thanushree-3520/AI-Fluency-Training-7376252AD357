"""Step 5: an agentic RAG helpdesk in LangGraph - tools + loop + memory."""
import ast
import operator

from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from lc_config import get_model, get_vectorstore

COURSE_FEES = {"CS101": 12000, "AI202": 18000, "DS303": 15000}   # same data as Day 1
store = get_vectorstore()


MAX_DISTANCE = 0.4

@tool
def search_handbook(query: str) -> str:
    """Search the college handbook and return only relevant matching passages."""
    results = store.similarity_search_with_score(query, k=3)

    # Keep only chunks whose cosine distance is low enough
    relevant_docs = [
        (doc, score)
        for doc, score in results
        if score <= MAX_DISTANCE
    ]

    if not relevant_docs:
        return "NO_MATCH: this is not covered in the college handbook."

    return "\n\n".join(
        f"[{doc.metadata['source']}] {doc.page_content}"
        for doc, score in relevant_docs
    )



@tool
def get_course_fee(course_code: str) -> str:
    """Return the fee in rupees for a course code such as CS101, AI202 or DS303."""
    fee = COURSE_FEES.get(course_code.strip().upper())
    return f"{course_code.upper()} fee is Rs. {fee}" if fee else f"Unknown course code {course_code}"


@tool
def check_exam_eligibility(attendance_percent: float) -> str:
    """Check if a student with this attendance percentage (0-100) may write the end-semester exam."""
    if not 0 <= attendance_percent <= 100:
        return "ERROR: Attendance percentage must be between 0 and 100."

    if attendance_percent >= 75:
        return "ELIGIBLE: You may write the end-semester exam."
    elif attendance_percent >= 65:
        return "CONDONATION: You need to pay Rs. 500 per course."
    else:
        return "NOT ELIGIBLE: Attendance below 65% does not meet the exam requirement."



OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}


@tool
def calculator(expression: str) -> str:
    """Evaluate simple arithmetic such as '18000 + 15000' or '100 * 12'."""
    def ev(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value
        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            return OPS[type(n.op)](ev(n.left), ev(n.right))
        raise ValueError("only + - * / on numbers")
    try:
        return str(ev(ast.parse(expression, mode="eval").body))
    except Exception as e:                       # tell the model, don't crash the graph
        return f"Error: {e}"


tools = [search_handbook, get_course_fee, calculator,check_exam_eligibility]
model = get_model().bind_tools(tools)

SYSTEM = (
    "You are the Greenfield College helpdesk. "
    "Use search_handbook for college rules and policies. "
    "Use get_course_fee for course fees. "
    "Use calculator for arithmetic. "
    "Use check_exam_eligibility for attendance eligibility questions. "
    "For questions involving multiple fees or charges, call all required tools, "
    "then use calculator to calculate the final total. "
    "For follow-up questions, use relevant information from earlier messages "
    "in the same conversation. "
    "If search_handbook returns NO_MATCH, say you don't know and do not "
    "answer using outside knowledge. "
    "Answer briefly and name the source file when using handbook information."
)

def agent(state: MessagesState):
    """The LLM node: read the conversation, either answer or ask for a tool."""
    reply = model.invoke([("system", SYSTEM)] + state["messages"])
    return {"messages": [reply]}


builder = StateGraph(MessagesState)
builder.add_node("agent", agent)
builder.add_node("tools", ToolNode(tools))          # runs every tool call in the last message
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)   # tool calls? -> "tools", else -> END
builder.add_edge("tools", "agent")                  # the LOOP back to the LLM
graph = builder.compile(checkpointer=InMemorySaver())  # checkpointer = memory per thread


def ask(question, thread_id):
    config = {"configurable": {"thread_id": thread_id}, "recursion_limit": 10}
    print(f"\n[{thread_id}] USER: {question}")
    for step in graph.stream({"messages": [("user", question)]}, config, stream_mode="updates"):
        for node, update in step.items():
            for msg in update["messages"]:
                if getattr(msg, "tool_calls", None):
                    for c in msg.tool_calls:
                        print(f"   {node:6} -> call {c['name']}({c['args']})")
                elif node == "tools":
                    print(f"   {node:6} -> {msg.name} returned {msg.content[:55]!r}...")
                else:
                    print(f"   {node:6} -> ANSWER: {msg.content}")




if __name__ == "__main__":
    # Test the exam eligibility tool directly
    print(check_exam_eligibility.invoke({"attendance_percent": 82}))
    print(check_exam_eligibility.invoke({"attendance_percent": 70}))
    print(check_exam_eligibility.invoke({"attendance_percent": 50}))
    print(check_exam_eligibility.invoke({"attendance_percent": 120}))

    # Day 8 evaluation: all questions use the same thread
    ask("What CGPA do I need to be eligible for placements?", "task-run")
    ask("My attendance is 70%. Can I write the exam?", "task-run")
    ask("What is the total of the CS101 fee, the AI202 fee and the maximum late fee?", "task-run")
    ask("And if I pay only 5 days late instead?", "task-run")
    ask("What is the capital of France?", "task-run")

    saved = graph.get_state({"configurable": {"thread_id": "task-run"}}).values["messages"]
    print(f"\nThread task-run has {len(saved)} messages saved in memory")
