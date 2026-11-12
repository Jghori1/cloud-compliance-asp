# Cloud Compliance Checker

A tool that finds misconfigurations in a described cloud setup and computes
the cheapest set of fixes. Written in Answer Set Programming (Clingo) with a
small Python converter. Built for CSE 579 (Knowledge Representation and
Reasoning).

## How it works

1. `src/convert.py` reads a JSON description of S3 buckets, RDS databases and
   security groups and writes it as Clingo facts.
2. `src/rules.lp` detects violations of five rules.
3. `src/fixes.lp` lists the possible fixes, gives each a cost, and uses
   `#minimize` to choose the cheapest set that repairs every violation.

## Rules checked

1. A public bucket must not hold sensitive data
2. Every bucket must be encrypted
3. Every database must have backups
4. Every database must be encrypted
5. A database must not be reachable from 0.0.0.0/0 on its own port

## Run it

    pip install clingo
    python3 src/convert.py data/example1.json > build/example1.lp
    python3 -m clingo build/example1.lp src/rules.lp src/fixes.lp

The last answer printed (marked OPTIMUM FOUND) is the cheapest fix set.

## Status

Done:
- JSON to Clingo converter for buckets, databases and security groups
- Detection of the five rules above
- Fix options with costs and cost minimization
- Two example configurations

Not done yet:
- Scaling tests on larger configurations
- More rules (logging, wider ingress ranges, IAM)
- Constraints on which fixes are allowed
- Evaluation and write-up

Fix costs are illustrative values, not real prices.