

def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    with open(filename) as openfileobject:
        rows = [l.strip() for l in openfileobject.readlines()]

    visible = set()
    total_rows = len(rows)
    total_cols = len(rows[0])

    for row in range(total_rows):
        highest_from_left = rows[row][0]
        highest_from_right = rows[row][-1]
        for col_left in range(total_cols):
            col_right = total_cols - col_left - 1

            if col_left == 0:
                visible.add((row, col_left))
                visible.add((row, col_right))
            else:
                if rows[row][col_left] > highest_from_left:
                    visible.add((row, col_left))
                    highest_from_left = rows[row][col_left]

                if rows[row][col_right] > highest_from_right:
                    visible.add((row, col_right))
                    highest_from_right = rows[row][col_right]

    for col in range(total_rows):
        highest_from_top = rows[0][col]
        highest_from_bottom = rows[-1][col]

        for row_top in range(total_rows):
            row_bottom = total_rows - row_top - 1

            if row_top == 0:
                visible.add((row_top, col))
                visible.add((row_bottom, col))
            else:
                if rows[row_top][col] > highest_from_top:
                    visible.add((row_top, col))
                    highest_from_top = rows[row_top][col]

                if rows[row_bottom][col] > highest_from_bottom:
                    visible.add((row_bottom, col))
                    highest_from_bottom = rows[row_bottom][col]

    max_seen = 0
    for row in range(total_rows):
        if row == 0 or row == total_rows-1:
            continue

        for col_left in range(total_cols):
            if col_left == 0 or col_left == total_cols -1:
                continue

            multiplied = 1
            current_seen = 0
            current_height = rows[row][col_left]

            # up
            for r in range(row):
                if rows[row - r - 1][col_left] < current_height:
                    current_seen += 1
                else:
                    multiplied *= (current_seen + 1)
                    max_seen = max(max_seen, multiplied)
                    current_seen = 0
                    break

            if current_seen > 0:
                multiplied *= current_seen
                max_seen = max(max_seen, multiplied)
                current_seen = 0


            # down
            for r in range(total_rows - row - 1):
                if rows[row + r + 1][col_left] < current_height:
                    current_seen += 1
                else:
                    multiplied *= (current_seen + 1)
                    max_seen = max(max_seen, multiplied)
                    current_seen = 0
                    break

            if current_seen > 0:
                multiplied *= current_seen
                max_seen = max(max_seen, multiplied)
                current_seen = 0

            # left
            for c in range(col_left):
                if rows[row][col_left - c - 1] < current_height:
                    current_seen += 1
                else:
                    multiplied *= (current_seen + 1)
                    max_seen = max(max_seen, multiplied)
                    current_seen = 0
                    break

            if current_seen > 0:
                multiplied *= current_seen
                max_seen = max(max_seen, multiplied)
                current_seen = 0

            # right
            for c in range(total_cols - col_left - 1):
                if rows[row][col_left + c + 1] < current_height:
                    current_seen += 1
                else:
                    multiplied *= (current_seen + 1)
                    max_seen = max(max_seen, multiplied)
                    current_seen = 0
                    break

            if current_seen > 0:
                multiplied *= current_seen
                max_seen = max(max_seen, multiplied)
                current_seen = 0

    return len(visible) if part == 1 else max_seen


print(f'Part 1: {solve(1, useExample=False)}')
print(f'Part 2: {solve(2, useExample=False)}')
