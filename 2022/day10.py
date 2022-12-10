from data.day10 import SAMPLE_TXT, INPUT_TXT
from typing import Iterable


def part1(raw: str) -> int:
    return sum(get_power(raw, cycle)*cycle for cycle in range(20, 221, 40))


def part2(raw: str) -> Iterable[str]:
    screen = ''
    i = 1
    while True:
        power = get_power(raw, i)
        try:
            screen += '█' if len(screen) % 40 in (power-1, power, power+1) else '.'
        except TypeError:
            break

        if i % 40 == 0:
            yield screen
            screen = ''
        i += 1


def get_power(raw: str, cycle_stop_count: int) -> int:
    sums = [1]
    cycle = 1
    for line in raw.splitlines():
        if line.startswith('addx'):
            sums.append(int(line.split()[1]))
            cycle += 2
        else:
            cycle += 1

        if cycle == cycle_stop_count:
            return sum(sums)
        if cycle > cycle_stop_count:
            return sum(sums[:-1])


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 13140
    print(part1(INPUT_TXT))
    print('\n'.join(part2(SAMPLE_TXT)))
    print('\n\n')
    print('\n'.join(part2(INPUT_TXT)))

