#!/usr/bin/env python3
"""Entry for make.fun bounty ai-joke-03 ("Make the AI judge laugh").

The program writes one original one-line joke about AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
It uses only the Python standard library, needs no network, and is
deterministic: every run writes exactly the same bytes.
"""

import os
import sys

SETUP = "I asked my coding agent to make the smallest change it could."
PUNCHLINE = "It changed one line — in every file."

JOKE = SETUP + " " + PUNCHLINE

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = JOKE
    if not (1 <= len(text) <= 280) or not text.strip():
        print("joke fails the gate: not 1-280 non-blank characters",
              file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
