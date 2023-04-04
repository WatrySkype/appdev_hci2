import pygame

class Piece:
    def __init__(self, pos, color, board):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.has_moved = False

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
                output.append([
                    board.get_square_from_pos(new_pos)
                ])
        return output
        
    def move(self, board, square, force=False):
        for i in board.squares:
            i.highlight = False
        if square in self.get_valid_moves(board) or force:
            prev_square = board.get_square_from_pos(self.pos)
            self.pos, self.x, self.y = square.pos, square.x, square.y
            prev_square.occupying_piece = None
            square.occupying_piece = self
            board.selected_piece = None
            self.has_moved = True
            return True
        else:
            board.selected_piece = None
            return False

    def attacking_squares(self, board):
        return self.get_moves(board)