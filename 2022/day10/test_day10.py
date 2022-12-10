def print_char(cycles, reg_x):
    pixel_index = cycles % 40

    if pixel_index == 0:
        print()

    print('#' if reg_x - 1 <= pixel_index <= reg_x + 1 else ' ', end='')


def solve(use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    cycles = 0
    reg_x = 1

    x_values = []

    with open(filename) as openfileobject:
        lines = [l.strip() for l in openfileobject.readlines()]

    print()
    print("Part 2:")

    for row in lines:
        cmd = row.split(' ')

        print_char(cycles, reg_x)

        if cmd[0] == 'noop':
            x_values.append(reg_x)
            cycles += 1

        elif cmd[0] == 'addx':
            x_values.append(reg_x)
            cycles += 1

            print_char(cycles, reg_x)

            reg_x += int(cmd[1])
            x_values.append(reg_x)

            cycles += 1

    signal_strengths = (x_values[v - 2] * v for v in (range(20, 221, 40)))

    print()
    print()

    return sum(signal_strengths)


print(f'Part 1: {solve(False)}')
