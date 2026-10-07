# Day 6 – Reliable Tool Calling: Schemas, Validation, Retry and Structured Outputs

## 1. Scenario

The scenario selected for this task is a Student Assistant.

The assistant can answer questions about student marks by using two tools:

1. `get_student_marks`
2. `calculate_average`

The first tool looks up marks for a subject. The second tool calculates the average of three marks.

This scenario was selected because it is small enough to understand clearly while demonstrating tool calling, validation, error handling, parallel calls and structured outputs.

---

# 2. Chat Completions Format

The Chat Completions API uses messages to represent the conversation.

Important request fields include:

- `model` – specifies the model to use.
- `messages` – contains system, user, assistant and tool messages.
- `tools` – describes the functions that the model is allowed to request.
- `tool_choice` – controls whether the model can or must use a tool.
- `max_tokens` – controls the maximum generated output.

A response contains fields such as:

- `choices`
- `message`
- `content`
- `tool_calls`
- `finish_reason`

The `finish_reason` tells the program why the model stopped generating.

### finish_reason = stop

The model has completed its response.

The program can use the message content as the final answer.

### finish_reason = length

The response was stopped because the token limit was reached.

The agent retries the request with a larger token limit.

### finish_reason = tool_calls

The model wants the program to execute one or more tools.

The program must process the tool calls, execute the functions and send the results back to the model.

When the model requests a tool, `message.content` can be empty because the important information is inside `message.tool_calls`.

---

# 3. OpenAI-Compatible Servers

An OpenAI-compatible server provides an API interface that follows the same general request and response format as the OpenAI API.

This allows the same Python client library to communicate with different providers by changing values such as:

- `base_url`
- `api_key`
- `model`

In this task, Groq was used as the provider.

The client was configured with:

```python
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)