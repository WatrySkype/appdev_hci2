import pygame
from pygame.locals import *

class SideMenu:
	def __init__(self, width, height, board):
		self.width = 840
		self.height = 600
		self.rect = pygame.Rect(
			self.width,
			0,
			width,
			height
		)
		self.board = board
			  
	def score_board(self, turn):
		score = set({})
		pvt_count = 0
		spy_count = 0
		for piece in self.board.captured_pieces:
			if piece.color != self.board.turn:
				if piece.notation == 'pvt':
					pvt_count += 1
				if piece.notation == 'spy':
					spy_count += 1
				score.add(piece.notation)
		if 'pvt' in score:
			score.remove('pvt')
			score.add('pvt x'+str(pvt_count))
		if 'spy' in score:
			score.remove('spy')
			score.add('spy x'+str(spy_count))
		return score
		
		
	def handle_click(self, board, mx, my):
		x = mx
		y = my
		if 885<x<1235 and 150<y<200 and not board.player_ready:
			board.player_ready = True
		if board.selected_piece is not None and 885<x<1235 and 260<y<310:
			self.reveal_piece(board)
			
		
	def reveal_piece(self, board):
		piece = board.selected_piece
		if piece != None:
			piece.reveal()
			for i in board.squares:
				i.highlight = False
				i.highlight_other = False
			board.selected_piece.has_moved = True
			board.selected_piece = None
			if board.turn == 'white':
				board.turn = 'black'
			else:
				board.turn = 'white'
			board.player_ready = False
			
	def draw(self, display):
		if self.board.turn == 'white':
			menu_color = (255,255,255)
			button_color = (245,245,245)
			text_color = (0,0,0)
		else:
			menu_color = (0,0,0)
			button_color = (40,40,40)
			text_color = (255,255,255)
		#background
		pygame.draw.rect(display, menu_color, self.rect)
		self.img = pygame.image.load('data/img/hqdefault.png')
		display.blit(self.img,(885, 10))
		
		Turn_display = Button(885, 150, 350,50)
		pygame.draw.rect(display, button_color, Turn_display.rect)
		if self.board.player_ready:
			Turn_display.updateText(display, self.board.turn.capitalize()+'\'s Turn', text_color)
		else:
			Turn_display.updateText(display, self.board.turn.capitalize()+'\'s Turn - Start Your Turn', text_color)
		if self.board.selected_piece is not None:
			help_button = Button(885, 205, 350,50)
			pygame.draw.rect(display, button_color, help_button.rect)
			help_button.updateText(display, self.board.selected_piece.notation, text_color)
		if self.board.selected_piece is not None:
			if self.board.selected_piece.color == self.board.turn:
				reveal_button = Button(885, 260, 350,50)
				pygame.draw.rect(display, button_color, reveal_button.rect)
				reveal_button.updateText(display, 'Reveal (Warning! Skips Turn)', text_color)
				
		textw = TextWindow()
		pygame.draw.rect(display, button_color, textw.rect)
		if self.board.selected_opponent is not None:
			textw.updateTitle(display, text_color, 'Opponent\'s piece might be:')
			middle = len(set(self.board.selected_opponent.opponent_guess)) // 2
			textw.setText(display, text_color, list(set(self.board.selected_opponent.opponent_guess))[:middle+1])
			textw.setText2(display, text_color, list(set(self.board.selected_opponent.opponent_guess))[middle+1:])
		else:
			textw.updateTitle(display, text_color)
			middle = len(self.score_board(self.board.turn)) // 2
			textw.setText(display, text_color, list(self.score_board(self.board.turn))[:middle+1])
			textw.setText2(display, text_color, list(self.score_board(self.board.turn))[middle+1:])
class Button:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = pygame.Rect(
			x,
			y,
			width,
			height
		)
		self.font = pygame.font.SysFont('Arial',25)
		self.enabled = False
		self.text = ''
		
	def updateText(self, display, text, color):
		new_text = self.font.render(text, True, color)
		display.blit(new_text, (self.x+20,self.y+7))
		
class TextWindow:
	def __init__(self):
		self.x = 850
		self.y = 350
		self.width = 395
		self.height = 235
		self.rect = pygame.Rect(
			self.x,
			self.y,
			self.width,
			self.height
		)
		self.font_title = pygame.font.SysFont('Arial',25)
		self.font_body = pygame.font.SysFont('Arial',22)
	
	def updateTitle(self, display, color, title='Captured Pieces:'):
		display.blit(self.font_title.render(title, True, color), (self.x,self.y-30))
		
	def setText(self, display, color, text):
		for i, l in enumerate(text):
			display.blit(self.font_body.render(l, True, color), (self.x + 10, self.y + 18*i))
			
	def setText2(self, display, color, text):
		for i, l in enumerate(text):
			display.blit(self.font_body.render(l, True, color), (self.x + 200, self.y + 18*i))
		
	