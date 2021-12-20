import unittest
from collections import defaultdict, deque


def get_bin(grid, row, col):
    grid_slice = grid[row - 1][col - 1:col + 2] + grid[row][col - 1:col + 2] + grid[row + 1][col - 1:col + 2]
    bin_list = list('1' if x == '#' else '0' for x in
                    grid_slice)
    bin_str = "".join(bin_list)
    return int(bin_str, 2)


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    # TODO put solution here
    lookup = ""
    grid = []
    with open(filename) as openfileobject:
        for line in openfileobject:
            tline = line.strip()
            if not lookup:
                lookup = tline
            elif not tline:
                pass
            else:
                grid.append([c for c in tline])


    max_r = len(grid)+4
    max_c = len(grid[0])+4

    new_g = grid

    new_char = [[lookup[-1]], [lookup[0]]]
    for rounds in range(50):

        round_char = new_char[rounds % 2]


        grid2 = []
        #grid2.append(round_char * (max_c+2))

        for r in new_g:
            grid2.append(round_char*2  + r + round_char*2)
        grid2.insert(0,round_char * len(grid2[-1]))
        grid2.insert(0,round_char * len(grid2[-1]))
        grid2.append(round_char * len(grid2[-1]))
        grid2.append(round_char * len(grid2[-1]))

        max_r = len(grid2)
        max_c = len(grid2[0])

        new_g = [[round_char[0] for _ in range(max_c)] for x in range(max_r)]

        cnt = 0
        for row in range(1, max_r - 1):
            for col in range(1, max_c - 1):
                ndx = get_bin(grid2, row, col)
                new_g[row][col] = lookup[ndx]
                if lookup[ndx] == '#':
                    cnt += 1

        res1 = []
        for r in new_g[1:-1]:
            res1.append(r[1:-1])

        new_g = res1

        print(" -- newG after 2 round -- ")
        for pr in new_g:
            print("".join(pr))


    return cnt


print(solve(1, False))

#42888 too high
#5483 too low
class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
