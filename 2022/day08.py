from typing import Iterable

from data.day08 import SAMPLE_TXT, INPUT_TXT
from itertools import permutations

TreeLocation = tuple[int, int]
HeightMap = list[list[int]]


def part1(height_map_raw: str) -> int:
    height_map = get_heightmap(height_map_raw)
    vals = set(get_left(height_map) + get_right(height_map) + get_down(height_map) + get_up(height_map))
    return len(vals)


def part2(height_map_raw: str) -> int:
    height_map = get_heightmap(height_map_raw)
    return max(get_score(height_map, *coords) for coords in permutations(range(len(height_map)), 2))


def get_trees(height_map: Iterable[Iterable[int]]) -> list[TreeLocation]:
    trees = []
    for row, line in enumerate(height_map):
        tallest = -1
        for col, height in enumerate(line):
            if height > tallest:
                tallest = height
                trees.append((row, col))
    return trees


def get_left(height_map: HeightMap) -> list[TreeLocation]:
    return get_trees(height_map)


def get_right(height_map: HeightMap) -> list[TreeLocation]:
    txt_transformed = map(reversed, height_map)
    trees_transformed = get_trees(txt_transformed)

    width = len(height_map[0])
    trees = [(row, width - col - 1) for row, col in trees_transformed]
    return trees


def get_up(height_map: HeightMap) -> list[TreeLocation]:
    txt_transformed = map(reversed, zip(*height_map))
    trees_transformed = get_trees(txt_transformed)

    width = len(height_map[0])
    trees = [(width - col - 1, row) for row, col in trees_transformed]
    return trees


def get_down(height_map: HeightMap) -> list[TreeLocation]:
    txt_transformed = zip(*height_map)
    trees_transformed = get_trees(txt_transformed)
    trees = [(col, row) for row, col in trees_transformed]
    return trees


def get_score(height_map: HeightMap, row: int, col: int) -> int:
    current_height = height_map[row][col]
    score = 1
    score_by_orientation = 0
    height, width = len(height_map), len(height_map[0])
    for i in range(row):  # UP
        row_check = row - i - 1
        score_by_orientation += 1
        if height_map[row_check][col] >= current_height:
            break
    score *= score_by_orientation
    score_by_orientation = 0
    for i in range(height - row - 1):  # DOWN
        row_check = row + i + 1
        score_by_orientation += 1
        if height_map[row_check][col] >= current_height:
            break
    score *= score_by_orientation
    score_by_orientation = 0
    for i in range(col):  # LEFT
        col_check = col - i - 1
        score_by_orientation += 1
        if height_map[row][col_check] >= current_height:
            break
    score *= score_by_orientation
    score_by_orientation = 0
    for i in range(width - col - 1):  # RIGHT
        col_check = col + i + 1
        score_by_orientation += 1
        if height_map[row][col_check] >= current_height:
            break
    score *= score_by_orientation
    return score


def get_heightmap(height_map_raw: str) -> HeightMap:
    return [[int(char) for char in line] for line in height_map_raw.splitlines()]


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 21
    print(part1(INPUT_TXT))
    assert get_score(get_heightmap(SAMPLE_TXT), 1, 2) == 4
    assert get_score(get_heightmap(SAMPLE_TXT), 3, 2) == 8
    assert part2(SAMPLE_TXT) == 8
    print(part2(INPUT_TXT))


