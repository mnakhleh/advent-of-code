from collections import deque, Counter, defaultdict
import copy

TEST = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

INPUT = """KKOSPHCNOCHHHSPOBKVF

NV -> S
OK -> K
SO -> N
FN -> F
NB -> K
BV -> K
PN -> V
KC -> C
HF -> N
CK -> S
VP -> H
SK -> C
NO -> F
PB -> O
PF -> P
VC -> C
OB -> S
VF -> F
BP -> P
HO -> O
FF -> S
NF -> B
KK -> C
OC -> P
OV -> B
NK -> B
KO -> C
OH -> F
CV -> F
CH -> K
SC -> O
BN -> B
HS -> O
VK -> V
PV -> S
BO -> F
OO -> S
KB -> N
NS -> S
BF -> N
SH -> F
SB -> S
PP -> F
KN -> H
BB -> C
SS -> V
HP -> O
PK -> P
HK -> O
FH -> O
BC -> N
FK -> K
HN -> P
CC -> V
FO -> F
FP -> C
VO -> N
SF -> B
HC -> O
NN -> K
FC -> C
CS -> O
FV -> P
HV -> V
PO -> H
BH -> F
OF -> P
PC -> V
CN -> O
HB -> N
CF -> P
HH -> K
VH -> H
OP -> F
BK -> S
SP -> V
BS -> V
VB -> C
NH -> H
SN -> K
KH -> F
OS -> N
NP -> P
VN -> V
KV -> F
KP -> B
VS -> F
NC -> F
ON -> S
FB -> C
SV -> O
PS -> K
KF -> H
CP -> H
FS -> V
VV -> H
CB -> P
PH -> N
CO -> N
KS -> K"""


def get_count_and_succs(pair_dict):
    successors = {}
    pair_count = defaultdict(int)
    for pair, ins in pair_dict.items():
        pair_count[pair[0] + ins] = 0
        pair_count[ins + pair[1]] = 0
        successors[pair] = (pair[0] + ins, ins + pair[1])
    return pair_count, successors


def main_grouped(text, steps):
    template, pairs = [val.strip() for val in text.split('\n\n')]
    pair_dict = get_pair_dict(pairs)
    pair_count, successors = get_count_and_succs(pair_dict)

    for start_pair in [template[i] + template[i+1] for i in range(len(template)-1)]:
        pair_count[start_pair] += 1

    for _ in range(steps):
        pair_count_new = defaultdict(int)
        for pair, count in pair_count.items():
            for succ in successors[pair]:
                pair_count_new[succ] += count
        pair_count = copy.deepcopy(pair_count_new)
    return score_grouped(pair_count, template)


def score_grouped(pair_count, starting_poly):
    full_count = defaultdict(int)
    for (lett_1, lett_2), count in pair_count.items():
        full_count[lett_1] += count
        full_count[lett_2] += count
    full_count[starting_poly[0]] += 1
    full_count[starting_poly[-1]] += 1

    as_counter = Counter({k: v//2 for k, v in full_count.items()})
    return as_counter.most_common()[0][1] - as_counter.most_common()[-1][1]


def get_pair_dict(pairs):
    pair_dict = dict()
    for line in pairs.split('\n'):
        pr, ins = line.split(' -> ')
        pair_dict[pr] = ins
    return pair_dict


def main(text, steps):
    template, pairs = [val.strip() for val in text.split('\n\n')]
    pair_dict = get_pair_dict(pairs)

    poly = str(template)
    for i in range(steps):
        poly = extend_poly(poly, pair_dict)
    return poly


def extend_poly(poly, pair_dict):
    poly_q = deque(poly[0])
    prev_char = poly[0]
    for char in list(poly)[1:]:
        try:
            poly_q.extend([pair_dict[prev_char + char], char])
        except KeyError:
            poly_q.append(char)
        prev_char = char
    return poly_q


def scoreit(poly):
    counter = Counter(poly)
    return counter.most_common()[0][1] - counter.most_common()[-1][1]


def test():
    assert scoreit(main(TEST, 10)) == 1588
    assert scoreit(main(INPUT, 10)) == 2321
    assert main_grouped(TEST, 1) == scoreit('NCNBCHB')
    assert main_grouped(TEST, 2) == scoreit('NBCCNBBBCBHCB')
    assert main_grouped(TEST, 3) == scoreit('NBBBCNCCNBBNBNBBCHBHHBCHB')
    assert main_grouped(TEST, 4) == scoreit('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')
    assert main_grouped(TEST, 40) == 2188189693529


##########################
if __name__ == '__main__':
    test()
    print(main_grouped(INPUT, 40))
    # print(main_grouped(TEST, 10))
