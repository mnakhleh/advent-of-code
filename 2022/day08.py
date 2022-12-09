import operator
from functools import reduce
from itertools import product
from typing import Iterable

from data.day08 import SAMPLE_TXT, INPUT_TXT

Coordinates = tuple[int, int]
HeightView = list[int]
HeightMap = list[HeightView]


def part1(height_map_raw: str) -> int:
    height_map = get_heightmap(height_map_raw)
    return sum(is_visible(pairs, height_map) for pairs in get_all_cells(height_map))


def part2(height_map_raw: str) -> int:
    height_map = get_heightmap(height_map_raw)
    return max(get_score(pairs, height_map) for pairs in get_all_cells(height_map))


def get_heightmap(height_map_raw: str) -> HeightMap:
    return [[int(char) for char in line] for line in height_map_raw.splitlines()]


def get_all_cells(height_map: HeightMap) -> Iterable[Coordinates]:
    return product(range(len(height_map)), range(len(height_map)))


def is_visible(coordinates: Coordinates, height_map: HeightMap) -> bool:
    row, col = coordinates
    height = height_map[row][col]
    return any(height > max(trees) if trees else True for trees in get_view_heights(coordinates, height_map))


def get_view_heights(coordinates: Coordinates, height_map: HeightMap) -> Iterable[HeightView]:
    size = len(height_map)
    row, col = coordinates
    yield [height_map[row - i - 1][col] for i in range(row)]  # UP
    yield [height_map[row + i + 1][col] for i in range(size - row - 1)]  # DOWN
    yield [height_map[row][col - i - 1] for i in range(col)]  # LEFT
    yield [height_map[row][col + i + 1] for i in range(size - col - 1)]  # RIGHT


def line_of_sight(start_height: int, tree_view: HeightView) -> int:
    nb_trees = 0
    for tree_height in tree_view:
        nb_trees += 1
        if tree_height >= start_height:
            break
    return nb_trees


def get_score(coordinates: Coordinates, height_map: HeightMap):
    row, col = coordinates
    height = height_map[row][col]
    return reduce(operator.mul, [line_of_sight(height, tree_view)
                                 for tree_view in get_view_heights(coordinates, height_map)])


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 21
    print(part1(INPUT_TXT))
    assert get_score((1, 2), get_heightmap(SAMPLE_TXT)) == 4
    assert get_score((3, 2), get_heightmap(SAMPLE_TXT)) == 8
    assert part2(SAMPLE_TXT) == 8
    print(part2(INPUT_TXT))