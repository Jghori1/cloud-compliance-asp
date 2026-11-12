import json
import sys

def bucket_facts(buckets):
    """Turn the list of buckets into Clingo fact lines."""
    lines = []
    for b in buckets:
        name = b["id"]
        lines.append(f'bucket("{name}").')
        # Only write a property when it is true.
        if b.get("public"):
            lines.append(f'public("{name}").')
        if b.get("encrypted"):
            lines.append(f'encrypted("{name}").')
        if b.get("sensitive"):
            lines.append(f'sensitive("{name}").')
    return lines

def database_facts(databases):
    """Turn the list of databases into Clingo fact lines."""
    lines = []
    for d in databases:
        name = d["id"]
        lines.append(f'database("{name}").')
        lines.append(f'db_port("{name}",{d["port"]}).')
        lines.append(f'db_sg("{name}","{d["security_group"]}").')
        if d.get("backup"):
            lines.append(f'backup("{name}").')
        if d.get("encrypted"):
            lines.append(f'encrypted("{name}").')
    return lines


def security_group_facts(groups):
    """Turn the list of security groups into Clingo fact lines."""
    lines = []
    for g in groups:
        name = g["id"]
        lines.append(f'security_group("{name}").')
        for rule in g.get("ingress", []):
            lines.append(f'ingress("{name}",{rule["port"]},"{rule["cidr"]}").')
    return lines


def main():
    path = sys.argv[1]                  # the JSON file given on the command line
    with open(path) as f:
        config = json.load(f)

    lines = []
    lines += bucket_facts(config.get("buckets", []))
    lines += database_facts(config.get("databases", []))
    lines += security_group_facts(config.get("security_groups", []))
    print("\n".join(lines))


if __name__ == "__main__":
    main()