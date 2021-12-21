import sys
import unittest
from collections import defaultdict, deque

#sys.setrecursionlimit(15000)
memo = dict()


def count_wins(current_pos, current_score, turn):
    if current_score[0] >= 21:
        return [1, 0]

    if current_score[1] >= 21:
        return [0, 1]
    memo_key1 = f'{current_pos},{current_score},{turn}'
    if memo_key1 in memo:
        return memo[memo_key1]

    cpos2 = [current_pos[1], current_pos[0]]
    cscore2 = [current_score[1], current_score[0]]
    memo_key2 = f'{cpos2},{cscore2},{(turn+1)%2}'
    if memo_key2 in memo:
        x,y = memo[memo_key2]
        return [y,x]


    dies = [[n1, n2, n3] for n1 in range(1, 4) for n2 in range(1, 4) for n3 in range(1, 4)]

    wins = [0, 0]
    for die in dies:
        new_pos = current_pos.copy()
        new_pos[turn] = ((new_pos[turn] + sum(die)) - 1) % 10 + 1
        new_score = current_score.copy()
        new_score[turn] += new_pos[turn]
        new_wins = count_wins(new_pos, new_score, (turn + 1) % 2)
        wins[0] += new_wins[0]
        wins[1] += new_wins[1]

    memo[memo_key1] = wins
    return wins

def part2(useExample):
    start1 = 4 if useExample else 2
    start2 = 8 if useExample else 7

    pos = [start1, start2]
    score = [0, 0]
    turn = 0

    wins = count_wins(pos, score, turn)

    return wins

def solve(part, useExample):
    start1 = 4 if useExample else 2
    start2 = 8 if useExample else 7

    pos = [start1, start2]
    score = [0, 0]
    die = 0
    turn = 0
    rolls = 0
    while score[0] < 1000 and score[1] < 1000:
        #        print(f'[roll: {rolls} Player: {turn+1} Pos: {pos[turn]} Score: {score[turn]} die: {die}]')
        diesum = 0
        for i in range(3):
            die = (die % 100) + 1
            #   print(die)
            diesum += die

        #       print(f' - diesum: {diesum} die: {die}')

        rolls += 3
        raw_pos = (pos[turn] + diesum)
        pos[turn] = (raw_pos - 1) % 10 + 1
        #      print(f' - newpos: {pos[turn]}')

        score[turn] += pos[turn]
        #     print(f' - newscore: {score[turn]}')

        if score[turn] >= 1000:
            return rolls * score[(turn + 1) % 2]

        turn = (turn + 1) % 2
    #    print(f' - newturn: {turn+1}')

    return None

#print(solve(1, False))
print(max(part2(False)))

class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
