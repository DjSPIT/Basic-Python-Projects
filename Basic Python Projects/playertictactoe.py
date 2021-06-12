import random


class Player:
    def __init__(self, letter):
        #  letter is X or O
        self.letter = letter

    #   Now all players need to get the next move in the game
    def get_move(self, game):
        pass


#   Now for the random computer player , we use inheritance
class RandomCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #   pass
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_sq = False
        val = None
        while not valid_sq:
            square = input(self.letter + '\'s turn --> Input move(0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_sq = True
            except ValueError:
                print("Invalid Square. Try again.")
        return val
