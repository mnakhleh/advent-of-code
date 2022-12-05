from itertools import chain
from collections import Counter

TEST = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

TEST2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

TEST3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

INPUT = """QR-da
QR-end
QR-al
start-op
zh-iw
zh-start
da-PF
op-bj
iw-QR
end-HR
bj-PF
da-LY
op-PF
bj-iw
end-da
bj-zh
HR-iw
zh-op
zh-PF
HR-bj
start-PF
HR-da
QR-bj"""


def get_graph(text):
    nodes = dict()
    for line in text.split('\n'):
        a, b = line.split('-')
        for n in a, b:
            if n not in nodes:
                nodes[n] = []

        nodes[a].append(b)
        if a != 'start' and b != 'end':
            nodes[b].append(a)
    return nodes


class Graph:
    """Adapted from https://www.geeksforgeeks.org/find-paths-given-source-destination/"""
    def __init__(self, graph, visit_twice=False):
        self.vertices = self.get_vertices(graph)
        self.V = len(self.vertices)
        self.graph = graph
        self.good_paths = []
        self.can_visit_twice = visit_twice
        # self.twice_small_cave = ''

    @staticmethod
    def get_vertices(graph):
        vertices = set(graph)
        for end_node in chain.from_iterable(graph.values()):
            vertices.add(end_node)
        return vertices

    def all_paths_recurs(self, cur, end, path):
        """A recursive function to print all paths from 'u' to 'd'
        visited[] keeps track of vertices in current path.
        path[] stores actual vertices and path_index is current index in path[]
        """
        path.append(cur)

        if cur == end:
            self.good_paths.append(path.copy())  # Need to create copy as path list continues to be used
        else:
            for neigh in self.graph[cur]:
                if not self.small_cave_allowances(path, neigh):
                    continue
                self.all_paths_recurs(neigh, end, path)

        # Once all options exhausted, remove current vertex from path[] and mark it as unvisited
        # This depends on path and visited sharing references up and down the recursion
        path.pop()

    def small_cave_allowances(self, path, neigh):
        cave_count = Counter(n for n in path + [neigh] if n.islower())
        if not cave_count:
            return True
        if neigh == 'start':
            return False
        if self.can_visit_twice:
            if cave_count.most_common()[0][1] == 3:  # If there'd now be a cave visited 3x
                return False
            elif Counter(list(cave_count.values()))[2] == 2:  # If there'd now be TWO caves visited more than 1x
                return False
        if not self.can_visit_twice and cave_count.most_common()[0][1] == 2:  # If can't visit 2x and a cave is 2x
            return False
        return True

    def all_paths(self, start, end):
        path = []
        self.all_paths_recurs(start, end, path)
        return self.good_paths


def solve(text, can_visit_twice=False):
    graph = Graph(get_graph(text), can_visit_twice)
    return graph.all_paths('start', 'end')


def test():
    assert len(solve(TEST)) == 10
    assert len(solve(TEST2)) == 19
    assert len(solve(TEST3)) == 226
    assert len(solve(INPUT)) == 5576

    assert len(solve(TEST, can_visit_twice=True)) == 36
    assert len(solve(TEST2, can_visit_twice=True)) == 103
    assert len(solve(TEST3, can_visit_twice=True)) == 3509


##########################
if __name__ == '__main__':
    test()
    print(len(solve(INPUT, can_visit_twice=True)))  # 152837
