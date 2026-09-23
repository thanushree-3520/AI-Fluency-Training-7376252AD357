import json

from config import client, MODEL
from tools import get_weather, check_room_capacity


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather information for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_room_capacity",
            "description": "Check whether a room can accommodate students.",
            "parameters": {
                "type": "object",
                "properties": {
                    "room": {"type": "string"},
                    "students": {"type": "integer"}
                },
                "required": ["room", "students"]
            }
        }
    }
]


FUNCTIONS = {
    "get_weather": get_weather,
    "check_room_capacity": check_room_capacity
}


def react_agent(question):

    messages = [
        {
            "role": "system",
            "content": (
                "You are a college event planning assistant. "
                "Use tools when external information is required. "
                "Do not guess tool results."
            )
        },
        {"role": "user", "content": question}
    ]

    for step in range(5):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content

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
            arguments = json.loads(call.function.arguments)

            print(f"Step {step + 1}")
            print("Action:", name)
            print("Arguments:", arguments)

            result = FUNCTIONS[name](**arguments)

            print("Observation:", result)
            print()

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": str(result)
            })

    return "Maximum steps reached."


questions = [
    "Which room can accommodate 50 students?",
    "What is the weather in Erode today?",
    "Which room can accommodate 75 students and how many seats will remain?"
]

print("\n=== REACT AGENT ===\n")

for question in questions:

    print("Q:", question)

    answer = react_agent(question)

    print("Final Answer:", answer)
    print("=" * 70)