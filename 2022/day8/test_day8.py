import copy
import unittest
from collections import defaultdict, deque


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read().strip()
        rows = [l.strip() for l in openfileobject.readlines()]

    # cols = copy.deepcopy(rows)

    visible = set()
    total_rows = len(rows)
    total_cols = len(rows[0])

    for row in range(total_rows):
        high_left = rows[row][0]
        high_right = rows[row][-1]
        for col in range(total_cols):
            if col == 0:
                visible.add((row, col))
                visible.add((row, total_cols - col - 1))
            else:
                if rows[row][col] > high_left:
                    visible.add((row, col))
                    high_left = rows[row][col]

                if rows[row][total_cols - col - 1] > high_right:
                    visible.add((row, total_cols - col - 1))
                    high_right = rows[row][total_cols - col - 1]

    for col in range(total_rows):
        high_up = rows[0][col]
        high_down = rows[-1][col]
        for row in range(total_cols):

            if row == 0:
                visible.add((row, col))
                visible.add((total_rows - row - 1, col))
            else:
                if rows[row][col] > high_up:
                    visible.add((row, col))
                    high_up = rows[row][col]

                if rows[total_rows - row - 1][col] > high_down:
                    visible.add((total_rows - row - 1, col))
                    high_down = rows[total_rows - row - 1][col]

    max_seen = 0
    for row in range(total_rows):
        if row == 0 or row == total_rows-1:
            continue

        for col in range(total_cols):
            if col == 0 or col == total_cols -1:
                continue
            multiplied = 1
            current_seen = 0
            current_val = rows[row][col]

            # up
            if row > 0:
                for r in range(row):
                    if rows[row - r - 1][col] < current_val:
                        current_seen += 1
                    else:
                        multiplied *= (current_seen + 1)
                        max_seen = max(max_seen, multiplied)
                        current_seen = 0
                        break
                if (current_seen > 0):
                    multiplied *= current_seen
                    max_seen = max(max_seen, multiplied)
                    current_seen = 0
            else:
                continue

            # down
            if row < total_rows - 1:
                for r in range(total_rows - row - 1):
                    if rows[row + r + 1][col] < current_val:
                        current_seen += 1
                    else:
                        multiplied *= (current_seen + 1)
                        max_seen = max(max_seen, multiplied)
                        current_seen = 0
                        break

                if (current_seen > 0):
                    multiplied *= current_seen
                    max_seen = max(max_seen, multiplied)
                    current_seen = 0

            # left
            if col > 0:
                for c in range(col):
                    if rows[row][col - c - 1] < current_val:
                        current_seen += 1
                    else:
                        multiplied *= (current_seen + 1)
                        max_seen = max(max_seen, multiplied)
                        current_seen = 0
                        break
                if (current_seen > 0):
                    multiplied *= current_seen
                    max_seen = max(max_seen, multiplied)
                    current_seen = 0
            else:
                continue

            # right
            if col < total_cols - 1:
                for c in range(total_cols - col - 1):
                    if rows[row][col + c + 1] < current_val:
                        current_seen += 1
                    else:
                        multiplied *= (current_seen + 1)
                        max_seen = max(max_seen, multiplied)
                        current_seen = 0
                        break
                if (current_seen > 0):
                    multiplied *= current_seen
                    max_seen = max(max_seen, multiplied)
                    current_seen = 0

            # left

            # right

    return len(visible) if part == 1 else max_seen


print(solve(2, useExample=False))
# not 190
# not 121


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
