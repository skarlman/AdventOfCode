import math
import sys
import unittest
from collections import defaultdict, deque


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    code = ""
    with open(filename) as openfileobject:
        for line in openfileobject:
            code = line.strip()

    target_x_min, target_x_max, target_y_min, target_y_max = [int(x) for x in
                                                              code[15:].replace("..", " ").replace(", y=", " ").split()]

    # x_min => = d^2+d-2*t_min-x = 0
    # x_max => target_x_max

    a = 1
    b = 1
    c = -2 * target_x_min
    #min_x_velocity = int((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
    min_x_velocity = 1
    #max_x_velocity = target_x_max
    max_x_velocity = target_x_max

    min_y_velocity = target_y_min
    max_y_velocity = abs(target_y_min) + 1
    max_y_reach = 0
    all_hits = []
    for x_velocity in range(min_x_velocity, max_x_velocity + 1):
        for y_velocity in range(min_y_velocity, max_y_velocity + 1):
            current_x, current_y = 0, 0
            current_x_velocity, current_y_velocity = x_velocity, y_velocity

            this_round_max_y = 0
            while current_x < target_x_max and current_y > target_y_min:
                current_x += current_x_velocity
                current_x_velocity -= 1
                current_x_velocity = max(0, current_x_velocity)

                current_y += current_y_velocity
                current_y_velocity -= 1

                this_round_max_y = max(this_round_max_y, current_y)

                if target_x_min <= current_x <= target_x_max and target_y_min <= current_y <= target_y_max:
                    # hit
                    max_y_reach = max(max_y_reach, this_round_max_y)
                    all_hits.append((x_velocity, y_velocity))
                    break

    return max_y_reach if part == 1 else len(set(all_hits))


part1 = solve(1, False)
part2 = solve(2, False)

print()
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
