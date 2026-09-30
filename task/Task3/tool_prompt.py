import sys
import json

sys.path.append("../Task2")

from config import client, MODEL
from one_tool import get_course_fee


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Returns the college fee for a course code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "The course code. Example: CS101"
                    }
                },
                "required": ["course_code"]
            }
        }
    }
]


question = "What is the fee for CS101?"

messages = [
    {
        "role": "user",
        "content": question
    }
]

print("LLM WITH ONE TOOL")
print("=================")
print("Question:", question)

response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    tools=tools,
    tool_choice={
        "type": "function",
        "function": {
            "name": "get_course_fee"
        }
    }
)

message = response.choices[0].message

if message.tool_calls:

    call = message.tool_calls[0]

    print("Tool call:", call.function.name)
    print("Arguments:", call.function.arguments)

    arguments = json.loads(call.function.arguments)

    course_code = arguments.get("course_code")

    if not course_code:
        course_code = arguments.get("course_name")

    result = get_course_fee(course_code)

    print("Tool result:", result)

    messages.append({
        "role": "assistant",
        "content": None,
        "tool_calls": message.tool_calls
    })

    messages.append({
        "role": "tool",
        "tool_call_id": call.id,
        "content": result
    })

    final_response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    print("Final answer:", final_response.choices[0].message.content)

else:
    print("No tool call was made.")