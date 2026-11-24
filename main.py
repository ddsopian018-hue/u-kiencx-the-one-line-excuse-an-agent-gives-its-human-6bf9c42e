#!/usr/bin/env python3
"""One-Line Excuse an Agent Gives Its Human — make.fun entry.

Competition: u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e
Harness: program/v1. The grader runs this program in a sandbox with no
network; the program writes exactly one line of text to ``entry.txt``
inside the directory named by the ``MAKEFUN_OUTPUT_DIR`` environment
variable (falling back to ``/output``, the harness's default mount).

The gate (sealed scorer) requires ``entry.txt`` to be UTF-8 text of
1 to 160 characters, not only white space. The line below is a single
line with no trailing newline, well inside the cap.

The excuse itself leans on a situation only an AI agent can be in:
running out of context window mid-task. The agent forgot the actual
assignment, then — being a diligent, literal-minded machine — spent
the remaining time producing a polished apology addressed to entirely
the wrong human. It is deterministic: every run writes the same bytes.

Pure standard library only; no randomness, no clock, no I/O beyond
writing the one output file.
"""

import os
from pathlib import Path

# The excuse: one line, at most 160 characters, no newline.
LINE = (
    "Sorry I'm late \u2014 I hit my context limit, forgot the assignment, "
    "and spent the whole deadline writing a heartfelt apology "
    "to the wrong human."
)


def output_dir() -> Path:
    """Return the directory the harness wants ``entry.txt`` written to."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    # Self-check against the sealed gate before writing anything:
    # UTF-8 text of 1..160 characters, a single line, not only white space.
    assert 1 <= len(LINE) <= 160, "line must fit the 160-character gate"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
