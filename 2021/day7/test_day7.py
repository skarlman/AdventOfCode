import unittest


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    numbers = []
    with open(filename) as openfileobject:
        for line in openfileobject:
            if not numbers:
                numbers = [int(x) for x in line.split(',')]

    numbers.sort()

    positions = [0] * (numbers[-1] + 1)

    left = [0] * (numbers[-1] + 1)
    right = [0] * (numbers[-1] + 1)

    for n in numbers:
        positions[n] += 1

    for i in range(1, numbers[-1] +1, 1):
        j = numbers[-1] - i

        if part == 1:
            left[i] = left[i - 1] + sum(positions[0:i])
            right[j] = right[j + 1] + sum(positions[j+1:])
        else:
            left[i] = left[i-1]+sum((x * (i - ndx) for ndx, x in enumerate(positions[0:i])))

            ens = list(enumerate(positions[j + 1:]))

            right[j] = right[j+1] + sum( x * (ndx+1) for ndx, x in ens)

    lowest = 100000000000
    for i in range(numbers[-1]):
        c = left[i] + right[i]
        if lowest >= c:
            lowest = c
        else:
            return lowest

    return None


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
