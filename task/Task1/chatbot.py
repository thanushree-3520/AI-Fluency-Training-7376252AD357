from config import client, MODEL

questions = [
    "What is Arun's attendance percentage?",
    "Is Arun eligible to attend the end-semester examination?",
    "Write a short welcome message for Arun."
]

print("=" * 60)
print("PLAIN CHATBOT - TASK 1")
print("=" * 60)

for q in questions:
    print("\nQ:", q)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful college assistant."
            },
            {
                "role": "user",
                "content": q
            }
        ]
    )

    print("A:", response.choices[0].message.content)
    print("-" * 60)