import unittest
from collections import defaultdict, deque

def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    ctr = 0
    elves = defaultdict(int)

    curr = 0
    total = 0

    # TODO put solution here
    with open(filename) as openfileobject:
        for line in openfileobject:
            tline = line.strip()
            if (tline == ''):
                ctr +=1
                curr = 0
            else:
                cals = int(tline)
                curr += cals
                total = max(curr, total)
                elves[ctr] += cals



    if part == 1:
        return total

    if part == 2:
        return sum(v for k, v in sorted(elves.items(), key=lambda item: item[1])[-3:])



print(solve(2, False))


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
