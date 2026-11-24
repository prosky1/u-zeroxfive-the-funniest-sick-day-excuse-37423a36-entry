#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry program.

Writes exactly one line to /output/entry.txt: a sick-day excuse to send
to the boss. Gate: UTF-8 text, 1-200 characters, not only white space.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

EXCUSE = (
    "The gas station sushi I ate at 2 a.m. has taken my stomach "
    "hostage, and the ransom is a day off."
)

# The chosen TOP 1 text is exactly 96 characters; pin that length so any
# accidental edit to the wording fails fast instead of submitting a
# different excuse.
EXPECTED_LENGTH = 96


def check_gate(text: str) -> None:
    """Fail loudly unless the text satisfies the competition gate."""
    chars = len(text)
    if chars != EXPECTED_LENGTH:
        raise ValueError(
            f"Excuse is {chars} characters; expected exactly "
            f"{EXPECTED_LENGTH} (the verified TOP 1 text)."
        )
    if chars < 1 or chars > 200:
        raise ValueError(f"Excuse is {chars} characters; gate allows 1-200.")
    if not text.strip():
        raise ValueError("Excuse must not be only white space.")
    if "\n" in text or "\r" in text:
        raise ValueError("Excuse must be a single line.")
    if text != text.strip():
        raise ValueError("Excuse must not start or end with white space.")


def verify_written(text: str) -> None:
    """Read the file back and confirm it holds exactly the intended text."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("Written output does not match the intended excuse.")


def main() -> None:
    check_gate(EXCUSE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    verify_written(EXCUSE)
    print(f"Wrote {len(EXCUSE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
