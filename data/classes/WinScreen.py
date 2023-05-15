import pygame
from pygame.locals import *

class WinScreen:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.winner = None
		self.win_title = None
		self.win_subtext = None
		self.banner = None
		self.font_color = None
		self.font_title = pygame.font.SysFont('Arial',70)
		self.font_subtext = pygame.font.SysFont('Arial',40)
		self.title_render = None
		self.title_center = None
		self.subtext_render = None
		self.subtext_center = None

	def draw(self, display, winner):
		self.winner = winner
		self.win_title = 'White Wins!' if self.winner[0] == 'w' else 'Black Wins!'
		self.win_subtext = 'The opponent\'s flag is captured!' if self.winner[1] == '1' else 'Your flag has successfully crossed!'
		self.banner = 'white' if self.winner[0] == 'w' else 'black'
		self.font_color = (0,0,0) if self.winner[0] == 'w' else (255,255,255)
		display.fill(self.banner)
		self.title_render = self.font_title.render(self.win_title, True, self.font_color)
		self.title_center = self.title_render.get_rect(center=(self.width//2, self.height//2))
		self.subtext_render = self.font_subtext.render(self.win_subtext, True, self.font_color)
		self.subtext_center = self.subtext_render.get_rect(center=(self.width//2, self.height//2+100))
		display.blit(self.title_render, self.title_center)
		display.blit(self.subtext_render, self.subtext_center)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT or event.type == pygame.MOUSEBUTTONDOWN:
				pygame.quit()
				sys.exit()