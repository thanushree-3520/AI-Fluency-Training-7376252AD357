# 3. Result

## 3.1 Explanation of Each Approach

### Direct Prompting

Direct prompting sends the user's question directly to the language model and produces an answer immediately.

**What kind of questions can it answer?**

It can answer simple questions and questions that can be solved using the model's existing knowledge. For example, it can answer:

> If 75 students attend and Room C has 100 seats, how many seats remain?

The answer is 25 seats.

**What can it not answer correctly?**

It cannot reliably answer questions that require current external information that is not available to the model. For example:

> What is the weather in Erode today?

The model has no weather tool in this approach, so it cannot reliably obtain the current weather.

**Does it use tools?**

No. Direct prompting does not use any external tools.

**How does it arrive at the final answer?**

The user's question is directly sent to the language model. The model processes the question using its available knowledge and generates the final answer immediately.

**Limitations in this scenario**

The main limitation is the lack of external tool access. It can solve room-capacity calculations but cannot reliably obtain current weather information.

---

### Chain-of-Thought Prompting

Chain-of-Thought prompting asks the model to reason through a problem step by step before producing the final answer.

**What kind of questions can it answer?**

It is useful for questions that require multiple reasoning steps. For example:

> If 75 students attend and Room C has 100 seats, how many seats remain?

The model can reason that:

100 - 75 = 25

Therefore, 25 seats remain.

**What can it not answer correctly?**

It cannot provide facts that it does not already have. For example, it cannot reliably determine today's weather in Erode because it has no external weather tool.

**Does it use tools?**

No. The Chain-of-Thought implementation used in this task does not use external tools.

**How does it arrive at the final answer?**

The user's question is sent to the model with an instruction to reason carefully. The model performs the required reasoning internally and then provides the final answer with a brief explanation.

**Limitations in this scenario**

Chain-of-Thought improves reasoning for multi-step questions, but it cannot obtain current external information. Therefore, it cannot reliably answer the live weather question.

---

### ReAct Agent

The ReAct agent combines reasoning with actions and observations. It can decide when a tool is required and use the tool result before producing the final answer.

**What kind of questions can it answer?**

It can answer reasoning questions and questions requiring external information.

For example, it can determine whether a room can accommodate a particular number of students using the room-capacity tool. It can also obtain weather information using the weather tool.

**What can it not answer correctly?**

If the required tool is unavailable, incorrectly implemented, or provides incorrect information, the ReAct agent may not produce a reliable answer.

**Does it use tools?**

Yes. The agent decides to call a tool when the question requires information or an operation that cannot be obtained directly.

The tools used in this scenario are:

- `check_room_capacity`
- `get_weather`

**How does it arrive at the final answer?**

The ReAct process follows:

```text
User Question
      ↓
   Thought
      ↓
   Action
      ↓
    Tool
      ↓
 Observation
      ↓
   Thought
      ↓
 Final Answer