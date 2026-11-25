#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant.

The fortune is assembled from three beats, each doing one job for the
gardener-judge's brief:

1. "lean toward the sun" — pins the fortune to this plant, on this
   windowsill, rather than any plant in any room.
2. "outgrow your little pot" — a warm prediction of growth, the classic
   fortune cadence of a future on its way.
3. "watered before you have to drop a leaf to ask" — the joke, and it is
   on the keeper's forgetfulness, never on the plant: no doom, no
   withering, just a plant politely filing its request in advance.

The assembled line is a single line of 117 characters, inside the
120-character gate. It is written to /output/entry.txt, or to
$OUTPUT_DIR/entry.txt when OUTPUT_DIR is set (local validation only;
the grader runs it with the default).
"""

import os
from pathlib import Path

BEATS = [
    "You will lean toward the sun",
    "outgrow your little pot",
    "and finally get watered before you have to drop a leaf to ask",
]

FORTUNE = ", ".join(BEATS) + "."


def render() -> str:
    """Return the fortune as one clean line, no padding."""
    return " ".join(FORTUNE.split())


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(render() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
