from contextlib import suppress
from typing import Iterator

from dijkstar import Graph, find_path  # Life is too short.
from dijkstar.algorithm import NoPathError

from data.day12 import SAMPLE_TXT, INPUT_TXT


def part1(maze_raw: str) -> int:
    start = maze_raw.replace('\n', '').find('S')
    end = maze_raw.replace('\n', '').find('E')
    graph = get_graph(maze_raw)
    return find_path(graph, start, end).total_cost


def part2(maze_raw: str) -> int:
    start_s = maze_raw.replace('\n', '').find('S')
    end = maze_raw.replace('\n', '').find('E')

    all_starts = [start_s] + [i for i, char in enumerate(maze_raw.replace('\n', '')) if char == 'a']
    graph = get_graph(maze_raw)

    distances = []  # Can't use a list comprehension due to NoPathErrors
    for start in all_starts:
        with suppress(NoPathError):
            distances.append(find_path(graph, start, end).total_cost)
    return min(distances)


def get_graph(maze_raw: str) -> Graph:
    graph = Graph()
    for edge, neighbour in get_edges(maze_raw.splitlines()):
        graph.add_edge(edge, neighbour, 1)
    return graph


def get_edges(maze: list[str]) -> Iterator[tuple[int, int]]:
    maze_string = ''.join(maze)
    for idx in range(len(maze_string)):
        char = maze_string[idx]
        for idx_adjacent in get_adjacent_indices(idx, maze):
            char_adjacent = maze_string[idx_adjacent]
            char, char_adjacent = (char + char_adjacent).replace('S', 'a').replace('E', 'z')
            if ord(char_adjacent) <= ord(char) + 1:
                yield idx, idx_adjacent


def get_adjacent_indices(idx: int, maze: list[str]) -> Iterator[int]:
    if idx % len(maze[0]) != 0:
        yield idx - 1
    if idx % len(maze[0]) != len(maze[0]) - 1:
        yield idx + 1
    if idx >= len(maze[0]):
        yield idx - len(maze[0])
    if idx < len(maze[0]) * (len(maze) - 1):
        yield idx + len(maze[0])


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 31
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 29
    print(part2(INPUT_TXT))
