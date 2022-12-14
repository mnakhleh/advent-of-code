from dataclasses import dataclass
from typing import Iterable

from data.day14 import SAMPLE_TXT, INPUT_TXT


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))


Formation = dict[Point, bool]


def part1(raw: str) -> int:
    rock_formation = get_rock_formation(raw)
    return simulate_sand(rock_formation)


def part2(raw: str) -> int:
    rock_formation = get_rock_formation(raw)
    return simulate_sand(add_bottom(rock_formation)) + 1  # Add 1 because 1 unit too high, can't be bothered to fix it


def get_rock_formation(raw: str) -> Formation:
    formation = dict()
    for coords in get_point_lists(raw):
        start = coords.pop(0)
        for prox in coords:
            range_x = range(start.x, prox.x + 1) if start.x < prox.x else range(prox.x, start.x + 1)
            range_y = range(start.y, prox.y + 1) if start.y < prox.y else range(prox.y, start.y + 1)
            formation.update({Point(x, y): True for x in range_x for y in range_y})
            start = prox
    return formation


def add_bottom(formation: Formation) -> Formation:
    bottom = max(point.y for point in formation)
    left = min(point.x for point in formation)
    right = max(point.x for point in formation)
    return {**formation, **{Point(x, bottom + 2): True for x in range(left - bottom, right + bottom + 1)}}


def simulate_sand(formation: Formation) -> int:
    turns = 0
    while True:
        new_formation = simulate_turn(formation)
        if new_formation == formation or Point(500, 0) in new_formation:
            return turns
        formation = new_formation
        turns += 1


def simulate_turn(formation: Formation) -> Formation:
    bottom = max(point.y for point in formation)
    sand = Point(500, 0)
    formation = dict(formation)
    while True:
        if (sand + Point(0, 1)).y > bottom:
            return formation
        if sand + Point(0, 1) not in formation:
            sand += Point(0, 1)
            continue

        for vector in (Point(-1, 1), Point(1, 1)):
            if sand + vector not in formation:
                sand += vector
                break
        else:
            formation[sand] = False
            return formation


def get_point_lists(raw: str) -> Iterable[list[Point]]:
    for ptrn in raw.splitlines():
        yield [Point(*map(int, coords.split(','))) for coords in ptrn.split(' -> ')]


def draw(formation: Formation):
    """For debugging"""
    bottom = max(point.y for point in formation)
    left = min(point.x for point in formation)
    right = max(point.x for point in formation)
    matrix = [['.' for _ in range(right - left + 1)] for _ in range(bottom)]
    for point in formation:
        matrix[point.y - 1][point.x - left] = '#' if formation[point] else 'o'
    print('\n'.join(''.join(row) for row in matrix) + '\n')


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 24
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 93
    print(part2(INPUT_TXT))
