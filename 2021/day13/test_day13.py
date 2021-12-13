import unittest
from collections import defaultdict, deque


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    points = set()
    instructions = []

    max_x = 0
    max_y = 0

    with open(filename) as openfileobject:
        sec1 = True
        for line in openfileobject:
            tline = line.strip()
            if not tline:
                sec1 = False
                continue

            if sec1:
                split_ = tline.split(',')
                points.add((int(split_[0]), int(split_[1])))
            else:
                instructions.append(tline)

    collisions = 0
    for inst in instructions:
        parts = inst.split('=')
        fold = int(parts[1])
        direction = parts[0][-1]

        moved_ps = []
        removed_ps = []
        for x, y in points:
            if direction == 'y':
                if y > fold:
                    moved_ps.append((x, fold - (y - fold)))
                    removed_ps.append((x, y))
            if direction == 'x':
                if x > fold:
                    moved_ps.append((fold - (x - fold), y))
                    removed_ps.append((x, y))

        points.difference_update(removed_ps)
        points.update(moved_ps)

    if part == 1:
        return len(points)

    max_x = 0
    max_y = 0

    for p in points:
        max_x = max(p[0], max_x)
        max_y = max(p[1], max_y)

    grid = []
    for x in range(max_x + 1):
        grid.append([' '] * (max_y + 1))

    for x, y in points:
        grid[x][y] = '*'

    grid = [*zip(*grid)]

    print("Part 2:")
    print()
    for r in grid:
        print("".join([str(c) for c in r]))

    return len(points)

print("Part 1")
print(solve(1, False))
print()
solve(2, False)


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(99, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(16, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(99, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(16, solve(2, True), "Part 2 example")
