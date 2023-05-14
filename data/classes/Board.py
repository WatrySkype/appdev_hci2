import pygame
from data.classes.Square import Square
from data.classes.Random import randomize_board
from data.classes.pieces.ranked import *
from data.classes.pieces.flag import Flag
from data.classes.pieces.spy import Spy
from data.classes.pieces.private import Private
from data.classes.Logic import get_rank

class Board:
    def __init__(self, width, height):
        self.width = (width*2/3)
        self.height = height
        self.tile_width = (width*2/3) // 9
        self.tile_height = height // 8
        self.selected_piece = None
        self.turn = 'white'
        self.config = randomize_board()
        self.squares = self.generate_squares()
        self.setup_board()

    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square

    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece
    
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_from_pos((x, y))
                    color = 'white' if piece[0] == 'w' else 'black'
                    match piece.strip('wb'):
                        case '5sGen':
                            square.occupying_piece = General5((x, y), color, self)
                        case '4sGen':
                            square.occupying_piece = General4((x, y), color, self)
                        case '3sGen':
                            square.occupying_piece = General3((x, y), color, self)
                        case '2sGen':
                            square.occupying_piece = General2((x, y), color, self)
                        case '1sGen':
                            square.occupying_piece = General1((x, y), color, self)
                        case 'Col':
                            square.occupying_piece = Colonel((x, y), color, self)
                        case 'LtCol':
                            square.occupying_piece = LtColonel((x, y), color, self)
                        case 'Maj':
                            square.occupying_piece = Major((x, y), color, self)
                        case 'Cap':
                            square.occupying_piece = Captain((x, y), color, self)
                        case '1Lt':
                            square.occupying_piece = FirstLt((x, y), color, self)
                        case '2Lt':
                            square.occupying_piece = SecondLt((x, y), color, self)
                        case 'Sgt':
                            square.occupying_piece = Sergeant((x, y), color, self)
                        case 'pvt':
                            square.occupying_piece = Private((x, y), color, self)
                        case 'spy':
                            square.occupying_piece = Spy((x, y), color, self)
                        case 'flag':
                            square.occupying_piece = Flag((x, y), color, self)
                        case _:
                            square.occupying_piece = None
    
    def handle_click(self, mx, my):
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))
        if self.selected_piece is None:
            if clicked_square.occupying_piece is not None:
                if clicked_square.occupying_piece.color == self.turn:
                    self.selected_piece = clicked_square.occupying_piece
                else:
                    #user clicks opponent piece to see possible ranks of that piece
                    for x in clicked_square.occupying_piece.opponent_guess:
                        print(get_rank(x))
                    print('actual: '+clicked_square.occupying_piece.notation)
        elif self.selected_piece.move(self, clicked_square):
            self.turn = 'white' if self.turn == 'black' else 'black'
        elif clicked_square.occupying_piece is not None:
            if clicked_square.occupying_piece.color == self.turn:
                self.selected_piece = clicked_square.occupying_piece
    
    def generate_squares(self):
        output = []
        for y in range(8):
            for x in range(9):
                output.append(
                    Square(x,  y, self.tile_width, self.tile_height)
                )
        return output
    
    def lose_condition(self, color):
        output = False
        flag = None
        for piece in [i.occupying_piece for i in self.squares]:
            if piece != None:
                if piece.notation == 'flag' and piece.color == color:
                    flag = piece
        if flag == None:
            output = True
        return output
    
    def draw(self, display):
        if self.selected_piece is not None:
            self.get_square_from_pos(self.selected_piece.pos).highlight = True
            for square in self.selected_piece.get_valid_moves(self):
                square.highlight = True
        for square in self.squares:
            if square.occupying_piece != None:
                if self.turn == 'white':
                    if square.occupying_piece.color == 'white':
                        square.occupying_piece.default_img(self)
                    elif square.occupying_piece.color == 'black':
                        square.occupying_piece.hide_img(self)
                else:
                    if square.occupying_piece.color == 'white':
                        square.occupying_piece.hide_img(self)
                    elif square.occupying_piece.color == 'black':
                        square.occupying_piece.default_img(self)
            square.draw(display)
    