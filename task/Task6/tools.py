# tools.py

STUDENT_MARKS = {
    "Python": 85,
    "SQL": 90,
    "AI": 88
}


SCHEMAS = {
    "get_student_marks": {
        "name": "get_student_marks",
        "description": "Get the marks obtained by a student in a subject.",
        "parameters": {
            "type": "object",
            "properties": {
                "subject": {
                    "type": "string",
                    "enum": ["Python", "SQL", "AI"],
                    "description": "The subject whose marks are required."
                }
            },
            "required": ["subject"],
            "additionalProperties": False
        },
        "strict": True
    },

    "calculate_average": {
        "name": "calculate_average",
        "description": "Calculate the average of three marks.",
        "parameters": {
            "type": "object",
            "properties": {
                "mark1": {
                    "type": "number",
                    "description": "First mark."
                },
                "mark2": {
                    "type": "number",
                    "description": "Second mark."
                },
                "mark3": {
                    "type": "number",
                    "description": "Third mark."
                }
            },
            "required": ["mark1", "mark2", "mark3"],
            "additionalProperties": False
        },
        "strict": True
    }
}


def get_student_marks(subject):
    return {
        "subject": subject,
        "marks": STUDENT_MARKS[subject]
    }


def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3

    return {
        "mark1": mark1,
        "mark2": mark2,
        "mark3": mark3,
        "average": round(average, 2)
    }


TOOLS = {
    "get_student_marks": get_student_marks,
    "calculate_average": calculate_average
}