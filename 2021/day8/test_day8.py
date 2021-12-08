import unittest

valid_digits = {}
valid_digits[0] = [1, 2, 3, 5, 6, 7]
valid_digits[1] = [3, 6]
valid_digits[2] = [1, 3, 4, 5, 7]
valid_digits[3] = [1, 3, 4, 6, 7]
valid_digits[4] = [2, 3, 4, 6]
valid_digits[5] = [1, 2, 4, 6, 7]
valid_digits[6] = [1, 2, 4, 5, 6, 7]
valid_digits[7] = [1, 3, 6]
valid_digits[8] = [1, 2, 3, 4, 5, 6, 7]
valid_digits[9] = [1, 2, 3, 4, 6, 7]


def part2(signals, displays):
    for i in range(len(signals)):
        signal = sorted(signals[i], key=lambda x: len(x))
        display = displays[i]

        possible_maps = {}
        for l in signal[0]:
            possible_maps[l] = valid_digits[1]

        letter = next(filter(lambda c: c not in signal[0], signal[1]))
        possible_maps[letter] = [1]

        letters = list(filter(lambda c: c not in signal[0], signal[2]))
        for l in letters:
            possible_maps[letter] = [2, 4]

        taken_letters = possible_maps.keys()

        for l in [c for c in signal[3:6] if c not in taken_letters]:
            possible_maps[l] = [5, 7]

        taken_pos = [1, 2, 3, 4, 5, 6, 7]

    pass


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    signals = []
    displays = []

    with open(filename) as openfileobject:
        for line in openfileobject:
            s, d = line.split('|')
            signals.append(s.split())
            displays.append(d.split())

    return part1(displays) if part == 1 else part2(signals, displays)


def part1(displays):
    cnt = 0
    for d in displays:
        cnt += len(list(filter(lambda i: len(i) in [2, 3, 4, 7], d)))
    return cnt


print(solve(1, False))


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
