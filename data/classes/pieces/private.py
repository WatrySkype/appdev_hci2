import pygame
from data.classes.Piece import Piece

class Private(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_pvt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = 'pvt'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_pvt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
