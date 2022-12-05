import re
from collections import defaultdict, Counter
from itertools import product

TEST = """Player 1 starting position: 4
Player 2 starting position: 8"""

INPUT = """"Player 1 starting position: 6
Player 2 starting position: 4"""


def move_freq():
    possible_moves = [sum(x) for x in product((1, 2, 3), repeat=3)]
    return sorted(Counter(possible_moves).items())


DIRAC_COUNTS = move_freq()


def toggle(player):
    if player == 1:
        return 2
    return 1


class Die:
    i = 0
    count = 1

    def roll(self):
        self.i = 1 if self.count == 1 else self.i + 3
        self.count += 1
        if self.i > 100:
            self.i -= 100
        return 3*(self.i+1)


def resolve(text, score_max):
    init_moves = [int(re.search(r'starting position: (\d)', line).group(1)) for line in text.split('\n')]
    moves = {1: init_moves[0], 2: init_moves[1]}
    scores = {1: 0, 2: 0}
    player_turn = 1
    die = Die()
    while True:
        turn_moves = die.roll()
        moves[player_turn] += turn_moves
        scores[player_turn] += moves[player_turn] % 10 if moves[player_turn] % 10 != 0 else 10
        if scores[player_turn] >= score_max:
            print(f"Player {player_turn} wins with {scores[player_turn]} on turn {die.count}")
            break
        player_turn = toggle(player_turn)
    return 3*(die.count-1) * scores[toggle(player_turn)]


def wrap10(pos):
    return pos % 10 or 10


def move_gen(plyr, verse):
    nextverse = defaultdict(int)
    for ((ascore, apos, bscore, bpos), nb_universes), (move, movecount) in product(verse.items(), DIRAC_COUNTS):
        if plyr == 'a':
            apos = wrap10(apos + move)
            ascore += apos
        else:
            bpos = wrap10(bpos + move)
            bscore += bpos
        nextverse[(ascore, apos, bscore, bpos)] += nb_universes * movecount
    return nextverse


def cull_winners(verse, completed):
    for k in list(verse):
        (ascore, apos, bscore, bpos) = k
        if ascore >= 21 or bscore >= 21:
            completed.append((ascore, bscore, verse[k]))
            del verse[k]


def resolve_dirac(text):
    """With lots of help from wleftwich: https://www.reddit.com/r/adventofcode/comments/rl6p8y/comment/hpinq8a"""
    init_moves = [int(re.search(r'starting position: (\d)', line).group(1)) for line in text.split('\n')]
    verse = {(0, init_moves[0], 0, init_moves[1]): 1}
    completed = []
    while verse:
        verse = move_gen('a', verse)
        cull_winners(verse, completed)
        verse = move_gen('b', verse)
        cull_winners(verse, completed)

    part_2 = [sum(c for (a, b, c) in completed if a >= 21),
              sum(c for (a, b, c) in completed if b >= 21)]

    print('part_2 =', part_2)


#########################
if __name__ == '__main__':
    # assert resolve(TEST, score_max=1000) == 739785
    # print(resolve(INPUT, score_max=1000))
    resolve_dirac(INPUT)


