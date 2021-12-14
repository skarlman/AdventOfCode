import unittest
from collections import defaultdict, Counter


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

    counts = Counter(first_template)
    template = Counter(["".join(x) for x in zip(first_template[:-1], first_template[1:])])

    for steps in range(40 if part == 2 else 10):
        updated_pairs = defaultdict(int)
        for k, v in template.items():
            if v == 0:
                continue

            new_letter = lookup[k]
            counts[new_letter] += v

            updated_pairs[k] -= v

            updated_pairs[k[0] + new_letter] += v
            updated_pairs[new_letter + k[1]] += v


        template.update(updated_pairs)

    ordered = counts.most_common()
    return ordered[0][1] - ordered[-1][1]


print(solve(1, False))
print(solve(2, False))


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(3048, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(1588, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(3288891573057, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(2188189693529, solve(2, True), "Part 2 example")
