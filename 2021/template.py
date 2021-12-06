import unittest


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    # TODO put solution here
    with open(filename) as openfileobject:
        for line in openfileobject:
            pass

    return None


print(solve(1, True))


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
