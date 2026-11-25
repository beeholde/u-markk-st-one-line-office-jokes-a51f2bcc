"""One-Line Office Jokes — entry program.

The whole entry is a single joke about office life. When the grader runs
this program it must produce exactly one file, /output/entry.txt, holding
that one line and nothing else: no trailing newline, no extra whitespace,
no second line.

The joke: a screen-share slip in front of a client. The laugh lands in the
last few words, when the desktop wallpaper turns out to be a beach the
narrator will never afford.
"""

import sys
from pathlib import Path

JOKE = (
    "I shared the wrong screen during my presentation, and the client saw "
    "my desktop wallpaper: a beach I will never afford."
)

# The house gate for this bounty: 1 to 199 characters, one line, UTF-8.
MIN_CHARS = 1
MAX_CHARS = 199


def check_line(text: str) -> None:
    """Refuse to write anything that would fail the entry gate."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise SystemExit(f"line is {len(text)} chars, gate wants 1-199")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    if not text.strip():
        raise SystemExit("line must not be only whitespace")
    text.encode("utf-8")  # raises if the line is not valid UTF-8


def main(argv: list[str]) -> int:
    check_line(JOKE)
    # An explicit path is accepted only so the line can be checked locally;
    # the grader runs with no argument, which writes /output/entry.txt.
    target = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(JOKE, encoding="utf-8")
    print(f"wrote {len(JOKE)} chars to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
