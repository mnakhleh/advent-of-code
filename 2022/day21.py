import operator
from itertools import cycle

from sympy import Symbol
from sympy.solvers import solve

from data.day21 import SAMPLE_TXT, INPUT_TXT

OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}


def part1(raw: str) -> int:
    monkeys = get_monkeys(raw)
    for monkey_id in cycle(monkeys):
        if isinstance(monkeys[monkey_id], int):
            continue
        v1, v2, op = monkeys[monkey_id]
        if isinstance(monkeys[v1], int) and isinstance(monkeys[v2], int):
            monkeys[monkey_id] = OPERATORS[op](monkeys[v1], monkeys[v2])
            if monkey_id == 'root':
                return monkeys[monkey_id]


def part2(raw: str) -> int:
    monkeys = get_monkeys(raw)
    monkeys['root'][2] = '-'  # solve() requires the equation to be = 0
    equation = "root"
    queue = ['root']
    while queue:
        node = queue.pop(0)
        if node == 'humn':
            continue
        if isinstance(monkeys[node], int):
            equation = equation.replace(node, str(monkeys[node]))
            continue
        v1, v2, op = monkeys[node]
        queue.extend([v1, v2])
        equation = equation.replace(node, f'({v1} {op} {v2})')
    solutions = solve(eval(equation, {}, {'humn': Symbol('humn')}), 'humn')
    return round(solutions[0])


def get_monkeys(raw: str) -> dict:
    monkeys = dict()
    for line in raw.splitlines():
        monkey, expression = line.split(': ')
        for op in OPERATORS:
            if op in expression:
                monkeys[monkey] = expression.split(f' {op} ') + [op]
                break
        else:
            monkeys[monkey] = int(expression)
    return monkeys


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 152
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 301
    print(part2(INPUT_TXT))
