from collections import defaultdict


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    dirs = defaultdict(int)

    with open(filename) as openfileobject:
        lines = [l.strip() for l in openfileobject.readlines()]

    current_path = ''

    for row in lines[1:]:

        if row[0] == '$':
            if row[0:4] == '$ cd':
                if row[5:7] == '..':
                    current_path = "/".join(current_path.split("/")[:-1])
                    dirs[current_path] += 0
                else:
                    current_path = "/".join(current_path.split("/") + [row[5:]])
                    dirs[current_path] += 0
            elif row[0:4] == '$ ls':
                pass

        elif row[0:3] == 'dir':
            pass
        else:
            dirs[current_path] += int(row.split()[0])

    sorted_dirs = sorted(dirs.items(), key=lambda k: k[0].count('/'), reverse=True)
    summed = defaultdict(int)

    for key, val in sorted_dirs:
        paths = key.split('/')

        current_path = "/".join(paths[:len(paths)])
        summed[current_path] += val

        if current_path != '':
            parent_path = "/".join(paths[:len(paths) - 1])
            summed[parent_path] += summed[current_path]

    needed = 30000000 - (70000000 - summed[""])

    part1 = sum(val for val in summed.values() if val <= 100000)
    part2 = min(val for val in summed.values() if val >= needed)

    if part == 1:
        return part1

    if part == 2:
        return part2


print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')
