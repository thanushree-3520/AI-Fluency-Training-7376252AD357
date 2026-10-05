# Day 5 - Model Comparison

## Objective

To compare two cloud-hosted language models using the same prompts and observe their response time, instruction following, and answer quality.

## Provider

Groq Cloud API

## Models Compared

1. openai/gpt-oss-20b
2. openai/gpt-oss-120b

## Prompt 1 - Exact Instruction

Prompt:

Reply with exactly: OK

### gpt-oss-20b
Time: 0.57 seconds
Answer: OK

### gpt-oss-120b
Time: 1.12 seconds
Answer: OK

Observation:
Both models followed the exact instruction correctly.

## Prompt 2 - AI Agent Explanation

Prompt:

In two sentences, what is an AI agent?

### gpt-oss-20b
Time: 0.68 seconds

The model explained that an AI agent perceives its environment, processes information, takes actions toward goals, and can adapt from experience.

### gpt-oss-120b
Time: 0.48 seconds

The model explained that an AI agent receives data, processes it using models or algorithms, takes actions toward specific goals, and can operate autonomously or semi-autonomously.

Observation:
Both models provided relevant explanations and followed the two-sentence instruction.

## Prompt 3 - Scholarship Calculation

Prompt:

A course costs Rs. 18,000 with a 15% scholarship. What is payable? Show the steps.

### gpt-oss-20b
Time: 0.70 seconds

The model calculated the scholarship amount as Rs. 2,700 and started subtracting it from the original fee.

### gpt-oss-120b
Time: 1.01 seconds

The model calculated the scholarship amount as Rs. 2,700 and showed the subtraction step.

Expected payable amount:

Rs. 18,000 - Rs. 2,700 = Rs. 15,300

Observation:
Both models correctly handled the percentage calculation and showed the required steps.

## Overall Comparison

The 20B model was faster for Prompt 1 and Prompt 3.

The 120B model was faster for Prompt 2.

Both models followed instructions correctly and produced relevant answers.

## Important Note

This Day 5 implementation uses the Groq cloud API instead of local Ollama because Ollama was not installed.

Therefore, local Ollama measurements such as loaded model size and local memory usage were not available.

The recorded times are cloud API response times, not local inference times.