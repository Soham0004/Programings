import random
def place_o(board):
    """Places an 'O' in a random empty spot on the board."""
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    if not empty_spots:
        return False
    i, j = random.choice(empty_spots)
    board[i][j] = 2
    return True
def check_win(board):
    """Checks if there is a winner on the board (either 'X' or 'O')."""
    for i in range(3):
        if all(board[i][j] == board[i][0] for j in range(3)) and board[i][0] != 0:
            return True
        if all(board[j][i] == board[0][i] for j in range(3)) and board[0][i] != 0:
            return True
    if all(board[i][i] == board[0][0] for i in range(3)) and board[0][0] != 0:
        return True
    if all(board[i][2 - i] == board[0][2] for i in range(3)) and board[0][2] != 0:
        return True
    return False
board = [[0 for _ in range(3)] for _ in range(3)]
while True:
    row = int(input("Enter the row for your X (0, 1, or 2): "))
    col = int(input("Enter the column for your X (0, 1, or 2): "))
    board[row][col] = 1
    if check_win(board):
        print("You win!")
        break
    if not place_o(board):
        print("It's a tie!")
        break
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print()
