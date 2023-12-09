import operator
from collections import defaultdict, deque


def get_next(ns, part):
    if all(v == 0 for v in ns):
        return 0
    else:
        diff = list(map(operator.sub, ns[1:], ns[:-1]))
        if part == 1:
            return get_next(diff, part) + ns[-1]
        else:
            return ns[0]-get_next(diff, part)

def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = openfileobject.readlines()

        for line in lines:
            ns = list(map(int, line.strip().split()))
            next_num = get_next(ns, part)
            score_part1 += next_num


    return score_part1




print(f'Part 1: {solve(2, False)}')
# print(f'Part 2: {solve(2, False)}')

