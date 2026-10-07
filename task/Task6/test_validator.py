from validator import validate_arguments


print("=== VALID CASE ===")

result = validate_arguments(
    "get_student_marks",
    {"subject": "Python"}
)

print(result)


print("\n=== MISSING ARGUMENT ===")

result = validate_arguments(
    "get_student_marks",
    {}
)

print(result)


print("\n=== EXTRA ARGUMENT ===")

result = validate_arguments(
    "get_student_marks",
    {
        "subject": "Python",
        "student_name": "Student"
    }
)

print(result)


print("\n=== WRONG TYPE ===")

result = validate_arguments(
    "get_student_marks",
    {
        "subject": 123
    }
)

print(result)


print("\n=== INVALID ENUM ===")

result = validate_arguments(
    "get_student_marks",
    {
        "subject": "Java"
    }
)

print(result)