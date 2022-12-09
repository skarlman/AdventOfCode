def print_grid(rope):
    print()
    for row in range(11):
        print()
        for col in range(20):
            try:
                i = rope.index((row, col))
            except:
                i = -1
            if i == 0:
                i = "H"
            elif i == len(rope) - 1:
                i = "T"

            print(i if (row, col) in rope else ".", end="")

    print()


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    with open(filename) as openfileobject:
        lines = [l.strip().split(' ') for l in openfileobject.readlines()]

    rope_length = 2 if part == 1 else 10

    # (10,10) just to visualize the maze easier in print_grid()
    rope = [(10, 10)] * rope_length

    tail_visits = set()
    tail_visits.add(rope[-1])

    for (direction, steps) in lines:
        for _ in range(int(steps)):

            # move head...
            if direction == "R":
                rope[0] = (rope[0][0], rope[0][1] + 1)
            elif direction == "L":
                rope[0] = (rope[0][0], rope[0][1] - 1)
            elif direction == "U":
                rope[0] = (rope[0][0] - 1, rope[0][1])
            elif direction == "D":
                rope[0] = (rope[0][0] + 1, rope[0][1])

            # ...and the knots will follow
            for knot_i in range(1, len(rope)):
                row_d = rope[knot_i - 1][0] - rope[knot_i][0]
                col_d = rope[knot_i - 1][1] - rope[knot_i][1]

                if row_d != 0:
                    row_d -= 1 if row_d > 0 else -1

                if col_d != 0:
                    col_d -= 1 if col_d > 0 else -1

                if row_d or col_d:
                    rope[knot_i] = (rope[knot_i - 1][0] - row_d, rope[knot_i - 1][1] - col_d)

            tail_visits.add(rope[-1])

            # print_rope(rope)

    return len(tail_visits)


print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')
