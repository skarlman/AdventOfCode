import unittest
from collections import defaultdict, deque

def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:

        lines = [l.strip() for l in  openfileobject.readlines()]

    for line in lines:
        tline = line.strip()
        left = set(tline[:len(tline)//2])
        right = set(tline[len(tline)//2:])

        for c in left:
            if c in right:
                prio = (ord(c) - (64 -26 if c.isupper() else 96))
                # print(f'{c}: {prio}')
                score_part1 += prio

    if part == 1:
        return score_part1

    score_part2 = 0
    for i in range(len(lines)//3):
        index = i*3
        r1 = set(lines[index])
        r2 = set(lines[index+1])
        r3 = set(lines[index+2])

        for c in r1:
            if c in r2 and c in r3:
                score_part2 += (ord(c) - (64 -26 if c.isupper() else 96))
                break

    return score_part2

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
