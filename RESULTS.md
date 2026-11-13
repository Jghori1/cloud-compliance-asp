# Scaling results

Random configurations made by src/generate.py (seed 1), with n buckets and
n databases each. Run in a GitHub Codespace, 60 second limit per run.

| n | default solver | --opt-strategy=usc,oll |
|---|---|---|
| 10  | 0.18 s, optimum 57 | 0.08 s, optimum 57 |
| 100 | 0.23 s, optimum 506 | 0.08 s, optimum 506 |
| 200 | 0.62 s, optimum 797 | 0.08 s, optimum 797 |
| 400 | timed out at 60 s, best cost found 1533, not proven optimal | 0.09 s, optimum 1527 |

Times for small n are mostly start-up time.

Observation: with the default (branch-and-bound) search, proving that no
cheaper fix set exists becomes very slow around n = 400. The core-guided
strategy proves the optimum almost instantly on the same input.