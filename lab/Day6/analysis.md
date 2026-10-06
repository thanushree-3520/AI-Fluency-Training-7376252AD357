# Day 6 – Function Calling That Survives a Badly Behaved Model

## 1. Objective

The objective of this lab was to make function calling more reliable when the model produces malformed or unexpected tool calls.

The implementation focused on:

* Defining stricter tool schemas.
* Validating tool arguments before execution.
* Handling malformed JSON.
* Handling unknown tools.
* Handling missing or extra arguments.
* Handling incorrect argument types.
* Handling invalid enum values.
* Handling truncated model responses.
* Detecting repeated failing tool calls.
* Supporting parallel tool calls.
* Comparing normal output, JSON mode, and structured output.

---

## 2. Tools Implemented

Two tools were implemented:

### `get_course_fee`

This tool returns the fee for a given course.

Course data used:

| Course |   Fee |
| ------ | ----: |
| CS101  | 12000 |
| AI202  | 18000 |
| DS303  | 15000 |

### `calculator`

This tool performs basic arithmetic operations:

* `add`
* `subtract`
* `multiply`
* `divide`

The tool schema restricts the operation value using an enum and prevents unexpected extra arguments.

---

## 3. Validation

The `validate.py` program was created to validate tool arguments before the tool is executed.

The validation checks include:

1. Arguments must be an object.
2. Required arguments must be present.
3. Extra arguments are rejected.
4. Argument types are checked.
5. Enum values are checked.

This prevents invalid tool calls from directly reaching the tool functions.

---

## 4. Robust Agent

The `robust_agent.py` program improves the basic Day 3 agent by adding error handling around tool calls.

The agent handles:

* JSON parsing errors.
* Unknown tool names.
* Invalid arguments.
* Tool execution errors.
* Truncated responses.
* Repeated failing calls.
* Parallel tool calls.

When a response is truncated because
