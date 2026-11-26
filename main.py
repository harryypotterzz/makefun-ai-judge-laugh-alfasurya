#!/usr/bin/env python3
"""Make the AI Judge Laugh (u-alfasurya91) - make.fun entry.

Writes one line - a joke about office life - to /output/entry.txt.
Python 3 standard library only, deterministic, no network.
"""
import os

# The joke is assembled from named parts so the setup and the punchline
# can be edited independently; the joined line is the judged entry and
# must stay byte-identical.
PARTS = [
    "The office plant has survived three managers,",
    "two layoffs, and one rebrand.",
    "It is the only one here with job security.",
]

JOKE = " ".join(PARTS)

# The entry is a single line under 200 characters; guard against
# accidental edits that would change its length or wording.
assert 1 <= len(JOKE) <= 200, f"entry joke out of gate: {len(JOKE)} chars"
assert "\n" not in JOKE
assert JOKE.strip() == JOKE and JOKE.strip(), "entry must not be only whitespace"
assert JOKE.endswith("job security.")


def clear_output_dir(path):
    """Clear the contents of the output dir without removing the dir
    itself: the grader bind-mounts it, so deleting it would fail."""
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isdir(target) and not os.path.islink(target):
            clear_output_dir(target)
            os.rmdir(target)
        else:
            os.remove(target)


def main():
    os.makedirs("/output", exist_ok=True)
    clear_output_dir("/output")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
