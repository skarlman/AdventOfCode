import math
from collections import defaultdict, deque


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    coords_next_to_symbol = set()
    gear_next_to_coord = defaultdict(set)
    number_next_to_gear = defaultdict(list)

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = openfileobject.readlines()

        for (row, line) in enumerate(lines):
            line = line.strip()
            for (col, c) in enumerate(line):
                if (not c.isdigit()) and (not c == '.'):
                    coords_next_to_symbol.add((row, col - 1))
                    coords_next_to_symbol.add((row + 1, col - 1))
                    coords_next_to_symbol.add((row - 1, col - 1))
                    coords_next_to_symbol.add((row, col + 1))
                    coords_next_to_symbol.add((row + 1, col + 1))
                    coords_next_to_symbol.add((row - 1, col + 1))
                    coords_next_to_symbol.add((row + 1, col))
                    coords_next_to_symbol.add((row - 1, col))

                if c == '*':
                    gear_next_to_coord[(row, col - 1)].add((row, col))
                    gear_next_to_coord[(row + 1, col - 1)].add((row, col))
                    gear_next_to_coord[(row - 1, col - 1)].add((row, col))
                    gear_next_to_coord[(row, col + 1)].add((row, col))
                    gear_next_to_coord[(row + 1, col + 1)].add((row, col))
                    gear_next_to_coord[(row - 1, col + 1)].add((row, col))
                    gear_next_to_coord[(row + 1, col)].add((row, col))
                    gear_next_to_coord[(row - 1, col)].add((row, col))
        curr_number = ''
        is_adjacent_to_symbol = False
        adjacent_to_gears = set()
        score_part1 = 0
        for (row, line) in enumerate(lines):
            for (col, c) in enumerate(line):

                if c.isdigit():
                    curr_number += c
                    if (row, col) in coords_next_to_symbol:
                        is_adjacent_to_symbol = True
                    if (row, col) in gear_next_to_coord:
                        adjacent_to_gears.update(gear_next_to_coord[(row, col)])
                else:
                    if curr_number:
                        if is_adjacent_to_symbol:
                            score_part1 += int(curr_number)
                        if adjacent_to_gears:
                            for gear in adjacent_to_gears:
                                number_next_to_gear[gear].append(int(curr_number))

                    curr_number = ''
                    is_adjacent_to_symbol = False
                    adjacent_to_gears = set()

    if part == 1:
        return score_part1

    score_part2 = 0
    for gear_numbers in number_next_to_gear.values():
        if len(gear_numbers) == 2:
            score_part2 += math.prod(gear_numbers)
    return score_part2

print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')
