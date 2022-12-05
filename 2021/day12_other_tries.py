from collections import Counter
import random

class NoMoves(Exception):
    pass


class Path:
    def __init__(self, start, end, nodes):
        self.cur = start
        self.end = end
        self.nodes = nodes
        self.nodes_visited = [start]

    def explore(self):
        while 1:
            # print(f"Starting at {self.cur} (prev: {self.nodes_visited})")
            if self.cur == self.end:
                # print("Done!\n")
                return self.nodes_visited
            try:
                legal_moves = self.find_legal_nodes()
            except NoMoves:
                # print("\tNo moves!")
                return None, None
            move = random.choice(legal_moves)
            # print(f"\tOptions are: {legal_moves}")
            # print(f"\tMoved to {move}")
            self.cur = move
            self.nodes_visited.append(move)

    def find_legal_nodes(self):
        all_options = self.nodes[self.cur]
        for node in self.nodes_visited:
            if node in all_options and node.islower():
                all_options.remove(node)
        if not all_options:
            raise NoMoves
        return all_options


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


def solve(text):  # Too slow, doesn't work
    nodes = get_graph(text)

    all_paths = [tuple(Path('start', 'end', nodes).explore()) for _ in range(1000000)]

    count = Counter(all_paths)
    del count[(None, None)]

    for good_path, freq in count.items():
        print(good_path, freq)
    return len(count)


def bfs(graph, node):
    # From https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
    visited = set()  # List to keep track of visited nodes.
    queue = []  # Initialize a queue
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def dfs(graph, node):
    # From https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
    visited = set()

    def dfs_recurse(graph_use, node_cur):
        if node_cur not in visited:
            print(node_cur, end=" ")
            visited.add(node_cur)
            for neighbour in graph_use[node_cur]:
                dfs_recurse(graph_use, neighbour)

    dfs_recurse(graph, node)
