import random
import re


# Lets create a board object
# noinspection PyTypeChecker
class Board:
    def __init__(self, dimension, mines):
        # keeping track of these parameters
        self.dimension = dimension
        self.mines = mines

        # Create a board
        self.board = self.make_new_board()  # plant the mines here
        self.assign_vals()
        # Initialize a set to keep track of users location {row, col} tuple
        self.dug = set()

    def make_new_board(self):
        # Construct a new board based on dimension and mines
        # Constructing a list of lists
        board = [[None for _ in range(self.dimension)] for _ in range(self.dimension)]
        mines_planted = 0
        while mines_planted < self.mines:
            loc = random.randint(0, self.dimension ** 2 - 1)
            row = loc // self.dimension
            col = loc % self.dimension

            if board[row][col] == "*":
                # Already mine is planted and therefore we keep going
                continue
            board[row][col] = "*"
            mines_planted += 1
        return board

    def get_num_mines_near(self, row, col):
        # Iterating to each neighbouring position
        # top_l = (row-1, col-1)
        # top_m = (row-1, col)
        # top_r = (row-1, col+1)
        # l = (row, col-1)
        # r = (row, col+1)
        # bottom_l = (row+1, col-1)
        # bottom_m = (row+1, col)
        # bottom_r = (row+1, col+1)

        # Make sure we don't go out of bounds
        num_mines_near = 0
        # Min and Max are defined so that we remain in the range of 0 to dimension size - 1
        for r in range(max(0, row - 1), min(self.dimension - 1, (row + 1) + 1)):
            for c in range(max(0, col - 1), min(self.dimension - 1, (col + 1) + 1)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == "*":
                    num_mines_near += 1
        return num_mines_near

    def assign_vals(self):
        for r in range(self.dimension):
            for c in range(self.dimension):
                if self.board[r][c] == "*":
                    continue
                #  This function will give the number of mines surrounding the number
                else:
                    self.board[r][c] = self.get_num_mines_near(r, c)

    def dig_board(self, row, col):
        #         If successful, return True else False
        # 1 -> hit a mine -> game over
        # 2 -> dig the location with neighbouring mines -> Victory
        # 3 -> no neighbouring mines -> dig neighbours recursively
        self.dug.add((row, col))  # keep track of dug

        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dimension - 1, (row + 1) + 1)):
            for c in range(max(0, col - 1), min(self.dimension - 1, (col + 1) + 1)):
                if (r, c) in self.dug:
                    continue
                self.dig_board(r, c)
        return True

    def __str__(self):
        # This function prints out whatever the function returns
        # We need to return a string that shows a board to the player
        visible_board = [[None for _ in range(self.dimension)] for _ in range(self.dimension)]
        for row in range(self.dimension):
            for col in range(self.dimension):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "

        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dimension):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))
        # print the csv strings
        indices = [i for i in range(self.dimension)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            form = '%-' + str(widths[idx]) + "s"
            cells.append(form % col)
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                form = '%-' + str(widths[idx]) + "s"
                cells.append(form % col)
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dimension)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len
        return string_rep


# Play function for the game
def play():
    print("Enter the dimension of your board: ")
    dimension = int(input())
    print("Enter the mines you want to place in your board: ")
    mines = int(input())
    # Create a board and plant the mines
    board = Board(dimension, mines)

    # Show the board to the user and ask the location
    # If location has a mine, game over
    # If location is not a mine, dig another square recursively
    # repeat the steps until all locations are cleared and therefore victory
    safe_loc = True

    while len(board.dug) < board.dimension ** 2 - mines:
        print(board)
        # Regex split -> match any part of the string and split it
        user = re.split(',(\\s)*', input("Where do you want to dig? (row, column): "))
        row, col = int(user[0]), int(user[-1])
        if row < 0 or row >= board.dimension or col < 0 or col >= dimension:
            print("\nInvalid Input, Try Again!!")
            continue

        safe_loc = board.dig_board(row, col)
        if not safe_loc:
            break

    if safe_loc:
        print("\nYou have won!! All clear")
    else:
        print("\nGame Over!! You landed on a mine")
        # Now we can reveal the whole board
        board.dug = [(r, c) for r in range(board.dimension) for c in range(board.dimension)]
        print(board)


if __name__ == '__main__':
    play()
