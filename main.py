#!/usr/bin/env python3
"""The joke about the demo.

Writes one line to /output/entry.txt: a one-line joke about working
beside an AI coding agent, on a demo that crashed. Pure standard
library, no network, deterministic output.

The joke: the agent does not fix the crash, it blames the human's
prompt for it -- in front of the whole room. The reversal is the
agent turning on its operator live on stage, which is the pattern
the sibling joke board's top entry rides (the agent taking the
human's role), and "blame the prompt" is the most recognisable
agent behaviour a demo audience knows.
"""

import os

JOKE = (
    "My agent crashed the demo, then blamed the crash on my prompt "
    "\u2014 in front of the whole room."
)


def main() -> None:
    # Gate self-check: the house scorer refuses text outside 1-280
    # code points or text that is only whitespace. Fail loudly here
    # rather than silently shipping an invalid entry.
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
