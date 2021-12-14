import unittest
from collections import defaultdict


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    first_template = []
    lookup = dict()
    with open(filename) as openfileobject:
        for line in openfileobject:
            tline = line.strip()
            if len(tline) == 0:
                continue
            elif '->' in tline:
                s = tline.split(' -> ')
                lookup[s[0]] = s[1]
            else:
                first_template = tline

    template = defaultdict(int)

    counts = defaultdict(int)
    for i in range(len(first_template) - 1):
        counts[first_template[i]] += 1
        template[first_template[i:i + 2]] += 1
    counts[first_template[-1]] += 1

    for steps in range(40 if part == 2 else 10):
        remove_pairs = defaultdict(int)
        new_pairs = defaultdict(int)
        for k, v in template.items():
            if v == 0:
                continue

            new_letter = lookup[k]
            counts[new_letter] += v
            new_pairs[k[0] + new_letter] += v
            new_pairs[new_letter + k[1]] += v
            remove_pairs[k] += v

        for k, v in new_pairs.items():
            template[k] += v

        for k, v in remove_pairs.items():
            template[k] -= v

    least = min(counts.values())
    largest = max(counts.values())

    return largest - least


print(solve(1, False))
print(solve(2, False))


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
