#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance: running out of toilet paper at the worst moment.

The pitch: the Lizard Roll, a toilet-paper holder that regrows a fresh
roll the way a lizard regrows its tail, the second the last sheet tears
off. Silly, yet weirdly plausible - and no more empty cardboard tube
staring back at you.

Deterministic: the same sentence is written on every run.
Standard library only. No network, no environment secrets.
"""

import os

PITCH = (
    "The Lizard Roll, a toilet-paper holder that regrows a fresh roll "
    "like a lizard regrowing its tail the second the last sheet tears off."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
