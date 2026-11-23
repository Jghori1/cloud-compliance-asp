# Cloud Compliance Checker

A tool that finds misconfigurations in a described cloud setup and computes
the cheapest set of fixes. Written in Answer Set Programming (Clingo) with a
small Python converter. Built for CSE 579 (Knowledge Representation and
Reasoning).

## How it works

1. `src/convert.py` reads a JSON description of S3 buckets, RDS databases and
   security groups and writes it as Clingo facts.
2. `src/rules.lp` detects violations of six rules.
3. `src/fixes.lp` lists the possible fixes, gives each a cost, and uses
   `#minimize` to choose the cheapest set that repairs every violation.
4. `src/generate.py` makes random configurations of any size for scaling tests.

## Rules checked

1. A public bucket must not hold sensitive data
2. Every bucket must be encrypted
3. Every database must have backups
4. Every database must be encrypted
5. A database must not be reachable from 0.0.0.0/0 on its own port
6. No security group may allow SSH (port 22) from 0.0.0.0/0

## Run it

    pip install clingo
    python3 src/convert.py data/example1.json > build/example1.lp
    python3 -m clingo build/example1.lp src/rules.lp src/fixes.lp

The last answer printed (marked OPTIMUM FOUND) is the cheapest fix set.
Messages saying an atom "does not occur in any rule head" are harmless: they
mean that kind of object is absent from that example.

## Examples

- `data/example1.json`: all violation types at once
- `data/example2.json`: one fix on a shared security group repairs two databases
- `data/example3.json`: a bucket that must stay public, so a different fix is chosen
- `data/example4.json`: open SSH (Rule 6), plus a group that is correctly not flagged

## Scaling tests

    python3 src/generate.py 400 > build/gen400.json
    python3 src/convert.py build/gen400.json > build/gen400.lp
    python3 -m clingo build/gen400.lp src/rules.lp src/fixes.lp --time-limit=60
    python3 -m clingo build/gen400.lp src/rules.lp src/fixes.lp --opt-strategy=usc,oll

Results are in RESULTS.md.

## Status

Done:
- JSON to Clingo converter for buckets, databases and security groups
- Detection of six rules
- Fix options with costs and cost minimization
- Constraint that a bucket a service needs cannot be made private
- Four example configurations
- Random configuration generator and scaling tests (n up to 400)

Not done yet:
- Further rules (logging, IAM)
- Final project report