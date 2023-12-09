from collections import defaultdict, deque, Counter
from functools import cmp_to_key


def points(c):
    if c == 'A':
        return 14
    if c == 'J':
        return 11 if globalpart == 1 else 1
    if c == 'Q':
        return 12
    if c == 'K':
        return 13
    if c == 'T':
        return 10
    return int(c)

globalpart = -1

def compare_higher_rank(hand1, hand2):
    h1_counts = sorted(list(Counter(hand1).values()), reverse=True)
    h2_counts = sorted(list(Counter(hand2).values()), reverse=True)

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
    if h1_counts[0] == 3 and h1_counts[1] == 2:
        if h2_counts[0] != 3 or h2_counts[1] != 2:
            return -1
    elif h2_counts[0] == 3 and h2_counts[1] == 2:
        if h1_counts[0] != 3 or h1_counts[1] != 2:
            return 1

    # three of a kind
    if h1_counts[0] == 3 and h1_counts[1] == 1:
        if h2_counts[0] != 3:
            return -1
    elif h2_counts[0] == 3 and h2_counts[1] == 1:
        if h1_counts[0] != 3:
            return 1

    #  two pair
    if h1_counts[0] == 2 and h1_counts[1] == 2:
        if h2_counts[0] != 2 or h2_counts[1] != 2:
            return -1
    elif h2_counts[0] == 2 and h2_counts[1] == 2:
        if h1_counts[0] != 2 or h1_counts[1] != 2:
            return 1

    # pair
    if len(h1_counts) == 4 and len(h2_counts) == 5:
        return -1
    if len(h2_counts) == 4 and len(h1_counts) == 5:
        return 1

    return 0


def apply_joker(hand):
    if globalpart == 1:
        return hand

    if not 'J' in hand:
        return hand

    



def comparer(hand1, hand2):

    higher_rank = compare_higher_rank(apply_joker(hand1[0]), apply_joker(hand2[0]))


    # if not len(h1_counts) == 5 and not len(h2_counts) == 5:
    #     print("ERROR")
    #     print(h1_counts)
    #     print(h2_counts)
    #     print(hand1)
    #     print(hand2)
    #     exit(1)
    if higher_rank == 0:
        for i in range(len(hand1[0])):
            if points(hand1[0][i]) > points(hand2[0][i]):
                return -1
            if points(hand1[0][i]) < points(hand2[0][i]):
                return 1
    else:
        return higher_rank

    return 0

def solve(use_example):
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



globalpart = 1
print(f'Part 1 ex: {solve(True)}')
print(f'Part 1 real: {solve(False)}')

globalpart = 2
print(f'Part 2 ex: {solve(True)}')
print(f'Part 2 real: {solve(False)}')

