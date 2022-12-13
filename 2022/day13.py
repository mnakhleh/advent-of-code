import functools
import itertools
import json
from typing import Union

from data.day13 import SAMPLE_TXT, INPUT_TXT


def part1(raw: str) -> int:
    return sum(i for i, pair_of_lines in enumerate(raw.split('\n\n'), 1)
               if are_ordered_raw(pair_of_lines.splitlines()) == 1)


def part2(raw: str) -> int:
    divider_packets = [[[2]], [[6]]]
    expressions = [json.loads(expression) for expression in raw.replace('\n\n', '\n').splitlines()]
    expressions.extend(divider_packets)
    expressions.sort(key=functools.cmp_to_key(are_ordered), reverse=True)
    expressions.insert(0, 0)  # To get indices to start at 1 and not 0
    return expressions.index(divider_packets[0]) * expressions.index(divider_packets[1])


def are_ordered_raw(expression_pairs: list[str]) -> int:
    expressions = map(json.loads, expression_pairs)
    return are_ordered(*expressions)


def are_ordered(a: Union[list, int], b: Union[list, int]) -> int:
    for char1, char2 in itertools.zip_longest(a, b):
        if char1 is None:
            return 1
        elif char2 is None:
            return -1
        elif (type(char1), type(char2)) == (list, list):
            order = are_ordered(char1, char2)
            if order != 0:
                return order
        elif (type(char1), type(char2)) == (int, list):
            order = are_ordered([char1], char2)
            if order != 0:
                return order
        elif (type(char1), type(char2)) == (list, int):
            order = are_ordered(char1, [char2])
            if order != 0:
                return order
        elif (type(char1), type(char2)) == (int, int):
            if char1 < char2:
                return 1
            if char1 > char2:
                return -1
    return 0


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 13
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 140
    print(part2(INPUT_TXT))
