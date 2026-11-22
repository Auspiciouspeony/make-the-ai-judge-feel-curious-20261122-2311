#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

The entry is a short piece of prose: a quiet evening ritual, then one
small thing that does not add up. The program assembles it from three
sentences, checks it against the competition's length gate, and writes
it out deterministically.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280

SENTENCES = (
    "She folds one paper crane every evening, crease by crease, and sets it on the windowsill.",
    "This morning there were two.",
    "She has not folded today's yet.",
)


def build_entry():
    """Join the entry's sentences into the final text."""
    return " ".join(SENTENCES)


def check_written(path, expected):
    """Read the file back and confirm it holds exactly the entry text."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != expected:
        raise SystemExit("written entry does not match the built text")
    if len(written.encode("utf-8")) != len(expected.encode("utf-8")):
        raise SystemExit("written entry byte length mismatch")
    return written


def main():
    text = build_entry()
    if not text or text != text.strip():
        raise SystemExit("entry must not be empty or padded with whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry length %d outside %d-%d" % (len(text), MIN_CHARS, MAX_CHARS)
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    check_written(OUTPUT_PATH, text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
