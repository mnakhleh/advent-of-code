from copy import deepcopy
from dataclasses import dataclass, field
from math import lcm
from typing import Callable, Optional
from typing import Iterator

from data.day11 import ITEMS_SAMPLE, ITEMS_INPUT


@dataclass
class Monkey:
    operation_func: Callable
    test_func: Callable
    number_inspections: int = field(init=False, default=0)
    modulo: int

    def inspect(self, item: int, divisor: Optional[int]) -> [int, int]:
        self.number_inspections += 1
        item = self.operation_func(item)
        if divisor:
            item %= divisor
        else:
            item = item // 3
        return item, self.test_func(item)


MONKEYS_SAMPLE = [Monkey(lambda old: old * 19, lambda item: 2 if item % 23 == 0 else 3, 23),
                  Monkey(lambda old: old + 6, lambda item: 2 if item % 19 == 0 else 0, 19),
                  Monkey(lambda old: old * old, lambda item: 1 if item % 13 == 0 else 3, 13),
                  Monkey(lambda old: old + 3, lambda item: 0 if item % 17 == 0 else 1, 17)]


MONKEYS_INPUT = [Monkey(lambda old: old * 11, lambda item: 7 if item % 2 == 0 else 4, 2),
                 Monkey(lambda old: old + 1, lambda item: 3 if item % 13 == 0 else 6, 13),
                 Monkey(lambda old: old + 6, lambda item: 1 if item % 3 == 0 else 6, 3),
                 Monkey(lambda old: old * old, lambda item: 7 if item % 17 == 0 else 0, 17),
                 Monkey(lambda old: old * 7, lambda item: 5 if item % 19 == 0 else 2, 19),
                 Monkey(lambda old: old + 8, lambda item: 2 if item % 7 == 0 else 1, 7),
                 Monkey(lambda old: old + 5, lambda item: 3 if item % 11 == 0 else 0, 11),
                 Monkey(lambda old: old + 7, lambda item: 4 if item % 5 == 0 else 5, 5)]


def part1(monkeys: list[Monkey], items: list[list[int]]) -> int:
    return get_monkeying(deepcopy(monkeys), items)


def part2(monkeys: list[Monkey], items: list[list[int]]) -> int:
    return get_monkeying(deepcopy(monkeys), items, round_max=10_000)


def get_item_and_monkey_id(items: list[list[int]]) -> Iterator[tuple[int, int]]:
    for i, item_list in enumerate(items):
        for item in item_list:
            yield item, i


def get_monkeying(monkeys: list[Monkey], items: list[list[int]], round_max=20):
    is_long_game = round_max > 20
    # 100% peaked at the Solutions thread to figure out the lcm
    divisor = lcm(*[monkey.modulo for monkey in monkeys]) if is_long_game else 0

    # Iterate through items instead of monkeys; round++ once you go down in Monkey num (ex. 1,3 | 2,4,5 | 2)
    for item, starting_id in get_item_and_monkey_id(items):
        round_nb = 0
        while round_nb < round_max:
            item, monkey_id = monkeys[starting_id].inspect(item, divisor)
            if monkey_id <= starting_id:
                round_nb += 1
            starting_id = monkey_id

    sorted_inspection_qties = sorted(monkey.number_inspections for monkey in monkeys)
    return sorted_inspection_qties[-1] * sorted_inspection_qties[-2]


##########################
if __name__ == '__main__':
    assert part1(MONKEYS_SAMPLE, ITEMS_SAMPLE) == 10605
    print(part1(MONKEYS_INPUT, ITEMS_INPUT))
    assert part2(MONKEYS_SAMPLE, ITEMS_SAMPLE) == 2713310158
    print(part2(MONKEYS_INPUT, ITEMS_INPUT))
