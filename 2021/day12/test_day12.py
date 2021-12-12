import unittest
from collections import defaultdict


def explore(explored_paths, no_go, twice_is_ok, all_paths):
    resulting_path = []

    for current_path in explored_paths:

        previous_cave = current_path[-1]
        if previous_cave == 'end':
            resulting_path.append(current_path)
            return resulting_path

        for possible in all_paths[previous_cave]:
            if possible == 'start':
                continue

            # (unnecessary) guard against infinite loop if two capital caves are connected
            if (previous_cave, possible) in no_go:
                continue

            new_path = list(current_path)
            new_path.append(possible)

            new_no_go = no_go.copy()

            if twice_is_ok:
                if ord(possible[0]) < 97 and ord(previous_cave[0]) < 97:
                    new_no_go.add((previous_cave, possible))
            else:
                new_no_go.add((previous_cave, possible))

            next_twice_is_ok = twice_is_ok
            if ord(possible[0]) >= 97 and current_path.count(possible) >= 1:
                if twice_is_ok:
                    next_twice_is_ok = False
                else:
                    continue

            new_found_paths = explore([new_path], new_no_go, next_twice_is_ok, all_paths)
            resulting_path.extend(new_found_paths)

    return resulting_path


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"
    all_paths = defaultdict(set)

    with open(filename) as openfileobject:
        for line in openfileobject:
            parts = line.strip().split('-')

            if parts[1] not in all_paths[parts[0]]:
                all_paths[parts[0]].add(parts[1])

            if parts[0] not in all_paths[parts[1]]:
                all_paths[parts[1]].add(parts[0])

    found_paths = explore([['start']], set(), part == 2, all_paths)

    #    for p in found_paths:
    #        print("|".join(p))

    return len(found_paths)


print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(3510, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(10, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(122880, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(36, solve(2, True), "Part 2 example")
