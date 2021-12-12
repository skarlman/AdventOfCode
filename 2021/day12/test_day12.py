import unittest

all_paths = dict()
print()
print('--- new run ---')
print()

def explore(found_paths, nog_go, twice_ok):
    resuling_paths = []

    for current_path in found_paths:

        previousCave = current_path[-1]
        if previousCave == 'end':
            resuling_paths.append(current_path)
            continue
        for possible in all_paths[previousCave]:
            if possible == 'start':
                continue

            if (previousCave, possible) in nog_go:
                continue

            if not twice_ok and ord(possible[0]) >= 97 and current_path.count(possible) >= 1:
                continue

            next_twice_ok = twice_ok
            if ord(possible[0]) >= 97 and current_path.count(possible) == 1:
                if twice_ok:
                    next_twice_ok = False



            new_path = list(current_path)
            new_path.append(possible)

            new_no_go = nog_go.copy()

            if twice_ok:
                if ord(possible[0]) < 97 and ord(previousCave[0]) < 97:
                    new_no_go.add((previousCave, possible))
            else:
                new_no_go.add((previousCave, possible))

            new_found = explore([new_path], new_no_go, next_twice_ok)
            resuling_paths.extend(new_found)

    return resuling_paths


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    with open(filename) as openfileobject:
        for line in openfileobject:
            parts = line.strip().split('-')

            if parts[0] not in all_paths:
                all_paths[parts[0]] = set()

            if parts[1] not in all_paths[parts[0]]:
                all_paths[parts[0]].add(parts[1])

            if parts[1] not in all_paths:
                all_paths[parts[1]] = set()

            if parts[0] not in all_paths[parts[1]]:
                all_paths[parts[1]].add(parts[0])



    no_go = set()
    no_go.add(('start', '-1'))
    found_paths = explore([['start']], no_go, True)

#    for p in found_paths:
#        print("|".join(p))

    return len(found_paths)


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
