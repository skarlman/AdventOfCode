import math
from collections import defaultdict, deque
from math import ceil


def quadratic(a, b, c):
    return (-b + (b**2 - 4*a*c)**0.5) / (2*a), (-b - (b**2 - 4*a*c)**0.5) / (2*a)

def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = openfileobject.readlines()

    if part == 1:
        times = [int(x.strip()) for x in lines[0].split()[1:]]
        distances = [int(x.strip()) for x in lines[1].split()[1:]]

    if part == 2:
        times =[ int(lines[0].replace(' ', '').split(':')[1]) ]
        distances = [int(lines[1].replace(' ', '').split(':')[1])]

    print(times)
    print(distances)

    race_ways = []
    for race in range(len(times)):
        sols = sorted([x for x in quadratic(1, -times[race], distances[race]+1)])
        sols[0] = math.ceil(sols[0])
        sols[1] = math.floor(sols[1])
        race_ways.append(sols[1]-sols[0]+1)

    score_part1 = math.prod(race_ways)
    return score_part1




print(f'Part 1: {solve(2, False)}')
# print(f'Part 2: {solve(2, False)}')

