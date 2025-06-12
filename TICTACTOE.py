import random

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

class TicTacToe:
    def __init__(self):
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = PLAYER_X

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def is_winner(self, player):
        # Check rows, columns, and diagonals
        for row in self.board:
            if all(s == player for s in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != EMPTY for row in self.board for cell in row)

    def ai_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == EMPTY]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = PLAYER_O

    def play(self):
        while True:
            self.print_board()
            if self.current_player == PLAYER_X:
                row, col = map(int, input("Enter your move (row and column): ").split())
                if self.board[row][col] != EMPTY:
                    print("Invalid move. Try again.")
                    continue
            else:
                self.ai_move()

            self.board[row][col] = self.current_player

            if self.is_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            if self.is_draw():
                self.print_board()
                print("It's a draw!")
                break

            self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X  # Switch player

if __name__ == "__main__":
    game = TicTacToe()
    game.play()