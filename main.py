"""Entry for make.fun: The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if sent by a houseplant, to
``entry.txt`` inside the output directory. Standard library only, no
network access, fully deterministic: the same bytes every run.

The output directory is $MAKEFUN_OUTPUT_DIR when set, else /output.
The entry is written with no trailing newline so the file holds exactly
the entry text (108 characters, inside the 1-120 gate).
"""

import os
import sys

# The entry: a fern's out-of-office reply. The joke is the plant's own
# life -- ignored and unwatered since March -- told in flat office voice.
ENTRY = (
    "I am out of the office. I have been out of the office since March. "
    "Nobody has watered me since March. \u2014 Fern"
)

MAX_CHARS = 120


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} chars, outside the 1-{MAX_CHARS} gate",
              file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and confirm the file holds exactly the entry text.
    if open(path, encoding="utf-8").read() != text:
        print("read-back mismatch: file does not match entry", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
