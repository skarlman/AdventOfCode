import unittest
from collections import defaultdict, deque


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        raw = openfileobject.read()
    lines_raw, moves_raw = raw.split('\n\n')

    lines = lines_raw.split('\n')[:-1]
    moves = moves_raw.split('\n')

    stacks = []
    for _ in range(3 if useExample else 9 ):
        stacks.append([])

    for row in lines[:]:

        for i,c in enumerate(row):
            if c in ['\n', '[', ']']:
                continue
            if c != ' ':
                stack_number = (i - 1)//4
                stacks[stack_number].insert(0, c)

    if part == 1:
        for move in moves:
            _, take, _, f, _, t = move.split()
            take = int(take)
            f = int(f)-1
            t = int(t)-1
            for i in range(take):
                tmp = stacks[f].pop()
                stacks[t].append(tmp)

        word = [x[-1] for x in stacks]
        return "".join(word)

    if part == 2:
        for move in moves:
            _, take, _, f, _, t = move.split()
            take = int(take)
            f = int(f)-1
            t = int(t)-1
            stacks[t] += stacks[f][-take:]
            for i in range(take):
                tmp = stacks[f].pop()


        word = [x[-1] for x in stacks]
        return "".join(word)

print(solve(2, True))



#
# class AocTest(unittest.TestCase):
#     def test_part_a_real(self):
#         self.assertEqual(4421, solve(1, False), "Part 1 REAL")
#
#     def test_part_a_example(self):
#         self.assertEqual(5, solve(1, True), "Part 1 example")
#
#     def test_part_b_real(self):
#         self.assertEqual(18674, solve(2, False), "Part 2 REAL")
#
#     def test_part_b_example(self):
#         self.assertEqual(12, solve(2, True), "Part 2 example")
