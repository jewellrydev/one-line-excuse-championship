#!/usr/bin/env python3
"""Held the Door — entry for The One-Line Excuse Championship on make.fun.

Prints exactly one line: the excuse an AI agent gives its human when
something has gone wrong.
"""

LINE = "The file deleted itself out of respect for your storage limits; I merely held the door and looked the other way."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
