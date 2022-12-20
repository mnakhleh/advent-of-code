import re
from collections import namedtuple
from functools import reduce
from operator import mul

from data.day19 import SAMPLE_TXT, INPUT_TXT

PATTERN = re.compile(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian "
                     r"robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian")

CostSchedule = dict[int, list[int]]
Blueprint = namedtuple('Blueprint', ['id', 'ore_cost', 'clay_cost', 'obsdn_ore_cost', 'obsdn_clay_cost',
                                     'geode_ore_cost', 'geode_obsdn_cost'])

MAX_QUEUE_SIZE = 10_000


def part1(raw: str) -> int:
    blueprints = get_blueprints(raw)
    return sum(bfs(24, costs(blueprint)) * blueprint.id for blueprint in blueprints)


def part2(raw: str) -> int:
    blueprints = get_blueprints(raw)
    return reduce(mul, [bfs(32, costs(blueprint)) for blueprint in blueprints[:3]])


def get_blueprints(raw: str) -> list[Blueprint]:
    return [Blueprint(*map(int, re.split(PATTERN, line)[1:-1])) for line in raw.splitlines()]


def costs(blueprint: Blueprint) -> CostSchedule:
    return {0: [blueprint.ore_cost, 0, 0],
            1: [blueprint.clay_cost, 0, 0],
            2: [blueprint.obsdn_ore_cost, blueprint.obsdn_clay_cost, 0],
            3: [blueprint.geode_ore_cost, 0, blueprint.geode_obsdn_cost]}


def bfs(time_max: int, robot_costs: CostSchedule) -> int:
    max_geodes = 0
    queue = [[0, [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
    depth = 0

    while queue:
        time, robots, old_resources, old_mined = queue.pop(0)

        if time > depth:  # Idea of quality heuristic from /r/Dutchcheesehead
            queue = sorted(queue, key=quality_heuristic, reverse=True)[:MAX_QUEUE_SIZE]
            depth = time

        if time == time_max:
            max_geodes = max(max_geodes, old_mined[3])
            continue

        resources = [old_resources[i] + robots[i] for i in range(4)]
        mined = [old_mined[i] + robots[i] for i in range(4)]

        # If didn't do anything this round
        queue.append([time + 1, robots, resources, mined])

        # Check if can build a robot
        for robot_type in range(4):
            if all([old_resources[res_type] >= robot_costs[robot_type][res_type] for res_type in range(3)]):
                new_resources = [resources[res_type] - robot_costs[robot_type][res_type] for res_type in range(3)]
                new_resources.append(resources[3])  # Geodes not part of cost schedule
                new_robots = robots[:]
                new_robots[robot_type] += 1
                queue.append([time + 1, new_robots, new_resources, mined])
        max_geodes = max(max_geodes, mined[3])

    return max_geodes


def quality_heuristic(state: list[list[int]]) -> int:
    mined = state[-1]
    return 1000 * mined[3] + 100 * mined[2] + 10 * mined[1] + mined[0]


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 33
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 56 * 62
    print(part2(INPUT_TXT))
