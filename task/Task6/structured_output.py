# structured_outputs.py

import os
import json
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv("../../lab/Day1/.env")


client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-20b"


QUESTION = """
Extract the student information from this sentence:

"Ananya is 20 years old and studies Artificial Intelligence.
Her CGPA is 9.2."

Return the name, age, course and CGPA.
"""


# --------------------------------------------------
# 1. No constraint
# --------------------------------------------------

def no_constraint():

    print("\n================================")
    print("1. NO CONSTRAINT")
    print("================================")

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": QUESTION
                }
            ],
            max_tokens=200
        )

        raw = response.choices[0].message.content

        print("Raw reply:")
        print(raw)

        print("\nParsed result:")
        print("No structured parsing was required.")

    except Exception as error:

        print("Error:", error)


# --------------------------------------------------
# 2. JSON mode
# --------------------------------------------------

def json_mode():

    print("\n================================")
    print("2. JSON MODE")
    print("================================")

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Return the answer as valid JSON with "
                        "name, age, course and cgpa fields."
                    )
                },
                {
                    "role": "user",
                    "content": QUESTION
                }
            ],
            response_format={
                "type": "json_object"
            },
            max_tokens=200
        )

        raw = response.choices[0].message.content

        print("Raw reply:")
        print(raw)

        try:
            parsed = json.loads(raw)

            print("\nParsed result:")
            print(parsed)

        except json.JSONDecodeError:

            print("\nInvalid JSON returned.")

    except Exception as error:

        print("JSON mode error:", error)


# --------------------------------------------------
# 3. Schema mode
# --------------------------------------------------

def schema_mode():

    print("\n================================")
    print("3. SCHEMA MODE")
    print("================================")

    schema = {
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            },
            "age": {
                "type": "integer"
            },
            "course": {
                "type": "string"
            },
            "cgpa": {
                "type": "number"
            }
        },
        "required": [
            "name",
            "age",
            "course",
            "cgpa"
        ],
        "additionalProperties": False
    }

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Extract the requested information "
                        "according to the provided schema."
                    )
                },
                {
                    "role": "user",
                    "content": QUESTION
                }
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "student_information",
                    "strict": True,
                    "schema": schema
                }
            },
            max_tokens=200
        )

        raw = response.choices[0].message.content

        print("Raw reply:")
        print(raw)

        try:

            parsed = json.loads(raw)

            print("\nParsed result:")
            print(parsed)

        except json.JSONDecodeError:

            print("\nInvalid JSON returned.")

    except Exception as error:

        print("Schema mode error:")
        print(error)


# --------------------------------------------------
# Run all three
# --------------------------------------------------

if __name__ == "__main__":

    no_constraint()

    json_mode()

    schema_mode()