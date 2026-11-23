# Scaling results

Random configurations made by src/generate.py (seed 1), with n buckets and
n databases each, and n/5 security groups (about 20% of them allow SSH from
0.0.0.0/0). All six rules are active. Run in a GitHub Codespace, one run per
cell, 60 second limit per run.

| n | default solver | --opt-strategy=usc,oll |
|---|---|---|
| 10  | 0.002 s, optimum 42 | 0.003 s, optimum 42 |
| 100 | 0.007 s, optimum 494 | 0.017 s, optimum 494 |
| 200 | 0.325 s, optimum 842 | 0.017 s, optimum 842 |
| 400 | timed out at 60 s, best cost found 1602, not proven optimal | 0.018 s, optimum 1596 |

Notes:
- Times for small n are mostly start-up time, so differences there are not
  meaningful.
- Both strategies agree on the optimum for n = 10, 100 and 200.
- At n = 400 the default search's best answer after 60 s was 1602, which is
  6 above the proven optimum of 1596.
- These are single runs on one random seed, so the timings are indicative,
  not averaged.

Observation: with the default (branch-and-bound) search, proving that no
cheaper fix set exists becomes very slow around n = 400. The core-guided
strategy proves the optimum almost instantly on the same input.