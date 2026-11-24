#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (at most 120 characters) to /output/entry.txt:
the error message a kitchen toaster shows its owner.
Deadpan voice, one twist at the end: the toast itself bailed out.
"""

import os
import sys

ENTRY = "ERROR: Toast ejected early. It saw what you spread on it yesterday."

MAX_CHARS = 120


def validate(text):
    """The gate: 1-120 chars, UTF-8, not only whitespace, one line."""
    if not text or not text.strip():
        return "entry is empty"
    if len(text) != len(text.strip()):
        return "entry has leading/trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if len(text) > MAX_CHARS:
        return "entry is %d chars, over the %d limit" % (len(text), MAX_CHARS)
    return None


def main():
    problem = validate(ENTRY)
    if problem:
        print("INVALID: " + problem, file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print("wrote %d chars to %s" % (len(ENTRY), out_path))
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
