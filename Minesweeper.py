import random

def create_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Place mines randomly on the board
    for _ in range(mines):
        while True:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
            if board[row][col] != '*':
                board[row][col] = '*'
                break

    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

def count_adjacent_mines(board, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]) and board[row + i][col + j] == '*':
                count += 1
    return count

def reveal(board, revealed, row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True

    if board[row][col] == ' ':
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]):
                    reveal(board, revealed, row + i, col + j)

def main():
    rows, cols, mines = 8, 8, 10
    board = create_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    game_over = False

    while not game_over:
        print_board(revealed)

        try:
            row = int(input("Enter row (0-7): "))
            col = int(input("Enter column (0-7): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if not (0 <= row < rows and 0 <= col < cols):
            print("Invalid row or column. Please enter values within the range.")
            continue

        if revealed[row][col]:
            print("You've already revealed this cell.")
            continue

        if board[row][col] == '*':
            print("Game over! You hit a mine.")
            game_over = True
        else:
            adjacent_mines = count_adjacent_mines(board, row, col)
            revealed[row][col] = True

            if adjacent_mines == 0:
                reveal(board, revealed, row, col)
            else:
                print(f"There are {adjacent_mines} mines nearby.")

if __name__ == "__main__":
    main()
