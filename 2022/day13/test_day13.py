from collections import defaultdict, deque


def find_closing_bracket(s):
    opening_brackets = 0
    for i, c in enumerate(s):
        if c == '[':
            opening_brackets += 1
        elif c == "]":
            opening_brackets -= 1
            if opening_brackets == 0:
                return i

    return -1


def splitup(s):
    # [1],[2,3,4]
    if len(s) == 0:
        return []

    if s[0] == ',':
        s = s[1:]

    comma = s.find(',')
    bracket = s.find('[')

    if -1 < comma < bracket:
        parts = [s[:comma]] + splitup(s[comma:])
    elif -1 < bracket < comma:
        closing_bracket = find_closing_bracket(s)
        parts = splitup(s[bracket + 1:closing_bracket])

        if closing_bracket < len(s) -1:
            parts += [splitup(s[closing_bracket + 1:])]
    else:
        parts = s.split(',')
        if len(parts) == 1:
            parts = [parts]

    return parts


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = openfileobject.readlines()

#    s = "[[1],[2,3,4]]"
    s="[1,[2,[3,[4,[5,6,7]]]],8,9]"
    s = splitup(s[1:-1])

    print(s)

    return score_part1


print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')
