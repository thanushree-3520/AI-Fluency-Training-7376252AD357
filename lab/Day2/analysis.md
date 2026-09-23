# 11. Observations

## 11.1 Paper trace vs agent trace

| Item | Your paper trace | The agent |
|---|---|---|
| Number of fee lookups | 3 | 3 |
| Number of calculator calls | 3 | 3 |
| Total steps | 13 rows | 4 steps |
| Any tools called in parallel? (Y/N) | N | Y |
| Final answer | Rs. 6,750 | Rs. 6,750 |
| Correct? (Y/N) | Y | Y |

## 11.2 Chain-of-Thought comparison

| Question | Without CoT correct? (Y/N) | With CoT correct? (Y/N) | Which reply was longer? |
|---|---|---|---|
| Q1 instalments | N | Y | With CoT |
| Q2 lab sittings | Y | Y | With CoT |
| Q3 tallest and shortest | Y | Y | With CoT |

## 11.3 Self-consistency

| Item | Value |
|---|---|
| Answers seen across the 5 runs | Rs. 9,562.50, Rs. 9,562.50, Rs. 11,250, Rs. 9,562.50, Rs. 9,562.50 |
| Majority answer | Rs. 9,562.50 |
| Was the majority answer correct? | Y |
| Result when temperature = 0 | The five answers became almost identical |