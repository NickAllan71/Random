import random

from Player import Player


class AIPlayer(Player):
    def __init__(self, player_number, game_board, delay_before_move=20):
        Player.__init__(self, player_number, game_board)
        self.delay_before_move = delay_before_move

    def make_move(self, graphics):
        graphics.wait_for_animation(self.delay_before_move)
        self.game_board.assess_board(self.number)
        best_move = random.choice(self.get_best_moves())
        self.game_board.try_to_make_move(best_move.location)
        graphics.update()
        graphics.animate_move(best_move)
        graphics.quit_if_user_wants()
        return best_move

    def get_move_score(self, move):
        move_score = self.get_location_score(move.location)
        for location in move.overturned:
            move_score += self.get_location_score(location)
        return move_score

    def get_location_score(self, location):
        x = location[0]
        y = location[1]
        if self.is_corner(x, y):
            return 20
        if self.is_edge_of_corner(x, y) and self.is_corner_unprotected(x, y):
            return -5
        if self.is_edge(x, y):
            return 10
        return 1

    def is_corner(self, x, y):
        return self.is_coordinate_an_edge(x) and self.is_coordinate_an_edge(y)

    def is_edge(self, x, y):
        if self.is_corner(x, y):
            return False
        return self.is_coordinate_an_edge(x) or self.is_coordinate_an_edge(y)

    @staticmethod
    def is_coordinate_an_edge(coordinate):
        return coordinate == 0 or coordinate == 7

    @staticmethod
    def is_edge_of_corner(x, y):
        return (x <= 1 or x >= 6) and (y <= 1 or y >= 6)

    def is_corner_unprotected(self, inner_corner_x, inner_corner_y):
        corner_x = self.get_edge_nearest(inner_corner_x)
        corner_y = self.get_edge_nearest(inner_corner_y)
        return self.game_board.get_player_at(corner_x, corner_y) != self.number

    @staticmethod
    def get_edge_nearest(coordinate):
        if coordinate < 4:
            return 0
        return 7

    def get_best_moves(self):
        best_move_score = None
        best_moves = []

        for key, move in self.game_board.moves.items():
            move_score = self.get_move_score(move)
            if best_move_score is None or move_score > best_move_score:
                best_move_score = move_score
                best_moves = [move]
            elif move_score == best_move_score:
                best_moves.append(move)

        return best_moves


