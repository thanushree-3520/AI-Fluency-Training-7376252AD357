import sys
sys.path.append("../Task2")

from config import client, MODEL


questions = [
    "What is the fee for CS101?",
    "What is Python?",
    "What is the capital of India?"
]

print("PLAIN LLM - NO TOOL")
print("===================")

for question in questions:

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": question}
        ]
    )

    answer = response.choices[0].message.content

    print("\nQuestion:", question)
    print("Answer:", answer)