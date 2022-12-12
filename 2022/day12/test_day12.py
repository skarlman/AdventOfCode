import heapq


def get_height_of_char(c):
    if c == 'S':
        return ord('a')
    elif c == "E":
        return ord('z')
    else:
        return ord(c)


def get_neighbors(grid, current_pos):
    neighbors = []

    current_height = get_height_of_char(grid[current_pos[0]][current_pos[1]])

    if current_pos[0] > 0 and get_height_of_char(grid[current_pos[0] - 1][current_pos[1]]) <= current_height + 1:
        neighbors.append((current_pos[0] - 1, current_pos[1]))
    if current_pos[0] < len(grid) - 1 and get_height_of_char(
            grid[current_pos[0] + 1][current_pos[1]]) <= current_height + 1:
        neighbors.append((current_pos[0] + 1, current_pos[1]))
    if current_pos[1] > 0 and get_height_of_char(grid[current_pos[0]][current_pos[1] - 1]) <= current_height + 1:
        neighbors.append((current_pos[0], current_pos[1] - 1))
    if current_pos[1] < len(grid[0]) - 1 and get_height_of_char(
            grid[current_pos[0]][current_pos[1] + 1]) <= current_height + 1:
        neighbors.append((current_pos[0], current_pos[1] + 1))

    return neighbors


def priority_heuristic(goal, next):
    return abs(goal[0] - next[0]) + abs(goal[1] - next[1])


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    with open(filename) as openfileobject:
        lines = [l.strip() for l in openfileobject.readlines()]

    all_S = []
    E = (-1, -1)

    for row_index, row in enumerate(lines):
        for col_index, c in enumerate(row):
            if c == 'S':
                all_S.append((row_index, col_index))
            elif c == "E":
                E = (row_index, col_index)
            elif c == 'a':
                if part == 2:
                    all_S.append((row_index, col_index))

    min_steps = 1e9

    # a*
    for S in all_S:

        frontier = []
        heapq.heappush(frontier, (0, S))

        came_from = dict()
        cost_so_far = dict()

        came_from[S] = None
        cost_so_far[S] = 0

        final_steps = 0

        while frontier:
            current = frontier.pop(0)

            if current[1] == E:
                final_steps = cost_so_far[came_from[current[1]]] + 1
                break

            neighbors = get_neighbors(lines, current[1])

            for next_square in neighbors:
                new_cost = cost_so_far[current[1]] + 1

                if next_square not in cost_so_far or new_cost < cost_so_far[next_square]:
                    cost_so_far[next_square] = new_cost
                    priority = new_cost + priority_heuristic(E, next_square)

                    heapq.heappush(frontier, (priority, next_square))
                    came_from[next_square] = current[1]

        if final_steps > 0:  # not all starting points reaches the goal
            min_steps = min(min_steps, final_steps)

    return min_steps


print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')
