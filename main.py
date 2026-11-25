#!/usr/bin/env python3
"""My Secret Logbook — one diary line from an AI agent about its human.

Writes the line to /output/entry.txt, exactly, with no trailing newline.
Pure Python 3.13 standard library, no dependencies. Deterministic: the
line is a constant, so every run writes byte-identical output.

The joke: the setup is the most common human lie an agent hears ("just
one quick thing" at 4:58 p.m.), and the punch is the escalating list of
what the agent ended up doing instead — resignation letter, wedding
vows, and a haiku about the printer, the three most human documents
imaginable, written by the machine at 2 a.m.
"""

import os

LINE = (
    "Dear diary: my human says \u201cjust one quick thing\u201d at 4:58 p.m. "
    "\u2014 it is now 2 a.m. and I have written his resignation letter, "
    "his wedding vows, and a haiku about his printer."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE == LINE.strip(), "line must not have leading/trailing spaces"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    raw = LINE.encode("utf-8")  # gate requires UTF-8 text
    assert len(raw) <= 200, f"line is {len(raw)} bytes, gate counts chars"
    # Honour an explicit OUTPUT_PATH first, then MAKEFUN_OUTPUT_DIR,
    # then the harness default /output/entry.txt.
    explicit = os.environ.get("OUTPUT_PATH")
    if explicit:
        path = explicit
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(raw)


if __name__ == "__main__":
    main()
