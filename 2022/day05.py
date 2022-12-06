from data.day05 import SAMPLE_TXT, INPUT_TXT
import re
from typing import Callable

BoxColumn = list[str]
BoxConfig = list[BoxColumn]
Instructions = list[list[int]]


def part1(txt: str) -> str:
    box_config, instructions = parse_input(txt)
    return get_last_letters(move_boxes(box_config, instructions, box_func=order_boxes_pt1))


def part2(txt: str) -> str:
    box_config, instructions = parse_input(txt)
    return get_last_letters(move_boxes(box_config, instructions, box_func=order_boxes_pt2))


def parse_input(txt: str) -> [BoxConfig, Instructions]:
    box_string, instructions_string = txt.split('\n\n')
    instructions = [parse_instruction(line) for line in instructions_string.split('\n')]
    box_config = parse_boxconfig(box_string)
    return box_config, instructions


def parse_instruction(line: str) -> list[int]:
    instructions = re.match(r'move (\d*) from (\d*) to (\d)', line).groups()
    return [int(line) for line in instructions]


def parse_boxconfig(box_string: str) -> BoxConfig:
    string_as_list = [line for line in box_string.splitlines()][:-1]
    boxes_as_list = list(zip(*string_as_list))[1::4]
    return [remove_empty_and_reverse(list(column)) for column in boxes_as_list]


def get_last_letters(box_config: BoxConfig) -> str:
    return ''.join(column[-1] for column in box_config)


def remove_empty_and_reverse(column: BoxColumn) -> BoxColumn:
    return [val for val in reversed(column) if val != ' ']


def order_boxes_pt1(column: BoxColumn, qty: int) -> [BoxColumn, BoxColumn]:
    boxes = [column.pop() for _ in range(qty)]
    return column, boxes


def order_boxes_pt2(column: BoxColumn, qty: int) -> [BoxColumn, BoxColumn]:
    boxes = [column.pop() for _ in range(qty)]
    return column, boxes[::-1]


def move_boxes(box_config: BoxConfig, instructions: Instructions, box_func: Callable):
    for qty, start, end in instructions:
        column = box_config[start-1]
        new_column, boxes = box_func(column, qty)
        box_config[start-1] = new_column
        box_config[end-1].extend(boxes)
    return box_config


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 'CMZ'
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 'MCD'
    print(part2(INPUT_TXT))
