import heapq
import sys
import unittest
from collections import defaultdict, deque

l = []
for i in range(998, 1015):
    n = i % 9 + 1
    l.append(n)


# print(l)
# exit(0)

def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    G = []
    with open(filename) as openfileobject:
        for line in openfileobject:
            G.append([int(x) for x in line.strip()])

    max_row = len(G)
    max_col = len(G[0])

    C = [[sys.maxsize for x in range(max_col * 5)] for x in range(max_row * 5)]
    G2 = [[0 for x in range(max_col * 5)] for x in range(max_row * 5)]

    for extra_row in range(5):
        for extra_col in range(5):
            for row in range(max_row):
                for col in range(max_col):
                    c_row = row + extra_row * max_row
                    c_col = col + extra_col * max_col

                    if c_row == 0 and c_col == 0:
                        continue

                    new_g = ((G[row][col] + extra_row + extra_col) - 1) % 9 + 1
                    G2[c_row][c_col] = new_g

    # pathfinding!
    frontier = []
    c_r = 0
    c_c = 0

    heapq.heappush(frontier, (0, (c_r, c_c)))
    C[c_r][c_c] = 0

    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]

    while frontier:
        priority, (row, col) = heapq.heappop(frontier)

        if row == (max_row*5) - 1 and col == (max_col*5) - 1:
            C[(max_row*5)-1][(max_col*5)-1] = priority
            break

        neighbors = []
        for dirs in range(4):
            rr = row + DR[dirs]
            cc = col + DC[dirs]
            if 0<= rr < (max_row*5) and 0<=cc<(max_col*5):
                neighbors.append((rr,cc))

        for (nr,nc) in neighbors:
            cost=C[row][col] + G2[nr][nc]
            if cost < C[nr][nc]:
                C[nr][nc] = cost
                heapq.heappush(frontier, (cost, (nr,nc)))



    return C[-1][-1]

    return None


# gues 2944 part 2 (too high)
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
