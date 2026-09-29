# 12. Observations

## 12.1 Step counts from Part C

| **Question**            | **Steps used** | **Tools called**             |
| ----------------------- | -------------: | ---------------------------- |
| Merit scholarship total |              2 | `read_webpage`, `calculator` |
| Hostel student total    |              2 | `read_webpage`, `calculator` |
| 15% of AI202            |              1 | `calculator`                 |
| Welcome message         |              0 | None                         |

The questions requiring information from `notice.html` first use the `read_webpage` tool and then use the `calculator` tool for arithmetic. The 15% calculation only needs the calculator. The welcome-message question does not require any tool.

## 12.2 Failure log from Part D

| **Failure**                     | **What you saw (no guards)**                                                                                                                                                        | **What it cost (steps / time)**                                                                                        |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 1. Repeating loop               | The agent repeatedly tried to read the missing `fees.html` file because the requested file was not available.                                                                       | Up to 6 steps before the existing `max_steps` safety limit stopped the agent.                                          |
| 2. Unknown tool (safe `.get`)   | The agent requested a tool that was not present in the registry. The `.get()` lookup returned `None`, allowing the program to return an `Unknown tool` message instead of crashing. | 1 tool-call step; the program continued safely.                                                                        |
| 2b. Unknown tool (unsafe `[ ]`) | Using `TOOL_FUNCTIONS[name]` for a missing tool caused a `KeyError` and stopped the program.                                                                                        | 1 tool-call step; the program terminated with an exception.                                                            |
| 3. Context overflow             | Reading the deliberately large `big.html` file produced excessive tool output and caused the conversation context to grow until the model/context limit was reached.                | Dependent on the model/context limit; the experiment demonstrated excessive context growth and unnecessary processing. |

## 12.3 After the fixes

| **Failure**         | **Behaviour with guards**                                                                                 | **Which guard acted**               |
| ------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| 1. Repeating loop   | The agent detected the same tool call repeatedly and stopped instead of continuing the loop indefinitely. | Repeat detection                    |
| 2. Unknown tool     | The agent returned an `Unknown tool` message instead of crashing.                                         | Safe registry lookup using `.get()` |
| 3. Context overflow | Large tool output was truncated and the overall character budget prevented uncontrolled context growth.   | `MAX_TOOL_CHARS` and `CHAR_BUDGET`  |

The fixed version adds repeat detection, output truncation and a character-budget guard. These changes are specifically required by the Day 3 experiment.

## 12.4 Your chosen limits

| **Setting**      | **Value you chose** | **Justification**                                                                                                                                                           |
| ---------------- | ------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| max_steps        |                   6 | Six steps provide enough iterations for a normal ReAct task involving reading information and performing calculations, while preventing an agent from running indefinitely. |
| MAX_TOOL_CHARS   |                1500 | Limiting each tool result keeps unnecessary webpage content out of the model context while still retaining the important information needed for the task.                   |
| CHAR_BUDGET      |               30000 | A total character budget provides an additional safety limit against very large tool outputs and runaway context usage.                                                     |
| Repeat threshold |                   3 | Three identical consecutive tool calls are treated as a loop, allowing legitimate repeated work while stopping an obvious repetition.                                       |

### Observation Summary

The experiments showed that a ReAct agent needs more than just tools and a reasoning loop. It also needs stopping and safety conditions. Repeat detection prevents repeated tool calls, safe registry lookup prevents crashes from unknown tools, output truncation controls the amount of information returned by a tool, and the character budget limits overall context growth. These guards make the agent more predictable and safer to run.
