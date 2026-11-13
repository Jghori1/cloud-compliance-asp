import json
import random
import sys


def make_config(n, seed):
    """Make a random cloud description with n buckets and n databases."""
    rng = random.Random(seed)
    groups = max(1, n // 5)
    config = {"buckets": [], "databases": [], "security_groups": []}

    for i in range(n):
        config["buckets"].append({
            "id": f"b{i}",
            "public": rng.random() < 0.3,
            "encrypted": rng.random() < 0.7,
            "sensitive": rng.random() < 0.4,
        })

    for g in range(groups):
        ingress = [{"port": 22, "cidr": "10.0.0.0/16"}]
        if rng.random() < 0.4:
            ingress.append({"port": 3306, "cidr": "0.0.0.0/0"})
        config["security_groups"].append({"id": f"sg{g}", "ingress": ingress})

    for i in range(n):
        config["databases"].append({
            "id": f"db{i}",
            "port": 3306,
            "security_group": f"sg{rng.randrange(groups)}",
            "backup": rng.random() < 0.7,
            "encrypted": rng.random() < 0.7,
        })

    return config
def main():
    n = int(sys.argv[1])
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    print(json.dumps(make_config(n, seed), indent=2))


if __name__ == "__main__":
    main()