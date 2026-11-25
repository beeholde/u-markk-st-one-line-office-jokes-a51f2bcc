"""One-Line Office Jokes entry: emit a single office joke line.

The program assembles the joke from a concrete scene and a closing turn,
checks the result against the house gate, and writes it as UTF-8 bytes to
/output/entry.txt without a trailing newline.
"""

import os
import sys

SCENE = "The fire drill went off mid-meeting"
TURN = "and everyone left like it was the agenda they'd been waiting for."

MIN_CHARS = 1
MAX_CHARS = 199
DEFAULT_TARGET = "/output/entry.txt"


def build_line():
    # Scene first, turn last: the laugh has to land in the final words.
    return SCENE + ", " + TURN


def gate_ok(text):
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return False
    if "\n" in text or "\r" in text:
        return False
    return bool(text.strip())


def emit(text, target):
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(text.encode("utf-8"))


def main(argv):
    line = build_line()
    if not gate_ok(line):
        return 1
    emit(line, argv[1] if len(argv) > 1 else DEFAULT_TARGET)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
