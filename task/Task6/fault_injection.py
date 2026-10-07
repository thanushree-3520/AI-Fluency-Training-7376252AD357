# fault_injection.py

import json
from validator import validate_arguments


def handle_tool_call(tool_name, arguments_text):
    print("\nTool:", tool_name)
    print("Arguments:", arguments_text)

    # Stage 1: Parse JSON
    try:
        arguments = json.loads(arguments_text)
    except json.JSONDecodeError:
        return "Invalid JSON: arguments could not be parsed."

    # JSON must contain an object
    if not isinstance(arguments, dict):
        return "Invalid arguments: expected a JSON object."

    # Stage 2 and 3: Look up tool and validate
    error = validate_arguments(tool_name, arguments)

    if error:
        return error

    return "Validation successful."


faults = [
    (
        "Fault 1 - Invalid JSON",
        "get_student_marks",
        '{"subject": "Python"'
    ),

    (
        "Fault 2 - Unknown tool",
        "get_student_grade",
        '{"subject": "Python"}'
    ),

    (
        "Fault 3 - Missing argument",
        "get_student_marks",
        '{}'
    ),

    (
        "Fault 4 - Wrong type",
        "get_student_marks",
        '{"subject": 123}'
    ),

    (
        "Fault 5 - Invalid enum",
        "get_student_marks",
        '{"subject": "Java"}'
    ),

    (
        "Fault 6 - Invented argument",
        "get_student_marks",
        '{"subject": "Python", "student_name": "Student"}'
    ),

    (
        "Fault 7 - Arguments are a list",
        "get_student_marks",
        '["Python"]'
    ),

    (
        "Fault 8 - Multiple invalid fields",
        "get_student_marks",
        '{"subject": "Java", "extra": "wrong"}'
    )
]


print("========================================")
print("       DAY 6 FAULT INJECTION TEST")
print("========================================")

for name, tool_name, arguments in faults:

    print("\n" + name)

    result = handle_tool_call(
        tool_name,
        arguments
    )

    print("Returned message:", result)
    print("Run continued: Y")