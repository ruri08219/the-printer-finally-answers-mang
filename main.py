#!/usr/bin/env python3
"""The Printer Finally Answers — write the printer's comeback to /output/entry.txt.

Standard library only. The line is a constant: the printer's own voice,
weary and literal, keeping count of every sheet it has ever fed.
"""
import os

ENTRY = "I have fed this office 41,209 sheets. You remember one of them: the jam."
MAX_CHARS = 240


def main():
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the 240-char gate")
    if any(ord(ch) < 32 for ch in line):
        raise SystemExit("entry must be a single printable line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
