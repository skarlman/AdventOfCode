from collections import defaultdict, deque, Counter
from functools import cmp_to_key


def points(c):
    if c == 'A':
        return 14
    if c == 'J':
        return 11
    if c == 'Q':
        return 12
    if c == 'K':
        return 13
    if c == 'T':
        return 10
    return int(c)

def comparer(hand1, hand2):


    h1_counts = sorted(list(Counter(hand1[0]).values()), reverse=True)
    h2_counts = sorted(list(Counter(hand2[0]).values()), reverse=True)

    # five of a kind
    if h1_counts[0] == 5 and h2_counts[0] < 5:
        return -1
    if h2_counts[0] == 5 and h1_counts[0] < 5:
        return 1

    # four of a kind
    if h1_counts[0] == 4 and h2_counts[0] < 4:
        return -1
    if h2_counts[0] == 4 and h1_counts[0] < 4:
        return 1

    # full house
    if len(h1_counts) == 2 and len(h2_counts) > 2:
        return -1
    if len(h2_counts) == 2 and len(h1_counts) > 2:
        return 1

    # three of a kind
    if h1_counts[0] == 3 and h2_counts[0] < 3:
        return -1
    if h2_counts[0] == 3 and h1_counts[0] < 3:
        return 1

    #  two pair
    if len(h1_counts) == 3 and h1_counts[0] == 2 and (len(h2_counts) != 3 and h2_counts[0] != 2):
        return -1
    if len(h2_counts) == 3 and h2_counts[0] == 2 and (len(h1_counts) != 3 and h1_counts[0] != 2):
        return 1

    # pair
    if len(h1_counts) == 4 and len(h2_counts) == 5:
        return -1
    if len(h2_counts) == 4 and len(h1_counts) == 5:
        return 1

    # if not len(h1_counts) == 5 and not len(h2_counts) == 5:
    #     print("ERROR")
    #     print(h1_counts)
    #     print(h2_counts)
    #     print(hand1)
    #     print(hand2)
    #     exit(1)

    for i in range(len(hand1[0])):
        if points(hand1[0][i]) > points(hand2[0][i]):
            return -1
        if points(hand1[0][i]) < points(hand2[0][i]):
            return 1

    return 0

def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"


    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = [x.strip().split() for x in openfileobject.readlines()]

        ranked_lines = sorted(lines, key=cmp_to_key(comparer), reverse=True)

    # print (ranked_lines)

    for (i, hand) in enumerate(ranked_lines):
        score_part1 += int(hand[1])*(i+1)

    return score_part1




print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, True)}')

