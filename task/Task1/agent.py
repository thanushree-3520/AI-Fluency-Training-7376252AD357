import json
from config import client, MODEL
from tools import TOOLS, TOOL_FUNCTIONS

SYSTEM_PROMPT = """
You are a college student assistant.

Use get_student_data whenever you need Arun's private student information.
Use check_eligibility to determine exam eligibility.
Do not guess private student information.
If no tool is needed, answer directly.
"""


def agent(question, max_steps=5):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content.strip()

        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments
                    }
                }
                for call in message.tool_calls
            ]
        })

        for call in message.tool_calls:
            name = call.function.name
            arguments = json.loads(call.function.arguments or "{}")

            function = TOOL_FUNCTIONS.get(name)

            if function:
                result = function(**arguments)
            else:
                result = f"Unknown tool: {name}"

            print(f"step {step}: {name}({arguments}) -> {result}")

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": str(result)
            })

    return "Stopped: maximum steps reached."


if __name__ == "__main__":

    questions = [
        "What is Arun's attendance percentage?",
        "Is Arun eligible to attend the end-semester examination?",
        "What is Arun's internal mark and course?",
        "Write a welcome message for Arun."
    ]

    print("\n=== SYSTEM 3: AI AGENT ===\n")

    for question in questions:
        print("Q:", question)
        print("A:", agent(question))
        print("-" * 70)