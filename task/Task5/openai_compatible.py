from openai import OpenAI


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


def main():

    print("=== OpenAI-Compatible API Test ===")

    try:

        response = client.chat.completions.create(
            model="college-assistant",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a strict programming teacher. "
                        "Give concise programming explanations."
                    )
                },
                {
                    "role": "user",
                    "content": "What is a Python function?"
                }
            ],
            temperature=0.2
        )

        print("\nResponse:")
        print(response.choices[0].message.content)

    except Exception as e:

        print("\nOllama OpenAI-compatible endpoint is not available.")
        print("Expected endpoint: http://localhost:11434/v1")
        print("Reason:", e)


if __name__ == "__main__":
    main()