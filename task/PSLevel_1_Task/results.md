# Day 8 Task Results

## Configuration

- **LLM Provider:** Groq
- **Model:** `openai/gpt-oss-20b`
- **Embedding Provider:** FastEmbed
- **Embedding Model:** `BAAI/bge-small-en-v1.5`
- **MAX_DISTANCE:** `0.4`

## Evaluation Results

| No. | Question | Tools Used | Result | Correct? |
|---|---|---|---|---|
| 1 | What CGPA do I need to be eligible for placements? | `search_handbook` | CGPA 6.5 or above; no standing arrears | Yes |
| 2 | My attendance is 70%. Can I write the exam? | `check_exam_eligibility` | Condonation of Rs. 500 per course | Yes |
| 3 | What is the total of the CS101 fee, the AI202 fee and the maximum late fee? | `search_handbook`, `get_course_fee`, `calculator` | Rs. 32,000 | Yes |
| 4 | And if I pay only 5 days late instead? | Tools used in the follow-up calculation | Rs. 30,500 | Yes |
| 5 | What is the capital of France? | `search_handbook` | `NO_MATCH`; the agent says it doesn't know | Yes |

## Relevance Guard Scores

- Placement eligibility question: `0.185` (top result: `placement_policy.md`)
- France question: `0.581` (top result: `hostel_rules.md`)
- Threshold: `0.4`

The relevance guard keeps results whose cosine distance is at most 0.4 and returns `NO_MATCH` when no result meets the threshold.