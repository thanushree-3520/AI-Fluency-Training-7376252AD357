# agent.py

import json
import os
from dotenv import load_dotenv
from openai import OpenAI

from tools import SCHEMAS, TOOLS
from validator import validate_arguments


load_dotenv("../../lab/Day1/.env")


client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-20b"

# --------------------------------------------------
# Convert our schemas into OpenAI tool definitions
# --------------------------------------------------

TOOLS_FOR_MODEL = []

for tool_name, schema in SCHEMAS.items():

    TOOLS_FOR_MODEL.append({
        "type": "function",
        "function": {
            "name": schema["name"],
            "description": schema["description"],
            "parameters": schema["parameters"],
            "strict": schema["strict"]
        }
    })


# --------------------------------------------------
# Handle one tool call
# --------------------------------------------------

def handle_tool_call(tool_call):

    tool_name = tool_call.function.name
    arguments_text = tool_call.function.arguments

    print("\nTool requested:", tool_name)
    print("Arguments:", arguments_text)

    # Stage 1: Parse JSON
    try:
        arguments = json.loads(arguments_text)

    except json.JSONDecodeError:
        return "ERROR: Invalid JSON in tool arguments."

    # Make sure JSON is an object
    if not isinstance(arguments, dict):
        return "ERROR: Tool arguments must be a JSON object."

    # Stage 2: Look up the tool
    if tool_name not in TOOLS:
        return f"ERROR: Unknown tool: {tool_name}"

    # Stage 3: Validate arguments
    validation_error = validate_arguments(
        tool_name,
        arguments
    )

    if validation_error:
        return f"ERROR: {validation_error}"

    # Stage 4: Execute tool
    try:
        result = TOOLS[tool_name](**arguments)

        return json.dumps(result)

    except Exception as error:
        return f"ERROR: Tool execution failed: {error}"


# --------------------------------------------------
# Robust agent
# --------------------------------------------------

def run_agent(question, max_steps=5):

    messages = [
        {
            "role": "system",
            "content": (
                "You are a reliable student assistant. "
                "Use tools when necessary. "
                "Never invent tool arguments. "
                "If a tool returns an error, correct the request "
                "and try again."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    previous_calls = set()

    for step in range(max_steps):

        print("\n--------------------------------")
        print("STEP:", step + 1)
        print("--------------------------------")

        try:

            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=TOOLS_FOR_MODEL,
                tool_choice="auto",
                max_tokens=300
            )

        except Exception as error:

            print("API ERROR:", error)
            return

        choice = response.choices[0]

        finish_reason = choice.finish_reason

        print("finish_reason:", finish_reason)

        message = choice.message

        # --------------------------------------------------
        # Retry when response is truncated
        # --------------------------------------------------

        if finish_reason == "length":

            print("Response was truncated.")
            print("Retrying with a larger max_tokens value...")

            try:

                response = client.chat.completions.create(
                    model=MODEL,
                    messages=messages,
                    tools=TOOLS_FOR_MODEL,
                    tool_choice="auto",
                    max_tokens=700
                )

                choice = response.choices[0]
                message = choice.message
                finish_reason = choice.finish_reason

                print(
                    "Retry finish_reason:",
                    finish_reason
                )

            except Exception as error:

                print("Retry failed:", error)
                return

        # --------------------------------------------------
        # Normal final answer
        # --------------------------------------------------

        if finish_reason == "stop":

            print("\nFINAL ANSWER:")
            print(message.content)

            return message.content

        # --------------------------------------------------
        # Tool calls
        # --------------------------------------------------

        if finish_reason == "tool_calls":

            tool_calls = message.tool_calls

            print(
                "Number of tool calls:",
                len(tool_calls)
            )

            # Add assistant message containing tool calls
            messages.append(message)

            for tool_call in tool_calls:

                tool_name = tool_call.function.name
                arguments = tool_call.function.arguments

                # Detect repeated identical calls
                call_signature = (
                    tool_name,
                    arguments
                )

                if call_signature in previous_calls:

                    print(
                        "Repeated identical tool call detected."
                    )

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": (
                            "ERROR: This exact tool call "
                            "was already attempted. "
                            "Do not repeat it."
                        )
                    })

                    continue

                previous_calls.add(call_signature)

                result = handle_tool_call(tool_call)

                print("Tool result:", result)

                # Every tool call must receive a tool message
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })

            continue

        print(
            "Unhandled finish_reason:",
            finish_reason
        )

        return

    print(
        "\nMaximum number of agent steps reached."
    )


# --------------------------------------------------
# Test questions
# --------------------------------------------------

if __name__ == "__main__":

    questions = [
        "What are my Python marks?",

        "Use the tools to look up my Python marks and my SQL marks independently. Call both tools in the same response if possible.",

        "What are my Java marks?",

        "What is artificial intelligence?"
    ]

    for question in questions:

        print("\n\n====================================")
        print("QUESTION:", question)
        print("====================================")

        run_agent(question)