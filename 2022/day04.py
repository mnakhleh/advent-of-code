from data.day04 import SAMPLE_TXT, INPUT_TXT
from typing import Iterable


ElfRange = set[int]


def part1(txt: str) -> int:
    return sum(1 for elf1, elf2 in get_elf_sets(txt)
               if elf1.issubset(elf2) or elf2.issubset(elf1))


def part2(txt: str) -> int:
    return sum(1 for elf1, elf2 in get_elf_sets(txt)
               if elf1 & elf2)


def get_elf_sets(txt: str) -> Iterable[list[ElfRange]]:
    for line in txt.split('\n'):
        yield [range_set(elf) for elf in line.split(',')]


def range_set(range_as_text: str) -> ElfRange:
    lower, upper = map(int, range_as_text.split('-'))
    return set(range(lower, upper + 1))


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 2
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 4
    print(part2(INPUT_TXT))
