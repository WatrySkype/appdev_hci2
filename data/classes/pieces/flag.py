import pygame
from data.classes.Piece import Piece

class Flag(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_flag.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = 'flag'
