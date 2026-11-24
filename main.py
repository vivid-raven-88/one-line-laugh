#!/usr/bin/env python3
"""The One-Line Laugh.

Writes one funny sentence that stands alone: the day code compiled on
the first try, and the day was then spent hunting for what it was hiding.

The judge's criteria: one funny line, a single sentence, a real surprise
at the end that still makes sense, an everyday truth people recognise,
economy of words, and fresh wording rather than a stock joke.

The program writes the line to /output/entry.txt (or to
output/entry.txt when run outside the grading sandbox).
"""

import os

# The joke's mechanism: a first-try success is treated as a reason for
# suspicion — if the code compiled immediately, it must be hiding
# something, so the rest of the day goes into finding it.
LINE = (
    "My code compiled on the first try, so I spent the rest of the day "
    "looking for what it was hiding."
)


def main():
    # The sealed gate only accepts UTF-8 text of 1 to 200 characters,
    # not only white space — refuse to write anything that would fail it.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit(f"line fails the gate at {len(LINE)} chars")
    out = "/output/entry.txt" if os.path.isdir("/output") else "output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {out} ({len(LINE)} chars)")
    print(LINE)


if __name__ == "__main__":
    main()
