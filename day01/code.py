#!/usr/bin/env python3
import sys
from itertools import takewhile
from functools import reduce


def max_sum(input):
    """
    >>> max_sum([(1,)])
    (1,)
    >>> max_sum([(1,), (2,)])
    2
    >>> max_sum([(1,), (2,), (3,)])
    3
    >>> max_sum([(1,), (2,), (1,)])
    2
    >>> max_sum([(1,), (2, 2), (1,)])
    4
    """
    return reduce(
        lambda a, b: max(sum(a) if isinstance(a, tuple) else a, sum(b)),
        input,
    )


def three_highest_sums(input):
    """
    >>> three_highest_sums([(1,)])
    (1,)
    >>> three_highest_sums([(1,), (2,)])
    [1, 2]
    >>> three_highest_sums([(1,), (2,), (3,)])
    [1, 2, 3]
    >>> three_highest_sums([(1,), (2,), (1,)])
    [1, 1, 2]
    >>> three_highest_sums([(1,), (2, 2), (1,)])
    [1, 1, 4]
    >>> three_highest_sums([(1,), (2, 2), (1,), (5,)])
    [1, 4, 5]
    """
    return reduce(
        lambda a, b: sorted(([sum(a)] if isinstance(a, tuple) else a) + [sum(b)])[-3:],
        input,
    )


def parse(input):
    r"""
    >>> list(parse(("123\n", "456\n")))
    [123, 456]
    >>> list(parse(("123\n", "\n", "456\n")))
    [123, None, 456]
    """
    for line in input:
        line = line.rstrip("\n")
        if line == "":
            yield None
            continue
        yield int(line)


def splitter(input):
    """
    >>> list(splitter((a for a in [1, None])))
    [(1,)]
    >>> list(splitter((a for a in [1, None, 2, 3])))
    [(1,), (2, 3)]
    >>> list(splitter((a for a in [1, None, 2, None])))
    [(1,), (2,)]
    """
    while group := tuple(takewhile(lambda v: v, input)):
        yield group


if __name__ == "__main__":
    fat_elves = three_highest_sums(splitter(parse(sys.stdin)))

    print(f'three elves with most calories: {", ".join(str(b) for b in fat_elves)}')
    print(f"calories they carry: {sum(fat_elves)}")
    print(f"elf with most calories: {fat_elves[-1]}")
