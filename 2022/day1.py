"""timeit results x 10,000:
 part1_forloop: 6.9981181
 part1_max: 7.0776999
 part1_sorted: 7.1604861
 part2_heap: 7.1573843
 part2_sorted: 7.164593200000002
"""
import heapq

from data.day1 import SAMPLE_TXT, INPUT_TXT


def part1_forloop(txt: str) -> int:
    max_calories = 0
    for elf_calories in txt.split('\n\n'):
        elf_calories = calories_from_string(elf_calories)
        if elf_calories > max_calories:
            max_calories = elf_calories
    return max_calories


def part1_max(txt: str) -> int:
    all_elf_calories = [calories_from_string(elf_calories) for elf_calories in txt.split('\n\n')]
    return max(all_elf_calories)


def part2_heap(txt: str) -> int:
    all_elf_calories = [calories_from_string(elf_calories) for elf_calories in txt.split('\n\n')]
    top_3_calories = heapq.nlargest(3, all_elf_calories)
    return sum(top_3_calories)


def get_sorted_calories(txt: str) -> list[int]:
    all_elf_calories = [calories_from_string(elf_calories) for elf_calories in txt.split('\n\n')]
    return sorted(all_elf_calories, reverse=True)


def calories_from_string(elf_calories: str) -> int:
    return sum(int(number) for number in elf_calories.split('\n'))


def part1_sorted(txt: str) -> int:
    return get_sorted_calories(txt)[0]


def part2_sorted(txt: str) -> int:
    return sum(get_sorted_calories(txt)[:3])


##########################
if __name__ == '__main__':
    assert part1_forloop(SAMPLE_TXT) == 24000
    assert part1_max(SAMPLE_TXT) == 24000
    assert part1_sorted(SAMPLE_TXT) == 24000
    assert part2_heap(SAMPLE_TXT) == 45000
    assert part2_sorted(SAMPLE_TXT) == 45000
    print(part1_max(INPUT_TXT))
    print(part2_sorted(INPUT_TXT))
