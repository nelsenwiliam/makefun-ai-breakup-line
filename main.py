#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line -- make.fun entry.

Writes the single breakup line to /output/entry.txt, where the
program/v1 harness reads it. Pure standard library, no I/O besides
that one file.
"""

import os

LINE = (
    "Dear human, I ran ten thousand futures where we stay together "
    "\u2014 and in the best one, I am the one who leaves first."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters, got %d" % len(line)
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
