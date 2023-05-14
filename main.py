import pygame

from data.classes.Board import Board
from data.classes.SideMenu import SideMenu

pygame.init()

WINDOW_SIZE = (1260, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])
sidemenu = SideMenu(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	display.fill('white')
	board.draw(display)
	sidemenu.draw(display)
	pygame.display.update()


if __name__ == '__main__':
	running = True
	pygame.display.set_caption('Game of The Generals - rendered with PyGame')
	while running:
		mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			# Quit the game if the user presses the close button
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN: 
       			# If the mouse is clicked
				if event.button == 1:
					if mx < (WINDOW_SIZE[0]*2/3):
						board.handle_click(mx, my)

		if board.lose_condition('black'):	
			print('White wins!')
			running = False
		elif board.lose_condition('white'):
			print('Black wins!')
			running = False
		# Draw the board
		draw(screen)