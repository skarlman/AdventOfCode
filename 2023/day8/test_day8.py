import math
from collections import defaultdict, deque
from functools import reduce


def mylcm(arr):

    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l

def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    directions = {}
    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = openfileobject.readlines()

        lr = [1 if d == 'R' else 0 for d in lines[0].strip()]
        instructions = len(lr)
        for row in lines[2:]:
            target, left, right = row.strip().replace("=", "").replace("(", "").replace(")", "").replace(",", "").split()
            directions[target] = (left, right)

        if part == 1:
            return path_steps(directions, instructions, lr, 'AAA', part)

        current = [k for k in directions.keys() if k[-1] == 'A']
        ptr = 0
        steps = 0

        all_path_steps = [path_steps(directions,instructions, lr, c, part) for c in current]
        print(mylcm(all_path_steps))


    return -1


def path_steps(directions, instructions, lr, starting_point, part):
    current = starting_point
    ptr = 0
    steps = 0
    while current != "ZZZ" if part == 1 else current[-1] != 'Z':
        steps += 1
        current = directions[current][lr[ptr]]
        ptr += 1
        if ptr == instructions:
            ptr = 0
    return steps


print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')
