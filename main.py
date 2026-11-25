"""One-line joke for make.fun's "One Line, One Laugh" bounty.

The whole entry is a single funny line, at most 200 characters, written to
/output/entry.txt. One gadget, one ordinary day, one twist: the tracker that
is supposed to keep me honest ends up believing in me more than I do.
The punchline lands harder as one flowing sentence, so the two-sentence
draft is tightened into a single breath with the turn at the end.
"""

from pathlib import Path

JOKE = (
    "My fitness tracker congratulated me on 10,000 steps \u2014 "
    "I was in a car all day, so it believes in me more than I do."
)


def main() -> None:
    # The gate only accepts 1-200 characters of real text, and the judge
    # reads a single cold line, so collapse any stray whitespace first.
    text = " ".join(JOKE.split())
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
