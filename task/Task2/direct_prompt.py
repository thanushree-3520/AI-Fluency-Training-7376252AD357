from config import client, MODEL

questions = [
    "Which room is suitable for 50 students: Room A, Room B, or Room C?",
    "If 75 students attend and Room C has 100 seats, how many seats remain?",
    "What is the weather in Erode today?"
]

print("\n=== DIRECT PROMPTING ===\n")

for question in questions:

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
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