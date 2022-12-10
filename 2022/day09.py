from dataclasses import dataclass

from data.day09 import SAMPLE_TXT, SAMPLE2_TXT, INPUT_TXT


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, delta: 'Point') -> 'Point':
        return Point(self.x + delta.x, self.y + delta.y)

    def __sub__(self, delta: 'Point') -> 'Point':
        return Point(self.x - delta.x, self.y - delta.y)


MOVE_VECTORS = {'R': Point(1, 0), 'L': Point(-1, 0), 'U': Point(0, 1), 'D': Point(0, -1)}


class Snake:
    def __init__(self, nb_knots: int):
        self.knots = [Point(0, 0)] * nb_knots
        self.visited = set()

    def move(self, orient: str):
        self.knots[0] += MOVE_VECTORS[orient]
        for i in range(1, len(self.knots)):
            self.knots[i] = self.move_tail(self.knots[i - 1], self.knots[i])
        self.visited.add((self.knots[-1].x, self.knots[-1].y))

    @staticmethod
    def move_tail(head: Point, tail: Point) -> Point:
        dx = head.x - tail.x
        dy = head.y - tail.y
        if dx ** 2 + dy ** 2 < 4:  # Tail is less than 1 unit away
            return tail
        if dx ** 2 + dy ** 2 == 4:  # Horizontal / Vertical
            return head - Point(dx // 2, dy // 2)
        if abs(dy) == 2 and abs(dx) == 1:
            return head - Point(0, dy // 2)
        if abs(dx) == 2 and abs(dy) == 1:
            return head - Point(dx // 2, 0)
        # All steps bigger than that, just diagonal 1
        return head - Point(1 if dx > 0 else -1, 1 if dy > 0 else -1)


def part1(raw: str) -> int:
    instructions = [line.split() for line in raw.splitlines()]
    return run_snake(Snake(2), instructions)


def part2(raw: str) -> int:
    instructions = [line.split() for line in raw.splitlines()]
    return run_snake(Snake(10), instructions)


def run_snake(snake: Snake, instructions: list[list[str]]) -> int:
    for orient, distance in instructions:
        for _ in range(int(distance)):
            snake.move(orient)
    return len(snake.visited)


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 13
    assert part1(INPUT_TXT) == 6090
    assert part2(SAMPLE_TXT) == 1
    assert part2(SAMPLE2_TXT) == 36
    print(part2(INPUT_TXT))
