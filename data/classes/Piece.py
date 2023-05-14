import pygame
from data.classes.Logic import attack_check

class Piece:
    def __init__(self, pos, color, board):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.has_moved = False
        self.opponent_guess = list(range(15))

    def get_valid_moves(self, board):
        output = []
        moves = [
            (0,-1), # north
            (1, 0), # east
            (0, 1), # south
            (-1, 0) # west
        ]
        for move in moves:
            new_pos = (self.x + move[0], self.y + move[1])
            if (
                new_pos[0] < 9 and
                new_pos[0] >= 0 and 
                new_pos[1] < 8 and 
                new_pos[1] >= 0
            ):
                output.append(
                    board.get_square_from_pos(new_pos)
                )
        return output
        
    def move(self, board, square, force=False):
        for i in board.squares:
            i.highlight = False
        if square in self.get_valid_moves(board) or force:
            prev_square = board.get_square_from_pos(self.pos)
            winner = attack_check(prev_square.occupying_piece, square.occupying_piece)
            if winner == self:
                self.pos, self.x, self.y = square.pos, square.x, square.y
                square.occupying_piece = self
            prev_square.occupying_piece = None
            board.selected_piece = None
            self.has_moved = True
            return True
        else:
            board.selected_piece = None
            return False

    def attacking_squares(self, board):
        return self.get_moves(board)