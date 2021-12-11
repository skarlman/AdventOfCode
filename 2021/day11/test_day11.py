import unittest


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    grid = []
    with open(filename) as openfileobject:
        for line in openfileobject:
            grid.append([int(c) for c in line.strip()])

    max_col = len(grid[0])
    max_row = len(grid)

    total = 0

    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    steps = 100 if part == 1 else 1000

    for step in range(steps):
        will_flash = set()
        has_flashed = set()
        for r in range(max_row):
            for c in range(max_col):
                grid[r][c] += 1
                if grid[r][c] > 9:
                    will_flash.add((r, c))

        while True:
            if not will_flash:
                break

            curr = will_flash.pop()
            if curr in has_flashed:
                continue

            has_flashed.add(curr)
            total += 1

            r, c = curr

            # print(f'r: {r}, c: {c}')
            for d in range(8):
                rr = r + dr[d]
                cc = c + dc[d]
                # print(f'rr: {rr}, cc: {cc}')
                if 0 <= rr < max_row and 0 <= cc < max_col:
                    grid[rr][cc] += 1
                    if grid[rr][cc] not in has_flashed and grid[rr][cc] > 9:
                        will_flash.add((rr, cc))

        if part == 2 and len(has_flashed) == max_col * max_row:
            return step + 1

        for p in has_flashed:
            rrr, ccc = p
            grid[rrr][ccc] = 0

#        ss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#        if step-1 in ss:
#            print()
#            print(f"After step {step + 1}:")
#            for row in grid:
#                print("".join([str(c) for c in row]))

    return total


print(solve(2, False))


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(1673, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(1656, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(279, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(195, solve(2, True), "Part 2 example")
