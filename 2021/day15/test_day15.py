import sys
import unittest
from collections import defaultdict, deque


l =[]
for i in range(998,1015):
    n = i%9 + 1
    l.append(n)

#print(l)
#exit(0)

def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    G = []
    with open(filename) as openfileobject:
        for line in openfileobject:
            G.append([int(x) for x in line.strip()])

    max_row = len(G)
    max_col = len(G[0])

    C = [[0 for x in range(max_col*5)] for x in range(max_row*5)]
    G2 = [[0 for x in range(max_col*5)] for x in range(max_row*5)]


    for extra_row in range(5):
        for extra_col in range(5):
            for row in range(max_row):
                for col in range(max_col):
                    c_row = row + extra_row*max_row
                    c_col = col + extra_col*max_col
#                    print(f'R:{row},{col}  C:{c_row},{c_col}')

                    if c_row == 0 and c_col == 0:
                        continue

                    costs =[]


                    new_g = ((G[row][col] + extra_row + extra_col)-1) % 9 + 1

                    if row==99 and col==99:
                        print(new_g, end='')

                    G2[c_row][c_col] = new_g
                    upper = new_g
                    if c_row > 0:
                        costs.append(upper + C[c_row - 1][c_col])

                    lefter = new_g
                    if c_col > 0:
                        costs.append(lefter + C[c_row][c_col-1])

                    C[c_row][c_col] = min(costs)
        print()


    for r in C[0:3]:
        print(",".join([str(i) for i in r]))
        print()
    return C[-1][-1]

    return None

#gues 2944 part 2 (too high)
print(solve(1, False))


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
