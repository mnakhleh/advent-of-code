from functools import lru_cache

EMPTY_BOARD = """#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #########"""


TEST = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""


INPUT = """#############
#...........#
###A#D#B#C###
  #B#C#D#A#
  #########"""


WEIGHTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
WINNING_CORRIDOR = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
CORRIDOR_LOCS = ((1, 1), (1, 2), (1, 4), (1, 6), (1, 8), (1, 10), (1, 11))


class Amphipod:
    def __init__(self, typ):
        self.typ = typ
        self.weight = WEIGHTS[typ]
        self.win_col = WINNING_CORRIDOR[typ]
        self.moved = 0
        self.is_good = False

    def __str__(self):
        return self.typ


class Graph:
    """Adapted from https://www.geeksforgeeks.org/find-paths-given-source-destination/"""
    def __init__(self, amphipod_locs):
        self.amphipod_locs = amphipod_locs
        for (row, col), amphi in self.amphipod_locs.items():
            amphi.is_good = self.set_good(amphi, (row, col))
        self.best = 1000000
        self.cur_score = 0
        self.path = []

    @lru_cache
    def _distance(self, start, end):
        return len(self.on_path(start, end))

    def winning(self):
        return all(col == amphi.win_col for (_, col), amphi in self.amphipod_locs.items())

    def set_good(self, amphi, amphi_coords):
        row, col = amphi_coords
        if col != amphi.win_col:
            return False
        elif row == 3:
            return True
        amphi_deeper = self.amphipod_locs.get((row + 1, col), None)
        return amphi_deeper and amphi_deeper.typ == amphi.typ

    def forward(self, instruction):
        self.path.append(instruction)
        if instruction == 'start':
            return
        start_pos, end_pos = instruction
        amphi = self.amphipod_locs[start_pos]
        amphi.moved += 1
        amphi.is_good = self.set_good(amphi, end_pos)
        self.amphipod_locs[end_pos] = amphi
        del self.amphipod_locs[start_pos]
        self.cur_score += amphi.weight * self._distance(start_pos, end_pos)

    def backward(self, instruction):
        self.path.remove(instruction)
        if instruction == 'start':
            return
        start_pos, end_pos = instruction
        amphi = self.amphipod_locs[end_pos]
        amphi.moved -= 1
        amphi.is_good = self.set_good(amphi, start_pos)
        self.amphipod_locs[start_pos] = amphi
        del self.amphipod_locs[end_pos]
        self.cur_score -= amphi.weight * self._distance(start_pos, end_pos)

    def valid_instructions(self):
        instructions = []
        for cur_coords, amphi in self.amphipod_locs.items():
            if amphi.is_good:
                continue

            if self.is_legal(cur_coords, (3, amphi.win_col)):
                instructions.append((cur_coords, (3, amphi.win_col)))
                continue

            elif self.is_legal(cur_coords, (2, amphi.win_col)):
                deeper_amphi = self.amphipod_locs.get((3, amphi.win_col), None)
                if deeper_amphi and deeper_amphi.typ == amphi.typ:
                    instructions.append((cur_coords, (2, amphi.win_col)))
                    continue
            for corr_coords in CORRIDOR_LOCS:
                if amphi.moved == 0 and self.is_legal(cur_coords, corr_coords):
                    instructions.append((cur_coords, corr_coords))
        return instructions

    def is_legal(self, coord1, coord2):
        path_coords = self.on_path(coord1, coord2)
        return path_coords and set(path_coords) & set(self.amphipod_locs) == set()

    @staticmethod
    @lru_cache
    def on_path(start, end):
        all_options = []
        (start_row, start_col), (end_row, end_col) = start, end
        x1, x2 = sorted([start_col, end_col])
        for row_val in range(x1, x2 + 1):
            all_options.append((1, row_val))
        for col_val in range(2, start_row + 1):
            all_options.append((col_val, start_col))
        for col_val in range(2, end_row + 1):
            all_options.append((col_val, end_col))
        all_options.remove(start)
        return all_options

    def dfs_recurse(self, new_instruction, i=0):
        self.forward(new_instruction)
        if self.cur_score < self.best:
            if self.winning():
                # print(f"Won ({self.cur_score})")
                # print(self.path)
                self.best = self.cur_score
            else:
                for instruction in self.valid_instructions():
                    self.dfs_recurse(instruction, i)

        self.backward(new_instruction)

    def best_score(self):
        self.dfs_recurse('start')
        return self.best


def solve(text):
    import time
    t0 = time.perf_counter()
    amphipod_locs = {}
    for i, row in enumerate(text.split('\n')):
        for j, typ in enumerate(row):
            if typ in ('A', 'B', 'C', 'D'):
                amphi = Amphipod(typ)
                amphipod_locs[(i, j)] = amphi

    graph = Graph(amphipod_locs)
    score = graph.best_score()
    print(time.perf_counter() - t0)
    return score


##########################
if __name__ == '__main__':
    assert solve(TEST) == 12521
    assert solve(INPUT) == 13336
