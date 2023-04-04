import pygame
from data.classes.Piece import Piece

class Sergeant(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_sgt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = 'Sgt'

class SecondLt(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_2lt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = '2Lt'

class FirstLt(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_1lt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = '1Lt'

class Captain(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_cap.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = 'Cap'

class Major(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_maj.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = 'Maj'

class LtColonel(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_ltcol.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = 'LtCol'

class Colonel(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_col.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = 'Col'

class General1(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_1sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = '1sGen'

class General2(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_2sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = '2sGen'

class General3(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_3sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = '3sGen'

class General4(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_4sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = '4sGen'

class General5(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + color[0] + '_5sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width-20, board.tile_height-20))
        self.notation = '5sGen'