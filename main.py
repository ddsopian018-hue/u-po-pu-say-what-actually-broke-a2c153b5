"""Say What Actually Broke — one line of brutally honest error copy.

Writes a single line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt naming the real failure: a save that
silently went nowhere because the document only ever lived in the
crashed tab's memory. Pure standard library, no network, no absolute
paths.
"""

import os

LINE = (
    "Your save didn't save. The document lived only in this tab's "
    "memory, and the tab just crashed, taking 47 minutes of typing "
    "with it. Nothing reached the disk \u2014 reopen the file and "
    "start over."
)

MAX_CHARS = 200


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, (
        f"entry is {len(LINE)} characters, must be 1-{MAX_CHARS}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
