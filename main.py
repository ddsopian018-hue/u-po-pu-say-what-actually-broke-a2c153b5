#!/usr/bin/env python3
"""Say What Actually Broke - make.fun entry.

Writes one line (190 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
the plain, specific truth about a lost document. Pure stdlib,
no network, no secrets, no hard-coded output path.
"""

import os

# The joke: the save that never saved — 47 minutes of typing existed
# only in the tab's memory, so the crash didn't lose the file, it
# revealed there never was one. A specific failure, not a generic crash.
LINE = (
    "Your save didn't save. The document lived only in this tab's memory, "
    "and the tab just crashed, taking 47 minutes of typing with it. "
    "Nothing reached the disk \u2014 reopen the file and start over."
)


def main():
    assert 1 <= len(LINE) <= 200, "LINE must be 1-200 characters"
    assert "\n" not in LINE, "LINE must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
