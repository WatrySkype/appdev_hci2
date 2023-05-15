import pygame
from data.classes.Logic import attack_check

class Piece:
	def __init__(self, pos, color, board):
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.color = color
		self.has_moved = False
		self.opponent_guess = ['5sGen', '4sGen', '3sGen', '2sGen', '1sGen',
			  'Col', 'LtCol', 'Maj', 'Cap', '1Lt', '2Lt',
			  'Sgt', 'pvt', 'pvt', 'pvt', 'pvt', 'pvt', 'pvt', 'spy', 'spy', 'flag']
		self.revealed = False

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
			if square.occupying_piece != None:
				if square.occupying_piece.color == prev_square.occupying_piece.color:
					return False
			winner = attack_check(board, self, square.occupying_piece)
			if winner == self:
				self.pos, self.x, self.y = square.pos, square.x, square.y
				square.occupying_piece = self
			elif winner == None:
				square.occupying_piece = None
			prev_square.occupying_piece = None
			if len(self.opponent_guess) <= 1:
				self.reveal()
			board.selected_piece = None
			self.has_moved = True
			board.player_ready = False
			return True
		else:
			board.selected_piece = None
			return False

	def attacking_squares(self, board):
		return self.get_moves(board)
	
	def default_img(self):
		pass

	def hide_img(self, board):
		img_path = 'data/img/' + self.color[0] + '.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height-20))
		
	def is_revealed(self):
		return self.revealed
		
	def reveal(self):
		self.revealed = True