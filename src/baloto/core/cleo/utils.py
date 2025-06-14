from __future__ import annotations

import math

from dataclasses import dataclass
from difflib import SequenceMatcher
from html.parser import HTMLParser


class TagStripper(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)

        self.reset()
        self.fed: list[str] = []

    def handle_data(self, d: str) -> None:
        self.fed.append(d)

    def handle_entityref(self, name: str) -> None:
        self.fed.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        self.fed.append(f"&#{name};")

    def get_data(self) -> str:
        return "".join(self.fed)


def _strip(value: str) -> str:
    s = TagStripper()
    s.feed(value)
    s.close()

    return s.get_data()


def strip_tags(value: str) -> str:
    while "<" in value and ">" in value:
        new_value = _strip(value)
        if value.count("<") == new_value.count("<"):
            break

        value = new_value

    return value


def find_similar_names(name: str, names: list[str]) -> list[str]:
    """
    Finds names similar to a given command name.
    """
    threshold = 0.4
    distance_by_name = {}
    if " " in name:
        names = [name for name in names if " " in name]
    for actual_name in names:
        distance = SequenceMatcher(None, actual_name, name).ratio()

        is_similar = distance <= len(name) / 3
        substring_index = actual_name.find(name)
        is_substring = substring_index != -1

        if is_similar or is_substring:
            distance_by_name[actual_name] = (
                distance,
                substring_index if is_substring else float("inf"),
            )

    # Only keep results with a distance below the threshold
    distance_by_name = {
        key: value for key, value in distance_by_name.items() if value[0] > threshold
    }
    # Display results with shortest distance first
    return sorted(distance_by_name, key=lambda key: distance_by_name[key])
