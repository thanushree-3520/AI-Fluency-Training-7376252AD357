from config import client, MODEL

questions = [
    "Which room is suitable for 50 students: Room A, Room B, or Room C?",
    "If 75 students attend and Room C has 100 seats, how many seats remain?",
    "Can you determine today's weather in Erode?"
]

print("\n=== CHAIN-OF-THOUGHT APPROACH ===\n")

for question in questions:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Reason carefully about the problem internally. "
                    "Give only the final answer with a brief explanation. "
                    "Do not use external tools."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    print("Q:", question)
    print("A:", response.choices[0].message.content)
    print("-" * 60)