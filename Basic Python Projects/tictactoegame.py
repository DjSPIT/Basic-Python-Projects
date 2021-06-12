import time
from playertictactoe import HumanPlayer
from playertictactoe import RandomCompPlayer


class TicTacToe:
    def __init__(self):
        #   Single list to represent a 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keep track of winner

    def print_board(self):
        #   Index 0 1 2 --> first row and so on...
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print(" | " + " | ".join(row) + " | ")

    @staticmethod
    def print_board_num():
        #   0 | 1 | 2 ... etc
        number_board = [[str(i) for i in range(j * 3, ((j + 1) * 3))] for j in range(3)]
        for row in number_board:
            print(" | " + " | ".join(row) + " | ")

    def available_moves(self):
        #   return []
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def make_move(self, square, letter):
        #   If move is valid, return true and make the move else return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #   Check all possibilities
        row_index = square // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_index = square // 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def num_empty_sq(self):
        return self.board.count(" ")

    def empty_sq(self):
        return " " in self.board  # will return a boolean value


def play(game, x_play, o_play, print_game=True):
    if print_game:
        game.print_board_num()

    letter = 'X'
    while game.empty_sq():
        if letter == "O":
            square = o_play.get_move(game)
        else:
            square = x_play.get_move(game)

        #   Function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to {square}')
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    print(letter + " wins the game!!")
                return letter

            letter = "O" if letter == "X" else "X"  # Switching players
    if print_game:
        print("Its a Tie")

    #   To add a pause
    time.sleep(0.5)


if __name__ == '__main__':
    print("The Tic-Tac-Toe Board:")
    x_player = HumanPlayer("X")
    o_player = RandomCompPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
