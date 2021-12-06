filename = "input.txt"
# filename = "testinput.txt"


def check_win(marked_board, board, row, col):
    if all(marked_board[row]) or all(map(lambda x: x[col], marked_board)):
        # win
        # calc numbers
        total = 0
        for row in range(5):
            total += sum(int(x) for i, x in enumerate(board[row]) if not marked_board[row][i])

        return total

    return 0


def find_winner():
    number_of_boards = len(boards)
    boards_left = number_of_boards
    board_won = [False] * number_of_boards

    for n in numbers:
        for b_i in range(number_of_boards):
            board = boards[b_i]
            for b_r in range(len(board[0])):
                if n in board[b_r]:
                    col = board[b_r].index(n)
                    marked_boards[b_i][b_r][col] = True
                    winner = check_win(marked_boards[b_i], board, b_r, col)
                    if winner != 0:
                        if not board_won[b_i]:
                            boards_left -= 1
                            board_won[b_i] = True
                        if boards_left == 0:
                            return winner * int(n)
                    break


numbers = []
boards = []
marked_boards = []

current_board = []

with open(filename) as openfileobject:
    for line in openfileobject:
        if not numbers:
            numbers = line.split(',')
            continue

        if line == '\n':
            if len(current_board) == 5:
                boards.append(current_board)
                current_board = []
                marked_boards.append([[False] * 5 for i in range(5)])
        else:
            current_board.append(line.split())

if len(current_board) == 5:
    boards.append(current_board)
    current_board = []
    marked_boards.append([[False] * 5 for i in range(5)])

result = find_winner()

print(result)
