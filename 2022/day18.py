from dataclasses import dataclass
from itertools import combinations

from data.day18 import SAMPLE2_TXT, INPUT_TXT, SAMPLE_TXT


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def adjacent(self, other: 'Point') -> bool:
        diff = self - other
        return abs(diff.x) + abs(diff.y) + abs(diff.z) == 1


ADJACENTS = (Point(1, 0, 0), Point(-1, 0, 0), Point(0, 1, 0), Point(0, -1, 0), Point(0, 0, 1), Point(0, 0, -1))


def part1(raw: str) -> int:
    cubes = {Point(*list(int(digit) for digit in line.split(','))) for line in raw.splitlines()}
    return get_unshared_sides(cubes)


def part2(raw: str) -> int:
    cubes = {Point(*(map(int, line.split(',')))) for line in raw.splitlines()}
    all_sides = get_unshared_sides(cubes)
    inside_cubes = flood_fill(cubes)
    return all_sides - get_unshared_sides(inside_cubes)


def get_unshared_sides(cubes: set[Point]) -> int:
    total_sides = len(cubes) * 6
    adjacent_sides = sum(1 for cube1, cube2 in combinations(cubes, 2) if cube1.adjacent(cube2))
    return total_sides - 2 * adjacent_sides


def flood_fill(cubes: set[Point]) -> set[Point]:
    min_z, *_, max_z = sorted(cube.z for cube in cubes)
    min_y, *_, max_y = sorted(cube.y for cube in cubes)
    min_x, *_, max_x = sorted(cube.x for cube in cubes)

    for x in range(min_x, max_x + 1):
        start_node = Point(x, min_y, min_z)
        if start_node not in cubes:
            break
    else:
        raise ValueError

    visited = set()
    queue = [start_node]
    while queue:
        cur_vertex = queue.pop()
        visited.add(cur_vertex)
        for adj in (cur_vertex + vector for vector in ADJACENTS):
            if adj in cubes or adj in visited:
                continue
            if min_x - 1 <= adj.x <= max_x + 1 and min_y - 1 <= adj.y <= max_y + 1 and min_z - 1 <= adj.z <= max_z + 1:
                queue.append(adj)
    all_cubes = {Point(x, y, z)
                 for x in range(min_x, max_x + 1)
                 for y in range(min_y, max_y + 1)
                 for z in range(min_z, max_z + 1)}
    return all_cubes - cubes - visited


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 10
    assert part1(SAMPLE2_TXT) == 64
    print(part1(INPUT_TXT))
    assert part2(SAMPLE2_TXT) == 58
    print(part2(INPUT_TXT))
