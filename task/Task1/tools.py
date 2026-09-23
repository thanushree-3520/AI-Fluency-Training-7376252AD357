# Tools for the AI agent

STUDENT_DATA = {
    "name": "Arun",
    "course": "AI & DS",
    "attendance": 82,
    "internal_mark": 76
}

def get_student_data(name):
    if name.lower() == "arun":
        return STUDENT_DATA
    return "Student not found"


def check_eligibility(attendance, internal_mark):
    if attendance >= 75 and internal_mark >= 40:
        return "Eligible"
    return "Not eligible"


TOOL_FUNCTIONS = {
    "get_student_data": get_student_data,
    "check_eligibility": check_eligibility
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_student_data",
            "description": "Get private attendance, internal mark and course details for Arun.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_eligibility",
            "description": "Check exam eligibility using attendance and internal mark.",
            "parameters": {
                "type": "object",
                "properties": {
                    "attendance": {"type": "number"},
                    "internal_mark": {"type": "number"}
                },
                "required": ["attendance", "internal_mark"]
            }
        }
    }
]


if __name__ == "__main__":
    print(get_student_data("Arun"))
    print(check_eligibility(82, 76))