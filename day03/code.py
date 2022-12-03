#!/usr/bin/env python3
import sys
from itertools import islice


def points(item):
    """
    >>> points("p")
    16
    >>> points("L")
    38
    >>> points("v")
    22
    >>> points("t")
    20
    >>> points("s")
    19
    """
    if "a" <= item <= "z":
        return ord(item) - ord("a") + 1
    assert "A" <= item <= "Z"
    return ord(item) - ord("A") + 27


def batched(iterable, n):
    """
    >>> for batch in batched((a for a in "abcdef"), 3):
    ...     print(batch)
    ...
    ('a', 'b', 'c')
    ('d', 'e', 'f')
    """
    assert n >= 1, "n must be at least one"
    while batch := tuple(islice(iterable, n)):
        yield batch


def get_badge(rucksack):
    """
    >>> get_badge("aa")
    'a'
    >>> get_badge("abca")
    'a'
    """
    left = set(rucksack[: len(rucksack) // 2])
    right = set(rucksack[len(rucksack) // 2 :])
    badges = set(left) & set(right)
    (badge,) = badges

    return badge


def by_last_three_rucksacks(input):
    yield from batched((l.rstrip("\n") for l in input), 3)


if __name__ == "__main__":
    score = 0
    three_score = 0

    for complete_elf_group in by_last_three_rucksacks(sys.stdin):

        group_badges = set.intersection(
            *(set(rucksack) for rucksack in complete_elf_group)
        )
        (group_badge,) = group_badges
        three_score += points(group_badge)

        for rucksack in complete_elf_group:
            score += points(get_badge(rucksack))

    print(f"sum of priorities for the elves: {score}")
    print(f"sum for the priorities of the three-elves-group: {three_score}")
