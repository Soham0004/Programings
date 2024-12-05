def is_valid_sudoku(board):
    for row in board:
        if not is_valid_unit(row):
            return False
    for col in zip(*board):
        if not is_valid_unit(col):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(block):
                return False
    return True
def is_valid_unit(unit):
    seen = set()
    for num in unit:
        if num != '.':
            if num in seen:
                return False
            seen.add(num)
    return True
def get_sudoku_board():
    print("Enter the Sudoku board (9x9), row-wise. Use '.' for empty cells.")
    board = []
    for _ in range(9):
        row = input("Enter row: ").strip()
        board.append(list(row))
    return board
user_sudoku_board = get_sudoku_board()
if is_valid_sudoku(user_sudoku_board):
    print("The Sudoku is solved correctly.")
else:
    print("There is a mistake in the Sudoku solution.")
