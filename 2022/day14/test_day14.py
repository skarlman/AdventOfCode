def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    with open(filename) as openfileobject:
        lines = openfileobject.readlines()

    grid = []

    # avoid multiple references to the same object
    max_x = 500 + 173  # the row-length in part 2 depends on the height (max_y)
    for rows in range(173):
        grid.append([])
        for cols in range(max_x):
            grid[-1].append(['.'])

    max_y = 0  # ok it is 171, but anyway...
    for row in lines:
        points = row.split(' -> ')
        for p_i in range(1, len(points)):
            p1_x, p1_y = [int(c) for c in points[p_i - 1].split(',')]
            p2_x, p2_y = [int(c) for c in points[p_i].split(',')]

            max_y = max(max(p1_y, p2_y), max_y)

            if p1_x != p2_x:
                for x in range(p1_x, p2_x + (p2_x - p1_x) // abs(p2_x - p1_x), (p2_x - p1_x) // abs(p2_x - p1_x)):
                    grid[p1_y][x] = '#'

            if p1_y != p2_y:
                for y in range(p1_y, p2_y + (p2_y - p1_y) // abs(p2_y - p1_y), (p2_y - p1_y) // abs(p2_y - p1_y)):
                    grid[y][p1_x] = '#'

    for floor_i in range(max_x):
        grid[max_y + 2][floor_i] = '#'

    units_of_sand = 0
    while True:
        is_at_rest = False
        units_of_sand += 1
        sand_x, sand_y = 500, 0

        while not is_at_rest:

            if grid[sand_y + 1][sand_x] not in ['o', '#']:
                sand_y += 1
            elif grid[sand_y + 1][sand_x - 1] not in ['o', '#']:
                # Go West
                sand_y += 1
                sand_x -= 1
            elif grid[sand_y + 1][sand_x + 1] not in ['o', '#']:
                sand_y += 1
                sand_x += 1
            else:
                grid[sand_y][sand_x] = 'o'
                is_at_rest = True

                if part == 2 and grid[0][500] == 'o':
                    break

            if part == 1 and sand_y == max_y:
                break

        if part == 1 and not is_at_rest:
            # If you are here; your sand is free-falling
            return units_of_sand - 1
        elif part == 2 and is_at_rest and grid[0][500] == 'o':
            return units_of_sand


print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')
