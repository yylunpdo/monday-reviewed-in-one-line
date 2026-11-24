#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one single-line review of the entrant's own Monday to
/output/entry.txt. The line is a literal one-star review: concrete
Monday details (a quitting alarm, 47 unread emails, a 9am meeting
about the next meeting) with the punchline in classic review
language ("Would not recommend."). Pure standard library, no
network, no input files, deterministic output.
"""

import os

TEXT = (
    "Monday: one star. My alarm quit, my inbox hit 47 unread, "
    "and my 9am was a meeting about the next meeting. "
    "Would not recommend."
)


def main() -> None:
    text = TEXT.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    # Read back and re-check the gate: UTF-8, one line, 1-200 chars.
    with open(out_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    assert written == text + "\n", "entry.txt content mismatch"
    assert written.count("\n") == 1, "entry must be exactly one line"


if __name__ == "__main__":
    main()
