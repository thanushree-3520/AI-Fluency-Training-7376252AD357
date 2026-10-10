# PS Level 1 Class — Retrieval-Augmented Generation and Agentic AI

## 1. Project Overview

This project explores the development of an AI-powered college helpdesk using Python, Large Language Models (LLMs), document retrieval, vector databases, and AI agent workflows.

The project progresses through five stages, starting with handbook ingestion and semantic search, then building a RAG chain, learning LangGraph fundamentals, and developing an agentic RAG application.

The handbook contains information about college fees, examination regulations, hostel rules, library policies, and AI Fluency Training.

## 2. Objectives

- Load college handbook documents from Markdown files.
- Split documents into smaller text chunks.
- Generate embeddings and store them in ChromaDB.
- Retrieve relevant passages using semantic similarity.
- Build a Retrieval-Augmented Generation (RAG) chain.
- Learn graph-based AI workflows with LangGraph.
- Develop an agentic RAG application using tools and an LLM.
- Configure model providers and dependencies through shared configuration.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| LangChain | Document processing, retrieval, and model integration |
| LangGraph | Graph-based agent workflows |
| ChromaDB | Vector database for handbook documents |
| FastEmbed | Text embedding generation |
| Groq | Configured cloud LLM provider |
| Ollama | Alternative local LLM provider |
| Markdown | Handbook document format |
| Git and GitHub | Version control |

### Configuration

The project uses the following configured model settings:

- LLM provider: Groq
- Model: `openai/gpt-oss-20b`
- Embedding provider: FastEmbed
- Embedding model: `BAAI/bge-small-en-v1.5`
- Vector database: ChromaDB
- Collection: `college_helpdesk`

The configuration is managed by `lc_config.py` and environment variables in `.env`.

## 4. Project Structure

```text
PSLevel_1_Class/
├── data/
│   ├── ai_fluency_training.md
│   ├── exam_regulations.md
│   ├── fee_policy.md
│   ├── hostel_rules.md
│   └── library.md
├── Output/
│   └── execution screenshots
├── chroma_db/
│   └── generated vector database
├── 1_ingest.py
├── 2_search.py
├── 3_rag_chain.py
├── 4_graph_basics.py
├── 5_agentic_rag.py
├── lc_config.py
├── requirements.txt
├── .env
└── README.md
```

**Note:** `.env`, `chroma_db/`, and `__pycache__/` are local files or generated artifacts and should not be committed to GitHub.

## 5. Stage 1 — Handbook Ingestion

**File:** `1_ingest.py`

### Objective

Load handbook Markdown files, split their contents into chunks, create embeddings, and store the resulting vectors in ChromaDB.

### Workflow

1. Read Markdown files from the `data/` folder.
2. Convert the file contents into document objects.
3. Split documents into smaller chunks with overlap.
4. Generate embeddings using the configured embedding model.
5. Store the chunks and metadata in ChromaDB.

### Run

```powershell
python 1_ingest.py
```

The output reports how many documents were loaded, how many chunks were created, and how many vectors were stored.

## 6. Stage 2 — Semantic Search

**File:** `2_search.py`

### Objective

Retrieve handbook passages that are semantically related to a user's question.

### Workflow

1. Receive a natural-language query.
2. Convert the query into an embedding.
3. Search the ChromaDB collection.
4. Return matching passages with similarity-distance scores and source filenames.

### Example questions

- How much is the late fee for paying fees after the due date?
- What time should hostel students return?
- Can I write the exam with 70% attendance?

### Run

```powershell
python 2_search.py
```

The output helps evaluate whether the correct handbook passages are retrieved.

## 7. Stage 3 — Retrieval-Augmented Generation

**File:** `3_rag_chain.py`

### Objective

Combine document retrieval with language-model generation.

### Workflow

1. Receive a question from the user.
2. Retrieve relevant handbook passages.
3. Provide the retrieved context to the language model.
4. Generate an answer based on the supplied context.

RAG helps the model answer questions using information from the college handbook instead of relying only on its general training knowledge.

### Run

```powershell
python 3_rag_chain.py
```

## 8. Stage 4 — LangGraph Basics

**File:** `4_graph_basics.py`

### Objective

Explore the fundamental concepts of LangGraph and graph-based application workflows.

A graph-based workflow typically consists of:

- **State:** Information shared between workflow steps.
- **Nodes:** Functions that perform operations.
- **Edges:** Connections that determine the next step.
- **Execution:** Processing state through the graph.

These concepts provide a foundation for creating more complex AI agents.

### Run

```powershell
python 4_graph_basics.py
```

## 9. Stage 5 — Agentic RAG

**File:** `5_agentic_rag.py`

### Objective

Combine handbook retrieval with an AI agent workflow.

The agent can use available tools to answer questions requiring handbook information or structured operations.

### General workflow

1. Receive the user's question.
2. Pass the conversation and system instructions to the model.
3. Determine whether a tool is required.
4. Execute the requested tool when applicable.
5. Return tool results to the model.
6. Produce the final response.

### Run

```powershell
python 5_agentic_rag.py
```

This stage builds on the earlier ingestion, retrieval, RAG, and graph concepts.

## 10. Shared Configuration

**File:** `lc_config.py`

The configuration module centralizes the settings used by the project, including:

- Language-model provider selection.
- Model initialization.
- Embedding provider selection.
- Embedding model configuration.
- ChromaDB persistence directory.
- Vector-store collection configuration.

Keeping configuration in one module avoids repeating model and database setup across the Python scripts.

## 11. Setup Instructions

### Step 1: Open the project folder

Open a terminal in the `lab/PSLevel_1_Class` directory.

### Step 2: Activate the virtual environment

From this directory, activate the repository-root virtual environment:

```powershell
..\..\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 4: Configure environment variables

Ensure `.env` contains the provider and model settings required by `lc_config.py`.

Keep API credentials private. Never upload secret keys to GitHub.

### Step 5: Run the stages

Run the scripts in order:

```powershell
python 1_ingest.py
python 2_search.py
python 3_rag_chain.py
python 4_graph_basics.py
python 5_agentic_rag.py
```

Run each command from the `PSLevel_1_Class` directory. Stage 1 should be completed before running searches that depend on the vector database.

## 12. Version Control

Recommended `.gitignore` entries:

```gitignore
**/.env
**/chroma_db/
**/__pycache__/
*.pyc
```

The source code, handbook documents, dependency file, README, and selected screenshots can be tracked in Git.

The generated vector database can be recreated by running `1_ingest.py`.

## 13. Learning Outcomes

Through this project, I explored:

- Document loading and text chunking.
- Embeddings and semantic search.
- Vector database storage and retrieval.
- Retrieval-Augmented Generation.
- Language-model integration.
- LangGraph state, nodes, and edges.
- Tool-based AI agent workflows.
- Environment configuration and Python dependencies.

## 14. Conclusion

The PS Level 1 class project demonstrates the progression from handbook document ingestion to semantic retrieval, RAG, graph-based workflows, and agentic RAG.

It provides practical experience in building AI applications that connect language models with external documents, vector databases, and executable tools.
