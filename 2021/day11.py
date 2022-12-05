from itertools import chain
from contextlib import suppress
TEST = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

TEST_STEP1 = """6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637"""

TEST_STEP2 = """8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848"""

TEST_STEP3 = """0050900866
8500800575
9900000039
9700000041
9935080063
7712300000
7911250009
2211130000
0421125000
0021119000"""

TEST_STEP10 = """0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000"""

TEST_STEP100 = """0397666866
0749766918
0053976933
0004297822
0004229892
0053222877
0532222966
9322228966
7922286866
6789998766"""

INPUT = """4738615556
6744423741
2812868827
8844365624
4546674266
4518674278
7457237431
4524873247
3153341314
3721414667"""

OFFSET_VECTORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
assert len(set(OFFSET_VECTORS)) == len(OFFSET_VECTORS)


def increment(table):
    return [[i + 1 for i in row] for row in table]


def increment_neighbours(table, i, j):
    for x_offset, y_offset in OFFSET_VECTORS:
        with suppress(IndexError):
            if i + x_offset < 0 or j + y_offset < 0:
                continue
            cell_neigh = table[i + x_offset][j + y_offset]
            if cell_neigh != 0:
                table[i + x_offset][j + y_offset] += 1
    return table


def resolve(table, new_activations_td=0):
    activations_triggered = False
    for idx, cell in enumerate(chain.from_iterable(table)):
        i = idx // len(table)
        j = idx % len(table)

        if cell >= 10:
            activations_triggered = True
            new_activations_td += 1
            table[i][j] = 0
            table = increment_neighbours(table, i, j)
    if activations_triggered:
        return resolve(table, new_activations_td)
    else:
        return table, new_activations_td


def evolve_table(table_raw, steps):
    activations = 0
    table = [[int(ch) for ch in line] for line in table_raw.split('\n')]
    for i in range(steps):
        table = increment(table)
        table, new_activations = resolve(table)
        activations += new_activations
    return table, activations


def find_sync(table_raw):
    table = [[int(ch) for ch in line] for line in table_raw.split('\n')]
    step = 0
    while 1:
        step += 1
        table = increment(table)
        table, _ = resolve(table)
        if all_synced(table):
            break
    return step


def all_synced(table):
    return all(cell == 0 for cell in chain.from_iterable(table))


def to_str(table_int):
    table_str = ''
    for row in table_int:
        table_str += ''.join(str(r) for r in row) + '\n'
    return table_str.rstrip()


def test():
    assert to_str(evolve_table(TEST, 1)[0]) == TEST_STEP1
    assert to_str(evolve_table(TEST, 2)[0]) == TEST_STEP2
    assert to_str(evolve_table(TEST, 3)[0]) == TEST_STEP3
    assert to_str(evolve_table(TEST, 10)[0]) == TEST_STEP10
    assert evolve_table(TEST, 10)[1] == 204
    assert to_str(evolve_table(TEST, 100)[0]) == TEST_STEP100
    assert evolve_table(TEST, 100)[1] == 1656
    assert find_sync(TEST) == 195


##########################
if __name__ == '__main__':
    test()
    print(evolve_table(INPUT, 100)[1])
    print(find_sync(INPUT))
