from data.day02 import SAMPLE_TXT, INPUT_TXT

OutcomeDict = dict[str, tuple[int, int]]

OUTCOMES1: OutcomeDict = {'A X': (1, 3),
                          'B X': (1, 0),
                          'C X': (1, 6),
                          'A Y': (2, 6),
                          'B Y': (2, 3),
                          'C Y': (2, 0),
                          'A Z': (3, 0),
                          'B Z': (3, 6),
                          'C Z': (3, 3)}

OUTCOMES2: OutcomeDict = {'A X': (3, 0),
                          'B X': (1, 0),
                          'C X': (2, 0),
                          'A Y': (1, 3),
                          'B Y': (2, 3),
                          'C Y': (3, 3),
                          'A Z': (2, 6),
                          'B Z': (3, 6),
                          'C Z': (1, 6)}


def either_part(txt: str, outcomes: OutcomeDict):
    return sum(sum(outcomes[pair]) for pair in txt.split('\n'))


def part1(txt: str):
    return either_part(txt, OUTCOMES1)


def part2(txt: str):
    return either_part(txt, OUTCOMES2)


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 15
    assert part2(SAMPLE_TXT) == 12
    print(part1(INPUT_TXT))
    print(part2(INPUT_TXT))
