import unittest
from collections import defaultdict, deque


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:

        lines = [[x[0].split('-'), x[1].split('-')] for x in [l.strip().split(',') for l in openfileobject.readlines()]]

    overlaps = 0
    for line in lines:
        if (int(line[0][0]) >= int(line[1][0])) and (int(line[0][1]) <= int(line[1][1])):
            overlaps += 1
        elif (int(line[1][0]) >= int(line[0][0])) and (int(line[1][1]) <= int(line[0][1])):
            overlaps += 1

    if part == 1:
        return overlaps

    overlaps = 0
    for line in lines:
        r1 = set(range(int(line[0][0]), int(line[0][1]) + 1))
        r2 = set(range(int(line[1][0]), int(line[1][1]) + 1))

        overlaps += 1 if len(r1.intersection(r2)) > 0 else 0

    return overlaps




print(solve(2, False))



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
