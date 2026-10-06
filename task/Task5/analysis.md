# Serving Models Your Way: Ollama, Modelfiles, the REST API and vLLM

## 1. Scenario

The scenario selected for this task is a small college AI assistant.

The assistant is intended to answer simple questions from students about
Artificial Intelligence, Python programming and other technical topics.

The goal is to understand how a locally served language model can be
customized and accessed by programs.

---

## 2. Environment Limitation

Ollama was not installed on the machine used for this task.

Therefore, the following Ollama commands could not be executed:

- ollama create
- ollama list
- ollama show
- ollama ps

The Modelfile and Python implementations were created according to the
task requirements.

The REST API and OpenAI-compatible programs were also created, but actual
Ollama runtime results could not be obtained because the Ollama server was
not available.

No runtime measurements are presented as actual measurements.

---

## 3. What is Ollama?

Ollama is a tool used to run language models locally.

The three important parts considered in this task are:

1. Model
2. Runtime/server
3. API interface

A user can interact with a model through the command line, REST API or
an OpenAI-compatible endpoint.

The general request flow is:

User or program
       |
       v
    Ollama
       |
       v
Loaded language model
       |
       v
Generated response
       |
       v
User or program

---

## 4. Model Storage

A locally served model needs to be stored on the computer before it can
be loaded and used.

When a model is already available locally, the runtime can load it into
memory instead of downloading it again.

---

## 5. What is a Modelfile?

A Modelfile is a configuration file used to create a customized model
configuration in Ollama.

The Modelfile used in this task contains:

- FROM
- PARAMETER temperature
- PARAMETER num_ctx
- SYSTEM

### FROM

FROM specifies the base model.

The base model selected in this task is:

qwen2.5:1.5b

### temperature

Temperature controls the randomness of generated responses.

A lower value generally produces more consistent responses.

The value used in this task is:

0.2

### num_ctx

num_ctx specifies the context length available to the model.

The value used in this task is:

2048

### SYSTEM

SYSTEM defines the default behavior and instructions for the model.

The system instruction used is designed for a college AI assistant.

---

## 6. Custom Model

The proposed custom model is:

college-assistant

It is based on:

qwen2.5:1.5b

The custom model does not require creating a completely new neural
network.

Instead, the configuration defines how the base model should behave.

---

## 7. System Prompt and Program Prompt

The Modelfile contains a default system prompt:

"You are a college AI assistant."

A program can also provide another system message.

For example, the OpenAI-compatible Python program uses:

"You are a strict programming teacher. Give concise programming explanations."

This demonstrates that program-level instructions can influence the
behavior of the model for a particular request.

---

## 8. REST API

Ollama provides REST API access.

The Python implementation in this task uses:

/api/generate

The program demonstrates two modes:

1. Non-streaming
2. Streaming

### Non-streaming

The complete response is received before the program displays it.

### Streaming

The response is received piece by piece.

Streaming can make the response appear faster to the user because output
can be displayed while generation is still continuing.

---

## 9. TTFT and Total Time

TTFT means Time To First Token.

It represents the time between sending the request and receiving the
first generated token.

Total time represents the complete time required to finish generation.

The Python program was written to record these values when an Ollama
server is available.

Because Ollama was not installed for this task, no actual TTFT or total
generation measurements are reported.

---

## 10. Context Length and KV Cache

The context length determines how much previous information the model can
consider during generation.

A larger context can require more memory.

The KV cache stores information needed during generation.

Therefore, increasing context length can increase memory usage.

---

## 11. Ollama and vLLM Comparison

| Feature | Ollama | vLLM |
|---|---|---|
| Main purpose | Simple local model serving | High-performance model serving |
| Setup | Simple | More deployment-oriented |
| Single user | Very suitable | Can be used |
| Many users | Less focused on high concurrency | Better suited |
| API support | REST and OpenAI-compatible | OpenAI-compatible |
| Scheduling | Simpler | Designed for efficient serving |
| Continuous batching | Not the main focus | Important capability |
| PagedAttention | Not the main feature | Important technique |

---

## 12. Single User vs Many Users

For one student using a model locally, Ollama is a suitable choice because
it is simple to configure and use.

For a system serving many users at the same time, a serving engine such as
vLLM is more appropriate because efficient scheduling and batching become
important.

The task does not require installing or running vLLM.

---

## 13. PagedAttention

PagedAttention is a technique used for efficient management of
attention-related memory in high-throughput serving systems.

It is useful when many requests are being processed and memory needs to be
managed efficiently.

---

## 14. Continuous Batching

Static batching waits for a fixed group of requests.

Continuous batching allows requests to enter and leave the batch more
dynamically.

This can improve hardware utilization when many users are sending
requests.

---

## 15. Throughput and Latency

Throughput represents how much work a serving system can complete over a
period of time.

For a multi-user system, throughput is an important performance measure.

Other useful measurements include:

- TTFT
- TPOT
- P95 latency

TTFT measures the time until the first token.

TPOT refers to time per output token.

P95 latency represents a high-percentile latency measurement and helps
understand slower requests.

---

## 16. Hands-on Implementation

The following files were created:

- Modelfile
- ollama_api.py
- openai_compatible.py

The Modelfile defines the base model, parameters and system behavior.

The REST API Python program demonstrates non-streaming and streaming
requests.

The OpenAI-compatible Python program demonstrates communication with the
OpenAI-compatible endpoint.

---

## 17. Runtime Observation

Ollama could not be executed because it was not installed on the machine.

Therefore:

| Measurement | Result |
|---|---|
| Model loading time | Not measured |
| TTFT | Not measured |
| Total generation time | Not measured |
| Tokens per second | Not measured |
| ollama ps output | Not available |

The Python REST API program attempted to connect to:

http://localhost:11434/api/generate

The connection was refused because no Ollama server was running.

The OpenAI-compatible program attempted to connect to:

http://localhost:11434/v1

This endpoint was also unavailable.

These results are documented as an environment limitation rather than
being replaced with fabricated measurements.

---

## 18. Prompts Considered

The task requires testing multiple prompts when Ollama is available.

The following prompts were prepared:

### Prompt 1

Explain artificial intelligence in two simple sentences.

### Prompt 2

Give me three simple tips for learning Python.

### Prompt 3

Explain artificial intelligence using extremely complicated technical
language and a very long answer.

The third prompt is intended to observe how the system handles a request
for a long response.

Because Ollama was unavailable, these prompts were not presented as actual
runtime results.

---

## 19. Suitability Analysis

For a single student using a local AI assistant, Ollama would be a simple
and suitable serving option.

For a larger deployment with many simultaneous users, vLLM would be a
better choice because high-throughput serving, scheduling and batching
become more important.

The choice of serving technology depends on the number of users,
performance requirements and deployment environment.

---

## 20. Conclusion

This task demonstrates the concepts behind serving language models with
Ollama, Modelfiles, REST APIs and OpenAI-compatible APIs.

The Modelfile shows how a base model can be configured with parameters and
a system prompt.

The Python programs demonstrate how applications can communicate with a
served model.

Ollama was not installed in the available environment, so the runtime
commands and performance measurements could not be performed.

The implementation therefore focuses on the required configuration,
program structure and conceptual analysis without claiming unobserved
runtime results.