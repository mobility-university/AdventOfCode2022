#!/usr/bin/env python3
import sys
from enum import Enum
from functools import reduce


class Shapes(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3

    def winning_against(shape):
        """
        >>> Shapes.winning_against(Shapes.Rock)
        <Shapes.Paper: 2>
        >>> Shapes.winning_against(Shapes.Paper)
        <Shapes.Scissor: 3>
        >>> Shapes.winning_against(Shapes.Scissor)
        <Shapes.Rock: 1>
        """
        if shape == Shapes.Scissor:
            return Shapes.Rock
        if shape == Shapes.Paper:
            return Shapes.Scissor
        if shape == Shapes.Rock:
            return Shapes.Paper
        assert False

    def loosing_against(shape):
        """
        >>> Shapes.loosing_against(Shapes.Rock)
        <Shapes.Scissor: 3>
        >>> Shapes.loosing_against(Shapes.Paper)
        <Shapes.Rock: 1>
        >>> Shapes.loosing_against(Shapes.Scissor)
        <Shapes.Paper: 2>
        """
        return Shapes.winning_against(Shapes.winning_against(shape))

    def score(shape):
        return shape.value

    def from_own_move(value):
        return dict(X=Shapes.Rock, Y=Shapes.Paper, Z=Shapes.Scissor)[value]

    def from_enemy_move(value):
        return dict(A=Shapes.Rock, B=Shapes.Paper, C=Shapes.Scissor)[value]


def play(moves):
    """
    >>> play([[Shapes.Rock, Shapes.Paper]])[0]
    8
    >>> play([[Shapes.Rock, Shapes.Paper], [Shapes.Rock, Shapes.Paper]])[0]
    16
    """
    original_score = 0
    score_optimized_strategy = 0

    for enemy_move, my_move in moves:
        a, b = play_single_game(enemy_move, my_move)

        original_score += a
        score_optimized_strategy += b

    return original_score, score_optimized_strategy


def play_single_game(enemy_move, my_move):
    """
    >>> play_single_game(Shapes.Rock, Shapes.Paper)[0]
    8
    >>> play_single_game(Shapes.Paper, Shapes.Rock)[0]
    1
    >>> play_single_game(Shapes.Scissor, Shapes.Scissor)[0]
    6
    >>> play_single_game(Shapes.Rock, Shapes.Rock)[1]
    3
    >>> play_single_game(Shapes.Rock, Shapes.Paper)[1]
    4
    >>> play_single_game(Shapes.Rock, Shapes.Scissor)[1]
    8
    """
    original_score = round_score(enemy_move, my_move) + Shapes.score(my_move)

    optimized_move = {
        Shapes.Rock: Shapes.loosing_against(enemy_move),
        Shapes.Paper: enemy_move,
        Shapes.Scissor: Shapes.winning_against(enemy_move),
    }[my_move]

    optimized_strategy_score = round_score(enemy_move, optimized_move) + Shapes.score(
        optimized_move
    )

    return original_score, optimized_strategy_score


def round_score(enemy, own):
    if enemy == own:
        return 3
    if Shapes.loosing_against(enemy) == own:
        return 0

    assert Shapes.winning_against(enemy) == own
    return 6


def by_moves(input):
    """
    >>> list(by_moves(["A X"]))
    [(<Shapes.Rock: 1>, <Shapes.Rock: 1>)]
    >>> list(by_moves(["C Y"]))
    [(<Shapes.Scissor: 3>, <Shapes.Paper: 2>)]
    >>> list(by_moves(["A Y", "B Z", "C X"]))
    [(<Shapes.Rock: 1>, <Shapes.Paper: 2>), (<Shapes.Paper: 2>, <Shapes.Scissor: 3>), (<Shapes.Scissor: 3>, <Shapes.Rock: 1>)]
    """
    for line in input:
        enemy_shape, own_shape = line.rstrip("\n").split()

        yield (Shapes.from_enemy_move(enemy_shape), Shapes.from_own_move(own_shape))


if __name__ == "__main__":
    original_score, score_optimized_strategy = play(by_moves(sys.stdin))

    print(f"score: {original_score}")
    print(f"score with optimized strategy: {score_optimized_strategy}")
