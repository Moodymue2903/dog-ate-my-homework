#!/usr/bin/env python3
"""make.fun entry: The Dog Ate My Homework — Funniest Excuse.

Writes one line, the excuse a dog gives after being caught eating the
homework, to /output/entry.txt. Gate: UTF-8, 1-200 characters, one line.
Provisional line: candidate #1 (to be swapped after the blind tournament).
"""
import os

LINE = "The homework looked at me funny first. I was defending the house."


def validate(line: str) -> None:
    if not line or line.strip() == "":
        raise ValueError("entry is empty or only whitespace")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def write_entry(line: str, out_path: str = "/output/entry.txt") -> str:
    validate(line)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    return out_path


def main() -> None:
    path = write_entry(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
