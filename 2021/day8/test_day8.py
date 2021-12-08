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

possible_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def list_is_in_list(item, l):
    for i, v in l.items():
        if v == item:
            return True

    return False


def brute_it(maps, input_strings):
    all_perms = [[a, b, c, d, e, f, g] for a in maps['a']
                 for b in maps['b']
                 for c in maps['c']
                 for d in maps['d']
                 for e in maps['e']
                 for f in maps['f']
                 for g in maps['g']
                 ]

    for perm in all_perms:
        if not len(perm) == len(set(perm)):
            continue

        lookup = dict(zip(possible_letters, perm))
        # check all inputs

        if all([list_is_in_list(
                sorted([lookup[c] for c in single_input]), valid_digits) for single_input in input_strings]):
            return lookup

    return None


def part2(signals, displays):
    total_sum = 0

    for i in range(len(signals)):
        signal = sorted(signals[i], key=lambda x: len(x))
        display = displays[i]

        possible_maps = {}
        for l in signal[0]:
            possible_maps[l] = valid_digits[1]

        the_one_letter = next(filter(lambda c: c not in signal[0], signal[1]))
        possible_maps[the_one_letter] = [1]

        letters = list(filter(lambda c: c not in signal[0], signal[2]))
        for l in letters:
            possible_maps[l] = [2, 4, 5, 7]

        for ss in signal[3:6]:
            for c in ss:
                if c not in possible_maps:
                    possible_maps[c] = [2, 4, 5, 7]

        combination = brute_it(possible_maps, signal)

        codestr = ''
        for d in display:
            translated = sorted([combination[c] for c in d])
            codestr += f'{next(key for key, value in valid_digits.items() if value == translated)}'

        total_sum += int(codestr)
    return total_sum


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


print(solve(2, False))


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(521, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(26, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(1016804, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(61229, solve(2, True), "Part 2 example")
