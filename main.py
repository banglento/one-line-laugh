#!/usr/bin/env python3
"""The One-Line Laugh - make.fun entry program.

Writes the one-line entry (a single funny sentence of at most
200 characters) to /output/entry.txt. Standard library only.
"""

import os

ENTRY = "I told my smart speaker to play something relaxing, so it whispered my bank balance."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit(
            "verification failed: /output/entry.txt does not match the entry"
        )
    print(f"wrote {len(text)} characters to {OUTPUT_PATH} (verified)")


if __name__ == "__main__":
    main()
