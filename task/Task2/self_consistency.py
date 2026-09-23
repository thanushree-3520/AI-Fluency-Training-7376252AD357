from config import client, MODEL

question = """
An AI workshop has 75 students.
Room A has 60 seats.
Room B has 40 seats.
Room C has 100 seats.

Which room should be selected and how many seats will remain?
"""

print("\n=== SELF-CONSISTENCY ===\n")

for i in range(5):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Reason carefully about the problem and give "
                    "the final answer with a short explanation."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.7
    )

    print(f"Run {i + 1}:")
    print(response.choices[0].message.content)
    print("-" * 50)

print("\n=== TEMPERATURE 0 ===\n")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "Solve carefully and give the final answer with a short explanation."
        },
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0
)

print(response.choices[0].message.content)