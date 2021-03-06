from colorama import Fore


class Player:
    def __init__(self, player_number, game_board):
        self.number = player_number
        self.game_board = game_board

        index = player_number - 1
        self.colour = (Fore.RED, Fore.BLUE)[index]
        self.name = ('Red', 'Blue')[index]
        self.character = ('©', 'ø')[index]
        self.score = 2

    def make_move(self, graphics):
        raise NotImplementedError()

    @property
    def opponent(self):
        return self.game_board.players[2 - self.number]
