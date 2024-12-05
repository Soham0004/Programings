class MNKGame:
    def __init__(self, rows, cols, k):
        self.rows = rows
        self.cols = cols
        self.k = k
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.cols * 2 - 1))
    def make_move(self, row, col, player):
        if 0 <= row < self.rows and 0 <= col < self.cols and self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False
    def check_winner(self, row, col, player):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            count += self.count_direction(row, col, player, dr, dc)
            count += self.count_direction(row, col, player, -dr, -dc)
            if count >= self.k:
                return True
        return False
    def count_direction(self, row, col, player, dr, dc):
        count = 0
        r, c = row + dr, col + dc
        while 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == player:
            count += 1
            r += dr
            c += dc
        return count
def play_mnk_game():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    k = int(input("Enter the value of k: "))
    game = MNKGame(rows, cols, k)
    current_player = 'X'
    while True:
        game.display_board()
        row = int(input(f"Player {current_player}, enter the row: ")) - 1
        col = int(input(f"Player {current_player}, enter the column: ")) - 1
        if game.make_move(row, col, current_player):
            if game.check_winner(row, col, current_player):
                print(f"Player {current_player} wins!")
                game.display_board()
                break
            if ' ' not in [cell for row in game.board for cell in row]:
                print("It's a tie!")
                game.display_board()
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
if __name__ == "__main__":
    play_mnk_game()
