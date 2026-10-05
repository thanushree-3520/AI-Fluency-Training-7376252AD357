from Day5_config import client, MODEL


def run_custom_model(name, system_prompt, user_prompt):
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )

    print("System prompt:")
    print(system_prompt)

    print("\nUser prompt:")
    print(user_prompt)

    print("\nResponse:")
    print(response.choices[0].message.content)


if __name__ == "__main__":

    run_custom_model(
        "Fee Assistant",
        "You are a college fee assistant. Give clear and concise answers about course fees.",
        "What is the fee for AI202?"
    )

    run_custom_model(
        "Student Welcome Assistant",
        "You are a friendly college assistant. Write short and professional welcome messages for students.",
        "Write a two-line welcome message for new AI students."
    )