#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters.

Writes the robot vacuum's excuse for missing a spot to
/output/entry.txt. Pure standard library, deterministic:
the same line on every run.
"""

import os

LINE = "I spared that spot. It is the last surviving witness to what the dog did on Tuesday."


def main() -> None:
    # The sealed scorer gates on 1-200 characters; fail loudly here
    # rather than ever writing an invalid entry.
    assert 1 <= len(LINE) <= 200, len(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
