from data.day03 import SAMPLE_TXT, INPUT_TXT
from string import ascii_letters


def part1(txt: str) -> int:
    overlaps = [get_common_items(line).pop() for line in txt.splitlines()]
    return calculate_total_value(overlaps)


def part2(txt: str) -> int:
    overlaps = [set.intersection(*elf_group).pop() for elf_group in get_threebies(txt.splitlines())]
    return calculate_total_value(overlaps)


def get_common_items(content: str) -> set[str]:
    half1, half2 = content[:len(content)//2], content[len(content)//2:]
    overlaps = set(half1) & set(half2)
    return overlaps


def get_threebies(lines: list[str]) -> list[set[str]]:
    for elves in zip(lines[::3], lines[1::3], lines[2::3]):
        yield [set(elf) for elf in elves]


def calculate_total_value(overlaps: list[str]) -> int:
    return sum(1 + ascii_letters.index(overlap) for overlap in overlaps) # Neat Trick from Joel Grus + LiquidFun


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 157
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 70
    print(part2(INPUT_TXT))
