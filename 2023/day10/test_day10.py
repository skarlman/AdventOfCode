from collections import defaultdict, deque


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        grid = [l.strip() for l in openfileobject.readlines()]

        S_loc = None
        for row, line in enumerate(grid):
            s = line.find('S')
            if s > -1:
                S_loc = (row, s)
                break

        path = []
        path.append(S_loc)
        curr_loc = S_loc

        right_of_pipe = set()
        left_of_pipe = set()
        #print(path)

        if curr_loc[0] > 0 and grid[curr_loc[0]-1][curr_loc[1]] in ['|', 'F', '7']:
            #go up
            curr_loc = (curr_loc[0]-1, curr_loc[1])

        elif curr_loc[1] < len(grid[0]) and grid[curr_loc[0]][curr_loc[1]+1] in ['-', '7', 'J']:
            #go right
            curr_loc = (curr_loc[0], curr_loc[1]+1)

        elif curr_loc[0] < len(grid)-1 and grid[curr_loc[0]+1][curr_loc[1]] in ['|', 'J', 'L']:
            # go down
            curr_loc = (curr_loc[0]+1, curr_loc[1])

        elif curr_loc[1] > 0 and grid[curr_loc[0]][curr_loc[1] - 1] in ['-', 'L', 'F']:
            #go left
            curr_loc = (curr_loc[0], curr_loc[1] - 1)

        path.append(curr_loc)
        #print(path)
        while curr_loc != S_loc:
            if path[-2] != (curr_loc[0]-1, curr_loc[1]) and grid[curr_loc[0]][curr_loc[1]] in ['|', 'J', 'L'] and curr_loc[0] > 0 and grid[curr_loc[0] - 1][curr_loc[1]] in ['S','|', 'F', '7']:
                # go up
                curr_loc = (curr_loc[0] - 1, curr_loc[1])

                match grid[curr_loc[0]][curr_loc[1]]:
                    case '|':
                        right_of_pipe.add((curr_loc[0], curr_loc[1]+1))
                        left_of_pipe.add((curr_loc[0], curr_loc[1]-1))
                    case 'F':
                        right_of_pipe.add((curr_loc[0]+1, curr_loc[1] + 1))
                        left_of_pipe.add((curr_loc[0], curr_loc[1] - 1))
                        left_of_pipe.add((curr_loc[0]-1, curr_loc[1] - 1))
                        left_of_pipe.add((curr_loc[0]-1 , curr_loc[1]))
                    case '7':
                        right_of_pipe.add((curr_loc[0], curr_loc[1]+1))
                        right_of_pipe.add((curr_loc[0]-1, curr_loc[1]+1))
                        right_of_pipe.add((curr_loc[0]-1, curr_loc[1]))
                        left_of_pipe.add((curr_loc[0]+1, curr_loc[1]-1))

            elif path[-2] != (curr_loc[0], curr_loc[1]+1) and  grid[curr_loc[0]][curr_loc[1]] in ['-', 'L', 'F'] and curr_loc[1] < len(grid[0]) and grid[curr_loc[0]][curr_loc[1] + 1] in ['S','-', '7', 'J']:
                # go right
                curr_loc = (curr_loc[0], curr_loc[1] + 1)

                match grid[curr_loc[0]][curr_loc[1]]:
                    case '-':
                        right_of_pipe.add((curr_loc[0]+1, curr_loc[1]))
                        left_of_pipe.add((curr_loc[0]-1, curr_loc[1]))
                    case '7':
                        right_of_pipe.add((curr_loc[0]+1, curr_loc[1] - 1))
                        left_of_pipe.add((curr_loc[0]-1, curr_loc[1]))
                        left_of_pipe.add((curr_loc[0]-1, curr_loc[1] + 1))
                        left_of_pipe.add((curr_loc[0] , curr_loc[1]+1))
                    case 'J':
                        right_of_pipe.add((curr_loc[0]+1, curr_loc[1]))
                        right_of_pipe.add((curr_loc[0]+1, curr_loc[1]+1))
                        right_of_pipe.add((curr_loc[0], curr_loc[1]+1))
                        left_of_pipe.add((curr_loc[0]-1, curr_loc[1]-1))

            elif path[-2] != (curr_loc[0]+1, curr_loc[1]) and grid[curr_loc[0]][curr_loc[1]] in ['|', 'F', '7'] and curr_loc[0] < len(grid) - 1 and grid[curr_loc[0] + 1][curr_loc[1]] in ['S','|', 'J', 'L']:
                # go down
                curr_loc = (curr_loc[0] + 1, curr_loc[1])

                match grid[curr_loc[0]][curr_loc[1]]:
                    case '|':
                        right_of_pipe.add((curr_loc[0], curr_loc[1]-1))
                        left_of_pipe.add((curr_loc[0], curr_loc[1]+1))
                    case 'J':
                        right_of_pipe.add((curr_loc[0]-1, curr_loc[1] - 1))
                        left_of_pipe.add((curr_loc[0], curr_loc[1] + 1))
                        left_of_pipe.add((curr_loc[0]+1, curr_loc[1] + 1))
                        left_of_pipe.add((curr_loc[0]+1 , curr_loc[1]))
                    case 'L':
                        right_of_pipe.add((curr_loc[0], curr_loc[1]-1))
                        right_of_pipe.add((curr_loc[0]+1, curr_loc[1]-1))
                        right_of_pipe.add((curr_loc[0]+1, curr_loc[1]))
                        left_of_pipe.add((curr_loc[0]-1,curr_loc[1]+1))


            elif path[-2] != (curr_loc[0], curr_loc[1]-1) and grid[curr_loc[0]][curr_loc[1]] in ['-', 'J', '7'] and curr_loc[1] > 0 and grid[curr_loc[0]][curr_loc[1] - 1] in ['S','-', 'L', 'F']:
                # go left
                curr_loc = (curr_loc[0], curr_loc[1] - 1)

                match grid[curr_loc[0]][curr_loc[1]]:
                    case '-':
                        right_of_pipe.add((curr_loc[0]-1, curr_loc[1]))
                        left_of_pipe.add((curr_loc[0]+1, curr_loc[1]))
                    case 'L':
                        right_of_pipe.add((curr_loc[0]-1, curr_loc[1] + 1))
                        left_of_pipe.add((curr_loc[0]+1, curr_loc[1]))
                        left_of_pipe.add((curr_loc[0]+1, curr_loc[1] - 1))
                        left_of_pipe.add((curr_loc[0] , curr_loc[1]-1))
                    case 'F':
                        right_of_pipe.add((curr_loc[0]-1, curr_loc[1]))
                        right_of_pipe.add((curr_loc[0]-1, curr_loc[1]-1))
                        right_of_pipe.add((curr_loc[0], curr_loc[1]-1))
                        left_of_pipe.add((curr_loc[0]+1, curr_loc[1]+1))

            else:
                print("ERROR")
                exit(1)
            path.append(curr_loc)
            #print(path)

        #for r_i, line in enumerate(grid):
        #    for c_i, c in enumerate(line):
        #        coord = (r_i, c_i)
        #        if coord in path:
        #            print('o', end='')
        #        elif coord in right_of_pipe:
        #            print('R', end='')
        #        elif coord in left_of_pipe:
        #            print('L', end='')
        #    print()

        is_on_border =False
        q = list(right_of_pipe)
        while q:
            c = q.pop()
            if c[0] == 0 or c[0] == len(grid)-1:
                is_on_border = True
                continue
            if c[1] == 0 or c[1] == len(grid[0])-1:
                is_on_border = True
                continue

            coord = (c[0] - 1, c[1])
            if not (coord in path or coord in right_of_pipe) and not (coord[0] < 1 or coord[0] > len(grid)-2) and not (coord[1] < 1 or coord[1] > len(grid[0])-2):
                right_of_pipe.add(coord)
                q.append(coord)

            coord = (c[0], c[1]+1)
            if not (coord in path or coord in right_of_pipe) and not (coord[0] < 1 or coord[0] > len(grid)-2) and not (coord[1] < 1 or coord[1] > len(grid[0])-2):
                right_of_pipe.add(coord)
                q.append(coord)

            coord = (c[0]+1, c[1])
            if not (coord in path or coord in right_of_pipe) and not (coord[0] < 1 or coord[0] > len(grid)-2) and not (coord[1] < 1 or coord[1] > len(grid[0])-2):
                right_of_pipe.add(coord)
                q.append(coord)

            coord = (c[0], c[1]-1)
            if not (coord in path or coord in right_of_pipe) and not (coord[0] < 1 or coord[0] > len(grid)-2) and not (coord[1] < 1 or coord[1] > len(grid[0])-2):
                right_of_pipe.add(coord)
                q.append(coord)

        closed_right = len(right_of_pipe)

        is_on_border =False
        q = list(left_of_pipe)
        while q:
            c = q.pop()
            if c[0] < 1 or c[0] > len(grid)-2:
                is_on_border = True
                continue
            if c[1] <1 or c[1] > len(grid[0])-2:
                is_on_border = True
                continue

            coord = (c[0] - 1, c[1])
            if not (coord in path or coord in left_of_pipe) and not (coord[0] < 1 or coord[0] > len(grid)-2) and not (coord[1] < 1 or coord[1] > len(grid[0])-2):
                left_of_pipe.add(coord)
                q.append(coord)

            coord = (c[0], c[1]+1)
            if not (coord in path or coord in left_of_pipe) and not (coord[0] < 1 or coord[0] > len(grid)-2) and not (coord[1] < 1 or coord[1] > len(grid[0])-2):
                left_of_pipe.add(coord)
                q.append(coord)

            coord = (c[0]+1, c[1])
            if not (coord in path or coord in left_of_pipe) and not (coord[0] < 1 or coord[0] > len(grid)-2) and not (coord[1] < 1 or coord[1] > len(grid[0])-2):
                left_of_pipe.add(coord)
                q.append(coord)

            coord = (c[0], c[1]-1)
            if not (coord in path or coord in left_of_pipe) and not (coord[0] < 1 or coord[0] > len(grid)-2) and not (coord[1] < 1 or coord[1] > len(grid[0])-2):
                left_of_pipe.add(coord)
                q.append(coord)

        closed_left = len(left_of_pipe)

        print(f"Part 2 alt: Right: {closed_right}")
        print(f"Part 2 alt: Left: {closed_left}")


    return (len(path)-1)//2




print(f'Part 1: {solve(1, False)}')
#print(f'Part 2: {solve(2, False)}')
