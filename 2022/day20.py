from collections import deque

from data.day20 import SAMPLE_TXT, INPUT_TXT

KEY = 811589153


def part1(raw: str) -> int:
    return solve(raw, key=1, iterations=1)


def part2(raw: str) -> int:
    return solve(raw, key=KEY, iterations=10)


def solve(raw: str, key: int = 1, iterations: int = 1) -> int:
    numbers = [int(x) * key for x in raw.splitlines()]
    number_queue = deque((x, i) for i, x in enumerate(numbers))  # Got idea for deques from /r/ri7chy!
    start_queue = number_queue.copy()
    for _ in range(iterations):
        for nb, i in start_queue:
            number_queue = move(number_queue, nb, i)
    return get_coords([x for x, i in number_queue])


def move(number_queue: deque[tuple[int, int]], x: int, i: int) -> deque[tuple[int, int]]:
    current_idx = number_queue.index((x, i))
    number_queue.rotate(-current_idx)
    number_queue.popleft()
    number_queue.rotate(-x)
    number_queue.appendleft((x, i))
    return number_queue  # Don't need to rotate back to location since the coord func only takes relative positions


def get_coords(numbers: list[int]) -> int:
    start = numbers.index(0)
    return sum([numbers[(start + i) % len(numbers)] for i in (1000, 2000, 3000)])


##########################
if __name__ == '__main__':
    assert get_coords([1, 2, -3, 4, 0, 3, -2]) == 3
    assert part1(SAMPLE_TXT) == 3
    print(part1(INPUT_TXT))
    print(part2(INPUT_TXT))
