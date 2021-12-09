import math
import sys
import unittest
from collections import deque
import timeit


def better_part_2(part):
    # https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/9.py

    filename = "input.txt"

    field = []
    with open(filename) as openfileobject:
        for line in openfileobject:
            tline = line.strip()
            if tline:
                field.append([int(c) for c in tline])

    low_values = []
    low_points = []

    max_col = len(field[0])
    max_row = len(field)

    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]

    for row in range(max_row):
        for col in range(max_col):
            current_val = field[row][col]

            is_low_point = True
            for direction in range(4):
                r = row + DR[direction]
                c = col + DC[direction]

                if 0 <= r < max_row and 0 <= c < max_col and field[r][c] <= field[row][col]:
                    is_low_point = False
                    break

            if is_low_point:
                low_values.append(current_val)
                low_points.append((row, col))

    if part == 1:
        return sum(low_values) + len(low_values)

    basins = []

    for basin in low_points:
        q = deque()
        q.append(basin)
        size = 0
        while q:
            row, col = q.popleft()
            if field[row][col] == 9:
                continue

            field[row][col] = 9

            size += 1
            for direction in range(4):
                r = row + DR[direction]
                c = col + DC[direction]
                if 0 <= r < max_row and 0 <= c < max_col and field[r][c] != 9:
                    q.append((r, c))
        basins.append(size)

    return math.prod(sorted(basins, reverse=True)[0:3])


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    field = []
    # TODO put solution here
    with open(filename) as openfileobject:
        for line in openfileobject:
            tline = line.strip()
            if tline:
                field.append([int(c) for c in tline])

    low_values = []
    low_points = []

    max_col = len(field[0])
    max_row = len(field)

    for row in range(max_row):
        for col in range(max_col):
            current_val = field[row][col]
            if col > 0 and field[row][col - 1] <= current_val:
                continue
            elif col < max_col - 1 and field[row][col + 1] <= current_val:
                continue
            elif row > 0 and field[row - 1][col] <= current_val:
                continue
            elif row < max_row - 1 and field[row + 1][col] <= current_val:
                continue

            low_values.append(current_val)
            item = set()
            item.add((row, col))
            low_points.append(item)

    if part == 1:
        return sum(low_values) + len(low_values)

    for basin in low_points:

        while True:
            found = set()
            for row, col in basin:

                # add left
                if col > 0 and field[row][col - 1] != 9:
                    found.add((row, col - 1))

                # add right
                if col < max_col - 1 and field[row][col + 1] != 9:
                    found.add((row, col + 1))

                # add up
                if row > 0 and field[row - 1][col] != 9:
                    found.add((row - 1, col))

                # add down
                if row < max_row - 1 and field[row + 1][col] != 9:
                    found.add((row + 1, col))

            old_size = len(basin)
            basin.update(found)

            if len(basin) == old_size:
                break

    largest = sorted([len(x) for x in low_points], reverse=True)[0:3]

    return math.prod(largest)


print("mine")
print(timeit.timeit("solve(2, False)", number=10, globals=globals()))
print("better")
print(timeit.timeit("better_part_2(2)", number=10, globals=globals()))



class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
