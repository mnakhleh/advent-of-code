import re
from itertools import permutations

from dijkstar import Graph, find_path

from data.day16 import SAMPLE_TXT, INPUT_TXT


Rates = dict[str, int]
Paths = dict[tuple[str, str], list[str]]


def part1(raw: str, time: int = 30) -> int:
    # Grateful to /u/culp for the idea of DFS + time limit to constrain the solution space + some implementation
    flow_rates, graph, subpaths = parse_input(raw)
    return max(score(paths, time, flow_rates, subpaths) for paths in dfs(30, flow_rates, subpaths))


def part2(raw: str, time: int = 26) -> int:
    flow_rates, graph, subpaths = parse_input(raw)
    max_score = 0
    for pth_1, pth_2 in permutations(dfs(time, flow_rates, subpaths), 2):
        if not set(pth_1).isdisjoint(set(pth_2)):
            continue

        # Really like this way of getting max score, as it's readable + only have calculated once, + don't need storage
        max_score = max(max_score, score(pth_1, time, flow_rates, subpaths) + score(pth_2, 26, flow_rates, subpaths))
    return max_score


def parse_input(raw: str) -> tuple[Rates, Graph, Paths]:
    flow_rates = {}
    graph = Graph()
    for line in raw.splitlines():
        valve, rate, tunnel_valves = re.split(r"Valve (\w+) .*?rate=(\d+); .*?valves? (.*)", line)[1:4]
        flow_rates[valve] = int(rate)
        for neighbour in tunnel_valves.split(', '):
            graph.add_edge(valve, neighbour, 1)
    subpaths = {valve_pair: find_path(graph, *valve_pair).nodes for valve_pair in permutations(flow_rates, 2)}
    return flow_rates, graph, subpaths


def dfs(time: int, rates: Rates, subpaths: Paths) -> list[list[str]]:
    paths = []

    def _dfs(v: str, t: int, visited: list[str]):
        if t <= 0:
            return
        for (cur_valve, next_valve), nodes in subpaths.items():
            if cur_valve != v:
                continue
            if not rates[next_valve] or next_valve in visited:
                continue
            if t - len(nodes) <= 0:
                continue
            # Heuristic. Cut things off if you're 5 deep and under average (which is ~16)
            if len(visited) == 5 and sum(rates[v] for v in visited) < 75:
                continue
            _dfs(next_valve, t - len(nodes), visited + [next_valve])
        paths.append(visited)

    _dfs('AA', time, [])
    return paths


def score(path: list[str], time: int, rates: Rates, distances: Paths) -> int:
    scoring = 0
    for valve, next_valve in zip(["AA"] + path, path):
        time -= len(distances[valve, next_valve])
        scoring += time * rates[next_valve]
    return scoring


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT) == 1651
    print(part1(INPUT_TXT))
    assert part2(SAMPLE_TXT) == 1707
    print(part2(INPUT_TXT))
