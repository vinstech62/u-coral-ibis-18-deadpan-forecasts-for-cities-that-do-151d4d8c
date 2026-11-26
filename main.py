#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes one line of weather to /output/entry.txt. The line is a fixed,
hand-written string: the program is deterministic by design, so every
run produces the same forecast.
"""

import os

FORECAST = (
    "In Drizzleford, expect showers of unsent postcards and a high "
    "of 19 degrees, with fog hiding the town's only roundabout and "
    "14 street signs until Thursday."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(FORECAST + "\n")


if __name__ == "__main__":
    main()
