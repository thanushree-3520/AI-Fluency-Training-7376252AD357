# 10. Observations

| **Criterion** | **Chatbot** | **Workflow** | **Agent** |
|---|---|---|---|
| Q1 correct? (Y/N) | N | Y | Y |
| Q2 correct? (Y/N) | N | Y | N |
| Q3 correct? (Y/N) | N | N | Y |
| Q4 handled well? (Y/N) | Y | N | Y |
| Challenge question handled? (Y/N) | N | N | Y |
| Same output on a repeat run? (Y/N) | Y | Y | N |
| Approximate response time | 1–2 sec | < 1 sec | 2–5 sec |
| Number of LLM calls per question | 1 | 0 | 1–3 |
| One strength | Natural language responses | Fast and predictable | Can use tools dynamically |
| One weakness | Can hallucinate or guess facts | Cannot handle unexpected questions | More complex and can fail during tool calling |
| Best suited for (one real use case) | General conversation | Fixed fee calculations | Flexible college assistant |

## Agent trace: Question 2

| **Step** | **Tool called and arguments** | **Result (observation)** |
|---|---|---|
| 1 | `get_course_fee({"course_code": "CS101"})` | `12000` |
| 2 | `get_course_fee({"course_code": "AI202"})` | `18000` |
| 3 | `calculator({"expression": "(12000+18000)-(12000+18000)*0.10"})` | Tool call validation error |
| 4 | — | No final answer because the agent stopped due to the tool-call error |

# 11. Discussion Questions

### 1. The chatbot gave a confident but wrong fee. Why is that more dangerous than replying "I don't know"?

A wrong fee can mislead the user and cause an incorrect financial decision. Saying "I don't know" is safer because it does not provide false information.

### 2. The workflow was always correct for questions 1 and 2. Why might a finance office still prefer it over the agent?

A workflow follows fixed rules, so its output is predictable, fast, and easier to test. For important financial calculations, predictable behavior can be more useful than a flexible agent.

### 3. The agent's steps can change between runs. What problems would that cause in a real product?

Changing steps can produce different answers, make debugging difficult, and reduce reliability. It can also make it harder to reproduce and verify an incorrect result.

### 4. Design a system that uses a workflow for common questions and an agent for the rest. Where would you draw the line?

Common and well-defined questions such as course fees, totals, and simple calculations should use the workflow. Questions that require flexible reasoning or multiple tools can be sent to the agent.

### 5. Which parts of agent.py are the LLM, the tools, and the loop?

- **LLM:** `client.chat.completions.create(...)`
- **Tools:** `TOOLS` and `TOOL_FUNCTIONS`
- **Loop:** `for step in range(1, max_steps + 1):`
- The Python program executes the selected tools and sends the results back to the LLM.

# 13. Viva Questions

### 1. What is the difference between a chatbot, a rule-based workflow, and an AI agent?

A chatbot directly uses an LLM to generate answers. A rule-based workflow follows predefined rules. An AI agent uses an LLM to decide when and which tools to use.

### 2. In agent.py, which lines are the LLM, which are the tools, and which is the loop?

The LLM is called using `client.chat.completions.create()`. The tools are `TOOLS` and `TOOL_FUNCTIONS`. The loop is `for step in range(1, max_steps + 1)`.

### 3. Who actually executes a tool: the LLM or your Python program?

The Python program executes the tool. The LLM only decides which tool should be called and provides its arguments.

### 4. Why does the agent need a max_steps limit?

It prevents the agent from running indefinitely if it keeps requesting tools without producing a final answer.

### 5. Why does the calculator tool avoid Python's eval() function?

`eval()` can execute arbitrary Python code and can be unsafe. The calculator uses Python's `ast` module to allow only supported arithmetic operations.

### 6. What is the purpose of the JSON Schema tool descriptions in tools.py?

They tell the LLM which tools are available, what each tool does, and what arguments each tool requires.

### 7. Why do we use a virtual environment for each project?

A virtual environment keeps project dependencies separate and prevents conflicts between different projects.

### 8. Why is the API key kept in a .env file instead of inside config.py?

It keeps the secret separate from the source code and helps prevent accidentally uploading the API key to GitHub.

### 9. What does it mean that Ollama, Groq, and Hugging Face all provide an OpenAI-compatible API?

It means they provide an API interface that follows the OpenAI-style format, so the same Python client can be used with different providers by changing the configuration.

# 14. Result

Thus, a Python environment was set up in VS Code and connected to an open large language model, and a chatbot, a rule-based workflow, and an AI agent were implemented and compared on the same task. The observations show that **the chatbot is simple and flexible but may provide incorrect information, the workflow is fast and predictable for predefined questions, and the agent is more flexible because it can use tools dynamically but is more complex and may encounter tool-calling errors.**