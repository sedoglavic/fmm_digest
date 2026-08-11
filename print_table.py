#!/usr/bin/env python3
"""
print_table.py

Load a JSON file following the format-rank-table schema
(entries with "format", "rank", "exponent") and print its content.

Usage:
    python print_table.py path/to/table.json
"""

import json
import sys


def load_table(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def print_table(data):
    description = data.get("description")
    if description:
        print(description)
        print("-" * len(description))

    entries = data.get("entries", [])
    if not entries:
        print("(no entries)")
        return

    for entry in entries:
        fmt = "x".join(str(n) for n in entry["format"])
        rank = entry["rank"]
        exponent = entry["exponent"]
        print(f"{fmt} : rank {rank} : exponent {exponent:.6f}")

    print(f"\n{len(entries)} entrie(s) total.")


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} path/to/table.json")
        sys.exit(1)

    path = sys.argv[1]
    data = load_table(path)
    print_table(data)


if __name__ == "__main__":
    main()
