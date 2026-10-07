# validator.py

from tools import SCHEMAS


def validate_arguments(tool_name, arguments):
    if tool_name not in SCHEMAS:
        return f"Unknown tool: {tool_name}"

    schema = SCHEMAS[tool_name]
    parameters = schema["parameters"]

    properties = parameters["properties"]
    required = parameters["required"]

    # Check required arguments
    for field in required:
        if field not in arguments:
            return f"Missing required argument: {field}"

    # Check extra arguments
    for field in arguments:
        if field not in properties:
            return f"Invented or extra argument: {field}"

    # Check types
    for field, value in arguments.items():
        expected_type = properties[field]["type"]

        if expected_type == "string" and not isinstance(value, str):
            return f"Wrong type for {field}: expected string"

        if expected_type == "number" and (
            not isinstance(value, (int, float))
            or isinstance(value, bool)
        ):
            return f"Wrong type for {field}: expected number"

    # Check enum
    for field, rules in properties.items():
        if "enum" in rules and field in arguments:
            if arguments[field] not in rules["enum"]:
                return (
                    f"Invalid value for {field}: "
                    f"{arguments[field]}. "
                    f"Expected one of {rules['enum']}"
                )

    return None