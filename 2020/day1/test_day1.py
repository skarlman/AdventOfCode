from collections import defaultdict, deque


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = openfileobject.readlines()

    for (i, line) in enumerate(lines):
        for (j, line2) in enumerate(lines[i:]):
            for (k, line3) in enumerate(lines[j:]):
                if int(line) + int(line2) + int(line3) == 2020:
                    score_part2 = int(line) * int(line2) * int(line3)
                    break
            if int(line) + int(line2) == 2020:
                score_part1 = int(line) * int(line2)
                break
        if score_part1 > 0:
            break



    return score_part2 if part == 2 else score_part1




print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')

