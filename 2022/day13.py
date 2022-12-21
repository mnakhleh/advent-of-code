import itertools
import json

from data.day13 import SAMPLE_TXT, INPUT_TXT


def part1(raw: str) -> int:
    return sum(i for i, pair_of_lines in enumerate(raw.split('\n\n'), 1)
               if are_ordered_raw(pair_of_lines.splitlines()))


def part2(raw: str) -> int:
    """Can shorten code (and reduce iterations) significantly by running pair_order() against packets, instead of
    inserting into list then sorting the entire list
    """
    expressions = [json.loads(expression) for expression in raw.replace('\n\n', '\n').splitlines()]
    packet_indices = [sum(1 for expression in expressions if pair_order(expression, divider_packet) == 1)
                      for divider_packet in ([[2]], [[6]])]
    return (packet_indices[0] + 1) * (packet_indices[1] + 2)  # Index starting at 1 + 1st packet offset


def are_ordered_raw(expression_pairs: list[str]) -> bool:
    expressions = map(json.loads, expression_pairs)
    return pair_order(*expressions) in (0, 1)


def pair_order(a: list | int, b: list | int) -> int:
    for char1, char2 in itertools.zip_longest(a, b):
        if char1 is None:
            return 1
        if char2 is None:
            return -1
        match (char1, char2):
            case list(), list():
                order = pair_order(char1, char2)
                if order != 0:
                    return order
            case int(), list():
                order = pair_order([char1], char2)
                if order != 0:
                    return order
            case list(), int():
                order = pair_order(char1, [char2])
                if order != 0:
                    return order
            case int(), int():
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
