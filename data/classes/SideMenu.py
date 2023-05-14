import pygame

class SideMenu:
	def __init__(self, width, height):
		self.width = 840
		self.height = 600
		self.rect = pygame.Rect(
			self.width,
			0,
			width,
			height
		)
		
		
	def draw(self, display):
		self.img = pygame.image.load('data/img/hqdefault.png')
		pygame.draw.rect(display, (125,127,113), self.rect)
		display.blit(self.img,(885, 10))
		