from data.day02 import SAMPLE_TXT, INPUT_TXT
from enum import IntEnum


class Rps(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Points(IntEnum):
    LOSE = 0
    DRAW = 3
    WIN = 6


OutcomeDict = dict[str, tuple[int, int]]

# (A, B, C) = RPS, (X, Y, Z) = RPS
OUTCOMES1: OutcomeDict = {'A X': (Rps.ROCK, Points.DRAW),
                          'B X': (Rps.ROCK, Points.LOSE),
                          'C X': (Rps.ROCK, Points.WIN),
                          'A Y': (Rps.PAPER, Points.WIN),
                          'B Y': (Rps.PAPER, Points.DRAW),
                          'C Y': (Rps.PAPER, Points.LOSE),
                          'A Z': (Rps.SCISSORS, Points.LOSE),
                          'B Z': (Rps.SCISSORS, Points.WIN),
                          'C Z': (Rps.SCISSORS, Points.DRAW)}

# (A, B, C) = RPS, (X, Y, Z) = LDW
OUTCOMES2: OutcomeDict = {'A X': (Rps.SCISSORS, Points.LOSE),
                          'B X': (Rps.ROCK, Points.LOSE),
                          'C X': (Rps.PAPER, Points.LOSE),
                          'A Y': (Rps.ROCK, Points.DRAW),
                          'B Y': (Rps.PAPER, Points.DRAW),
                          'C Y': (Rps.SCISSORS, Points.DRAW),
                          'A Z': (Rps.PAPER, Points.WIN),
                          'B Z': (Rps.SCISSORS, Points.WIN),
                          'C Z': (Rps.ROCK, Points.WIN)}


def either_part(txt: str, outcomes: OutcomeDict):
    return sum(sum(outcomes[pair]) for pair in txt.splitlines())


def part1(txt: str):
    return either_part(txt, OUTCOMES1)


def part2(txt: str):
    return either_part(txt, OUTCOMES2)


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 15
    assert part2(SAMPLE_TXT) == 12
    print(part1(INPUT_TXT))
    print(part2(INPUT_TXT))
