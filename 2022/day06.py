from data.day06 import SAMPLE1_TXT, SAMPLE2_TXT, SAMPLE3_TXT, SAMPLE4_TXT, INPUT_TXT
from collections import deque


def part1(txt: str) -> int:
    return find_start(txt, 4)


def part2(txt: str) -> int:
    return find_start(txt, 14)


def find_start(txt: str, message_length: int) -> int:
    buffer = deque(maxlen=message_length)
    for i, char in enumerate(txt, 1):
        buffer.append(char)
        if len(set(buffer)) == message_length:
            return i


##########################
if __name__ == '__main__':
    assert part1(SAMPLE1_TXT) == 5
    assert part1(SAMPLE2_TXT) == 6
    assert part1(SAMPLE3_TXT) == 10
    assert part1(SAMPLE4_TXT) == 11
    print(part1(INPUT_TXT))
    assert part2(SAMPLE1_TXT) == 23
    assert part2(SAMPLE2_TXT) == 23
    assert part2(SAMPLE3_TXT) == 29
    assert part2(SAMPLE4_TXT) == 26
    print(part2(INPUT_TXT))

