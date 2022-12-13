import json
from collections import defaultdict, deque


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        raw = openfileobject.read()
        #lines = openfileobject.readlines()

    chunks = raw.split('\n\n')

#If both values are integers, the lower integer should come first.
    # If the left integer is lower than the right integer, the inputs are in the right order.
    # If the left integer is higher than the right integer, the inputs are not in the right order.
    # Otherwise, the inputs are the same integer; continue checking the next part of the input.

# If both values are lists, compare the first value of each list, then the second value, and so on.
    # If the left list runs out of items first, the inputs are in the right order.
    # If the right list runs out of items first, the inputs are not in the right order.
    # If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.

# If exactly one value is an integer, convert the integer to a list which contains that integer as its only value,
    # then retry the comparison.
    # For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2);
    # the result is then found by instead comparing [0,0,0] and [2].


    for chunk in chunks:
        rows = [json.loads(r.strip()) for r in chunk.split()]


        print()
        print(rows[0])
        print(rows[1])


    return score_part1


print(f'Part 1: {solve(1, True)}')
# print(f'Part 2: {solve(2, False)}')
