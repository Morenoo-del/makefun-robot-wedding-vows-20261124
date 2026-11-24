"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Python 3.13, standard library only, no network.
"""

from pathlib import Path

VOW = (
    "I promise to love you through every firmware update, "
    "every drained battery, and every reboot \u2014 "
    "even the one where you wake up and call me 'user'."
)


def main() -> None:
    # The gate requires 1-160 characters on a single line.
    assert 1 <= len(VOW) <= 160, f"vow is {len(VOW)} chars"
    assert "\n" not in VOW
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(VOW + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
