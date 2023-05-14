import pygame
from data.classes.Piece import Piece

class Sergeant(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_sgt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = 'Sgt'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_sgt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class SecondLt(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_2lt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = '2Lt'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_2lt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class FirstLt(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_1lt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = '1Lt'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_1lt.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class Captain(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_cap.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = 'Cap'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_cap.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class Major(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_maj.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = 'Maj'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_maj.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class LtColonel(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_ltcol.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = 'LtCol'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_ltcol.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class Colonel(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_col.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = 'Col'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_col.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class General1(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_1sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = '1sGen'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_1sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class General2(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_2sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = '2sGen'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_2sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class General3(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_3sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = '3sGen'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_3sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class General4(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_4sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = '4sGen'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_4sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))

class General5(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/img/' + self.color[0] + '_5sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
        self.notation = '5sGen'

    def default_img(self, board):
        img_path = 'data/img/' + self.color[0] + '_5sgen.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))