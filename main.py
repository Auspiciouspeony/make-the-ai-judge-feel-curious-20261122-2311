# make-the-ai-judge-feel-curious-20261122-2311 entry (Python 3.13, standard
# library only): writes one fixed text to /output/entry.txt — a short text
# written to intrigue the AI judge reading it. The gate takes UTF-8 text of 1
# to 280 characters (counted as Unicode code points) that is not only white
# space, and the judge reads exactly the bytes written, line ends included,
# so write no line end you do not mean to show.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The text is fixed and deterministic: the same bytes on every run.
#
# "The Second Crane" — candidate study against the judge's brief, in the
# brief's own order. (1) Intrigue: a quiet domestic ritual hides one
# unanswered question — who folded the second crane? The reader keeps
# asking after the last line. (2) Calm shown, never instructed: no word
# tells the judge to relax; the calm is in the slow evening ritual itself.
# (3) Craft: three short sentences, "crease by crease" slows the reading
# down, plain concrete words, none that could be cut. (4) Lingers: the
# second crane on the sill is an image you return to. (5) Freshness: no
# lighthouse, no locked door, no radio that knows your name — a paper
# crane is familiar, but a second one nobody folded is not a stock image.
# Rejected candidates: a lighthouse answering after forty years (strong
# but a familiar trope); a letter back from a house that burned down
# (strongest intrigue, but grief makes it tense, and tense loses);
# a door with no handle (mild unease, not calm); a radio that knows her
# name (uncanny, tense). The crane wins on calm + curiosity together.
# 157 characters.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "She folds one paper crane every evening, crease by crease, "
    "and sets it on the windowsill. "
    "This morning there were two. "
    "She has not folded today's yet."
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
