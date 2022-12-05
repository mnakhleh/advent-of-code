import time
from functools import lru_cache


TEST = """#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########"""


INPUT = """#############
#...........#
###A#D#B#C###
  #D#C#B#A#
  #D#B#A#C#
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


class Graph:
    """Adapted from https://www.geeksforgeeks.org/find-paths-given-source-destination/"""
    def __init__(self, amphipod_locs):
        self.amphipod_locs = amphipod_locs
        self.best = 1000000
        self.cur_score = 0
        self.path = []
        for (row, col), amphi in self.amphipod_locs.items():
            amphi.is_good = self.set_good(amphi, (row, col))

    def best_score(self):
        self.dfs_recurse('start')
        return self.best

    def dfs_recurse(self, new_instruction, i=0):
        self.change_state(new_instruction)

        if self.cur_score < self.best:
            if self.winning():
                print(f"Won ({self.cur_score})")
                print(self.path)
                self.best = self.cur_score
            else:
                for instruction in self.valid_instructions():
                    self.dfs_recurse(instruction, i)

        self.revert_state(new_instruction)

    def change_state(self, instruction):
        self.path.append(instruction)
        if instruction == 'start':
            return
        start_pos, end_pos = instruction
        amphi = self.amphipod_locs[start_pos]
        amphi.moved += 1
        amphi.is_good = self.set_good(amphi, end_pos)
        self.amphipod_locs[end_pos] = amphi
        del self.amphipod_locs[start_pos]
        self.cur_score += amphi.weight * len(self.on_path(start_pos, end_pos))

    def revert_state(self, instruction):
        self.path.remove(instruction)
        if instruction == 'start':
            return
        start_pos, end_pos = instruction
        amphi = self.amphipod_locs[end_pos]
        amphi.moved -= 1
        amphi.is_good = self.set_good(amphi, start_pos)
        self.amphipod_locs[start_pos] = amphi
        del self.amphipod_locs[end_pos]
        self.cur_score -= amphi.weight * len(self.on_path(start_pos, end_pos))

    def valid_instructions(self):
        instructions = []
        for cur_coords, amphi in self.amphipod_locs.items():
            if amphi.is_good:
                continue

            burrowing = False
            for row_bur in range(5, 1, -1):
                if not self.is_legal(cur_coords, (row_bur, amphi.win_col)):
                    continue
                for row_deeper in range(row_bur+1, 6):
                    deeper_amphi = self.amphipod_locs.get((row_deeper, amphi.win_col), None)
                    if not deeper_amphi or deeper_amphi.typ != amphi.typ:
                        break
                else:
                    instructions.append((cur_coords, (row_bur, amphi.win_col)))
                    burrowing = True
            if burrowing:  # Prioritize burrows
                continue

            for corr_coords in CORRIDOR_LOCS:
                if amphi.moved == 0 and self.is_legal(cur_coords, corr_coords):
                    instructions.append((cur_coords, corr_coords))
        return instructions

    def winning(self):
        return all(col == amphi.win_col for (_, col), amphi in self.amphipod_locs.items())

    def set_good(self, amphi, amphi_coords):
        row, col = amphi_coords
        if col != amphi.win_col:
            return False
        elif row == 5:
            return True
        for row_bur in range(row + 1, 6):
            amphi_deeper = self.amphipod_locs.get((row_bur, col), None)
            if not amphi_deeper or amphi_deeper.typ != amphi.typ:
                return False
        return True

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


def solve(text):
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
    assert solve(TEST) == 44169
    assert solve(INPUT) == 53308
