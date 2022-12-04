#!/usr/bin/env python3
import sys


def by_elf(input):
    def split_group(b):
        return tuple(int(a) for a in b.split("-"))

    for left_elf, right_elf in (l.rstrip("\n").split(",") for l in input):
        yield split_group(left_elf), split_group(right_elf)


def is_contained(left_elf, right_elf):
    """
    >>> is_contained((0, 0), (1, 1))
    False
    >>> is_contained((0, 2), (1, 1))
    True
    >>> is_contained((1, 1), (0, 2))
    True
    """
    left_from, left_until = left_elf
    right_from, right_until = right_elf

    return (
        left_from <= right_from <= right_until <= left_until
        or right_from <= left_from <= left_until <= right_until
    )


def is_overlapped(left_elf, right_elf):
    """
    >>> is_overlapped((0, 0), (1, 1))
    False
    >>> is_overlapped((0, 1), (1, 1))
    True
    """
    left_from, left_until = left_elf
    right_from, right_until = right_elf

    return max(left_from, right_from) <= min(left_until, right_until)


if __name__ == "__main__":
    contained = 0
    overlap = 0

    for left_elf, right_elf in by_elf(sys.stdin):
        contained += is_contained(left_elf, right_elf)
        overlap += is_overlapped(left_elf, right_elf)

    print(f"contained: {contained}")
    print(f"overlap: {overlap}")
