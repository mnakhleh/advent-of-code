from data.day05 import SAMPLE_TXT, INPUT_TXT
import re
from typing import Callable, Iterator

Stack = list[str]
AllStacks = list[Stack]
Instructions = Iterator[list[int]]


def part1(txt: str) -> str:
    stacks, instructions = parse_input(txt)
    return get_last_letters(move_boxes(stacks, instructions, box_func=order_boxes_pt1))


def part2(txt: str) -> str:
    stacks, instructions = parse_input(txt)
    return get_last_letters(move_boxes(stacks, instructions, box_func=order_boxes_pt2))


def parse_input(txt: str) -> [AllStacks, Instructions]:
    stacks_raw, instructions_raw = txt.split('\n\n')
    return parse_stacks(stacks_raw), parse_instructions(instructions_raw)


def parse_instructions(raw: str) -> Instructions:
    for instruction in re.findall(r'move (\d*) from (\d*) to (\d)', raw):
        yield [int(number) for number in instruction]


def parse_stacks(raw: str) -> AllStacks:
    stacks_as_strings = list(zip(*raw.splitlines()))[1::4]
    return [[val for val in reversed(column) if val != ' '] for column in stacks_as_strings]


def get_last_letters(box_config: AllStacks) -> str:
    return ''.join(column[-1] for column in box_config)


def order_boxes_pt1(column: Stack, qty: int) -> [Stack, Stack]:
    boxes = [column.pop() for _ in range(qty)]
    return column, boxes


def order_boxes_pt2(column: Stack, qty: int) -> [Stack, Stack]:
    boxes = [column.pop() for _ in range(qty)]
    return column, boxes[::-1]


def move_boxes(box_config: AllStacks, instructions: Instructions, box_func: Callable):
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
