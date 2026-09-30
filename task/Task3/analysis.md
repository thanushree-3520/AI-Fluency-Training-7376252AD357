# Day 3 Task 3 - From Prompt to Action

## 1. Scenario

For this task, I selected a college course fee lookup scenario.

The college has different courses and their corresponding fees:

- CS101 - ₹12000
- AI202 - ₹18000
- DS303 - ₹15000

The purpose of this scenario is to compare a plain LLM prompt with an LLM that has access to one external tool.

The external tool is called `get_course_fee`. It receives a course code and returns the corresponding course fee.

---

## 2. What is a Large Language Model?

A Large Language Model is an AI system trained on a large amount of text that can understand questions and generate natural-language responses.

For example, questions such as "What is Python?" can normally be answered directly by an LLM using its learned knowledge.

However, the LLM does not automatically have access to the current college fee database used in this task. If it does not have the required information in its available context, it may give an incorrect or guessed answer.

In this scenario, the course fee is external information. Therefore, a tool can provide the actual value.

---

## 3. What is an Agent?

An agent is an LLM-based system that can use external tools to complete a task.

A normal chat response mainly generates an answer from the model's available knowledge and context.

An agent can identify that additional information or an operation is required, use an available tool, receive the result, and then use that result to produce its answer.

In this scenario, the agent can recognise that a question about the CS101 fee requires the course-fee lookup tool.

---

## 4. What is a Tool and Tool Call?

A tool is an external function that performs an operation for the LLM.

The tool used in this task is:

`get_course_fee(course_code)`

The tool receives a course code and returns its fee.

A tool call is the action of requesting the tool to execute.

For example:

`get_course_fee("CS101")`

returns:

`CS101 course fee is ₹12000`

The tool description tells the model what the tool does and what information it needs.

The parameter description tells the model that the course code should be supplied when calling the tool.

This information helps the model decide when the tool is useful.

---

## 5. Flow of a Tool Call

The tool call follows these steps:

1. The user asks a question about a course fee.
2. The LLM receives the question.
3. The system provides information about the available course-fee tool.
4. The model identifies that the question requires course-fee information.
5. The course code is supplied to the `get_course_fee` function.
6. The tool looks up the course in the fee data.
7. The tool returns the result.
8. The result is given back to the LLM.
9. The LLM uses the result to generate the final answer.

For example, for the question "What is the fee for CS101?", the tool returns ₹12000 and the model can use this value in its response.

---

## 6. Why Should a Tool Return Text When It Fails?

A tool should return its result as text even when the operation fails.

For example, if a user asks for an unknown course such as XYZ101, the tool can return:

"XYZ101 course not found"

instead of stopping the entire program with an exception.

This allows the LLM to receive the failure information and explain it to the user.

---

## 7. Comparison Table

| Basis | Plain LLM Prompt | LLM With One Tool |
|---|---|---|
| Source of the answer | Model knowledge and conversation context | Model knowledge plus tool result |
| Can it fetch or compute information outside its own memory? | No | Yes, through the available tool |
| Reliability on factual or numeric questions | Depends on information available to the model | More reliable when the required information is supplied by the tool |
| Transparency | The answer generation is not based on an external lookup | The tool call and returned result can be observed |
| Speed / cost | Usually simpler and faster | Additional tool execution adds a small amount of processing |

---

## 8. Observation

### Question 1

**Question:** What is the fee for CS101?

The plain LLM was asked the question without access to the course-fee tool.

The tool-enabled version had access to `get_course_fee` and could obtain the CS101 fee from the course data.

Expected tool result:

`CS101 course fee is ₹12000`

This question genuinely benefits from the external tool because the exact fee is stored in the tool's data.

### Question 2

**Question:** What is Python?

This is a general knowledge question.

The plain LLM can answer this question without using an external tool.

The tool-enabled system also does not need the course-fee tool because the question is unrelated to course fees.

### Question 3

**Question:** What is the capital of India?

This is another general knowledge question.

The plain LLM can answer it without an external tool.

The course-fee tool is not necessary because it does not contain information about countries or capitals.

---

## 9. Suitability and Conclusion

A plain LLM prompt is suitable when the question can be answered reliably from the model's available knowledge and context.

In this scenario, general questions such as "What is Python?" can be answered without the course-fee tool.

An external tool becomes useful when the answer depends on specific information outside the model's available knowledge.

For example, the exact CS101 course fee is stored in the course-fee lookup tool. The tool provides the required information so that the answer can be based on the actual stored value.

In general, a plain LLM is sufficient for many general explanations and knowledge-based questions. A tool becomes necessary when the task requires external data, a calculation, a file lookup, or another operation that the model cannot reliably perform from its own knowledge alone.

This task demonstrates how adding even one external tool can extend an LLM from simply generating text to obtaining information needed to complete a task.