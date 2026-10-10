# PS Level 1 — Agentic AI: Foundations and Open-Source Practice

## 1. Project Overview

This project implements an Agentic AI college helpdesk using Python, a large language model (LLM), handbook documents, semantic search, and custom tools.

The helpdesk answers questions about placement eligibility, examination attendance, course fees, and college policies. It also checks whether retrieved handbook information is relevant to the user's question.

The project demonstrates document ingestion, vector search, tool calling, relevance filtering, arithmetic operations, and conversation memory.

## 2. Objectives

- Ingest six Markdown handbook documents into a vector database.
- Retrieve relevant handbook passages using semantic similarity.
- Identify the CGPA requirements for campus placements.
- Check examination eligibility based on attendance percentage.
- Calculate course fees and late fees using tools.
- Reject unrelated questions that are not covered by the handbook.
- Test follow-up questions using a shared conversation thread.
- Record execution output and evaluation results.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| LangChain | Model and tool integration |
| LangGraph | Agent workflow and conversation state |
| Groq | LLM provider |
| `openai/gpt-oss-20b` | Configured language model |
| ChromaDB | Vector database for handbook documents |
| FastEmbed | Generates document embeddings |
| `BAAI/bge-small-en-v1.5` | Configured embedding model |
| Git and GitHub | Version control and project submission |

## 4. Project Structure

```text
PSLevel_1_Task/
├── data/
│   ├── ai_fluency_training.md
│   ├── exam_regulations.md
│   ├── fee_policy.md
│   ├── hostel_rules.md
│   ├── library.md
│   └── placement_policy.md
├── Output/
│   └── screenshots of execution
├── lc_config.py
├── 1_ingest.py
├── 2_search.py
├── task_agent.py
├── results.md
├── run_log.txt
└── README.md
```

The `chroma_db/` directory is generated locally when the handbook is ingested. It is excluded from version control because it can be recreated from the source documents.

## 5. Task A — Handbook Ingestion and Semantic Search

### Description

Six Markdown documents are loaded from the `data/` directory. The documents are split into smaller chunks and stored in ChromaDB using embeddings.

The placement policy document specifies that students need a CGPA of at least 6.5 and no standing arrears to be eligible for campus placements.

### Placement policy example

File: `data/placement_policy.md`

```markdown
# Placement Policy

## Eligibility

Students with a CGPA of 6.5 or above and no standing arrears
are eligible for campus placements.

Students must register on the placement portal before
31 July of their final year.
```

### Ingestion process

The `1_ingest.py` script:

1. Reads all Markdown files from `data/`.
2. Converts the contents into documents.
3. Splits the documents into chunks.
4. Creates embeddings.
5. Stores the chunks in ChromaDB.

### Run the ingestion script

```powershell
python 1_ingest.py
```

### Search the handbook

The `2_search.py` script tests semantic retrieval for questions about late fees, hostel timings, examination attendance, and placement eligibility.

```powershell
python 2_search.py
```

### Observed result

For the question:

`What CGPA do I need to be eligible for placements?`

The top retrieved document was `placement_policy.md`, with an observed distance score of `0.185`.

## 6. Task B — Examination Eligibility Tool

### Description

The `check_exam_eligibility()` tool determines whether a student meets the attendance requirements for the end-semester examination.

### Implementation

The following is the tool's core decision logic, as implemented in `task_agent.py`.

```python
@tool
def check_exam_eligibility(attendance_percent: float) -> str:
    """Check exam eligibility using attendance percentage."""

    if not 0 <= attendance_percent <= 100:
        return "ERROR: Attendance percentage must be between 0 and 100."

    if attendance_percent >= 75:
        return "ELIGIBLE: You may write the end-semester exam."
    elif attendance_percent >= 65:
        return "CONDONATION: You need to pay Rs. 500 per course."
    else:
        return (
            "NOT ELIGIBLE: Attendance below 65% "
            "does not meet the exam requirement."
        )
```

### Decision rules

| Attendance | Result |
|---|---|
| 75% to 100% | Eligible |
| 65% to below 75% | Condonation required |
| Below 65% | Not eligible |
| Below 0% or above 100% | Invalid input |

### Test cases

```python
print(check_exam_eligibility.invoke(
    {"attendance_percent": 82}
))
print(check_exam_eligibility.invoke(
    {"attendance_percent": 70}
))
print(check_exam_eligibility.invoke(
    {"attendance_percent": 50}
))
print(check_exam_eligibility.invoke(
    {"attendance_percent": 120}
))
```

The four cases test eligibility, condonation, rejection, and invalid input.

## 7. Task C — Relevance Guard

### Description

A relevance guard prevents the agent from using unrelated handbook results to answer questions that are outside the scope of the college handbook.

The implementation uses `similarity_search_with_score()` to retrieve the top three documents and filters them using a maximum distance threshold.

### Implementation

The core filtering logic in `task_agent.py` is:

```python
MAX_DISTANCE = 0.4

results = store.similarity_search_with_score(query, k=3)

relevant_docs = [
    (doc, score)
    for doc, score in results
    if score <= MAX_DISTANCE
]

if not relevant_docs:
    return "NO_MATCH: this is not covered in the college handbook."
```

When relevant documents exist, the tool returns their source filenames and content.

### Threshold evaluation

The configured threshold is `0.4`.

| Query | Observed top distance | Expected behavior |
|---|---:|---|
| Placement eligibility | 0.185 | Return relevant handbook content |
| Capital of France | 0.581 | Return `NO_MATCH` |

A lower distance indicates a closer match for the tested embedding and vector-store configuration. The threshold should be reevaluated if the embedding model or data changes.

The agent's system prompt instructs it to say that it does not know when `search_handbook` returns `NO_MATCH`.

## 8. Tools Implemented

The agent uses the following tools:

### `search_handbook(query)`

Retrieves relevant passages from the college handbook and rejects results above the configured distance threshold.

### `check_exam_eligibility(attendance_percent)`

Checks attendance and returns eligibility, condonation, rejection, or an invalid-input message.

### `get_course_fee(course_code)`

Retrieves the configured fee for a course.

The current course fee mapping is:

```python
COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000,
}
```

### `calculator(expression)`

Performs arithmetic required by the agent, such as adding course fees and late fees.

The agent's system prompt directs it to use the appropriate tools rather than inventing policy information.

## 9. Task D — Agent Evaluation

The evaluation runs five questions in the same conversation thread, using the thread ID `task-run`.

| No. | Question | Expected result |
|---|---|---|
| 1 | What CGPA do I need to be eligible for placements? | CGPA of at least 6.5 and no standing arrears |
| 2 | My attendance is 70%. Can I write the exam? | Condonation of Rs. 500 per course |
| 3 | What is the total of the CS101 fee, the AI202 fee and the maximum late fee? | Rs. 32,000 |
| 4 | And if I pay only 5 days late instead? | Rs. 30,500 |
| 5 | What is the capital of France? | `NO_MATCH`; the agent says it does not know |

### Conversation memory

The same `task-run` thread is used for all five questions. This allows the follow-up question to refer to the earlier fee calculation.

### Execution log

The `run_log.txt` file records the printed program output, including the questions, tool calls, and answers.

To regenerate the log:

```powershell
python task_agent.py > run_log.txt
```

This command executes the agent again and overwrites the previous log file.

## 10. Configuration

The `lc_config.py` file configures the model provider, embedding provider, model settings, and ChromaDB collection.

The current configuration uses:

- LLM provider: Groq
- Model: `openai/gpt-oss-20b`
- Embedding provider: FastEmbed
- Embedding model: `BAAI/bge-small-en-v1.5`
- Vector-store collection: `college_helpdesk`
- Relevance threshold: `0.4`

Required environment variables and API credentials must be configured locally. Do not commit API keys or secret values to GitHub.

## 11. Setup and Execution

Run the following commands from the `PSLevel_1_Task` folder.

### Step 1: Activate the project's virtual environment

From this folder, if the repository-root `.venv` exists:

```powershell
..\..\.venv\Scripts\Activate.ps1
```

### Step 2: Install dependencies

Return to the repository root if necessary, then install the dependencies listed in the root requirements file:

```powershell
python -m pip install -r ..\..\requirements.txt
```

Run this command from `PSLevel_1_Task`.

### Step 3: Configure environment variables

Ensure the required `.env` file and API credentials are configured in the location expected by `lc_config.py`.

### Step 4: Build the vector database

```powershell
python 1_ingest.py
```

### Step 5: Test document retrieval

```powershell
python 2_search.py
```

### Step 6: Run the agent evaluation

```powershell
python task_agent.py
```

### Step 7: Save the execution log

```powershell
python task_agent.py > run_log.txt
```

## 12. Version Control

The source code, handbook documents, evaluation results, and README should be tracked by Git.

Generated vector database files and environment files should not be committed.

Recommended `.gitignore` entries:

```gitignore
**/chroma_db/
**/.env
**/__pycache__/
*.pyc
```

The virtual environment should also remain outside version control.

## 13. Results and Learning Outcomes

The task demonstrates:

- Loading and splitting handbook documents.
- Creating embeddings and storing them in a vector database.
- Retrieving policy information through semantic search.
- Implementing custom Python tools for attendance eligibility.
- Applying a relevance threshold to reject unrelated questions.
- Using multiple tools for fee calculations.
- Maintaining context across follow-up questions.
- Evaluating the agent using test cases and execution logs.

The evaluation results and recorded execution output are available in `results.md` and `run_log.txt`.

## 14. Conclusion

This project demonstrates an Agentic AI helpdesk that combines a language model, retrieval-based handbook search, custom tools, and conversation memory. The relevance guard helps prevent the system from answering unrelated questions using irrelevant handbook passages.

The project provides practical experience with Python, LangChain, LangGraph, embeddings, ChromaDB, and tool-based AI workflows.
