import pygame
import sys
from pygame.locals import *

from data.classes.Board import Board
from data.classes.SideMenu import SideMenu
from data.classes.WinScreen import WinScreen

pygame.init()

WINDOW_SIZE = (1260, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])
sidemenu = SideMenu(WINDOW_SIZE[0], WINDOW_SIZE[1], board)
winscreen = WinScreen(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	display.fill('white')
	board.draw(display)
	sidemenu.draw(display)
	pygame.display.update()

if __name__ == '__main__':
	running = True
	winner = None
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
					else:
						sidemenu.handle_click(board, mx, my)
						
		
		if board.flag_captured('black'):	
			print('White wins!')
			winner = 'w1'
			running = False
			winscreen.draw(screen, winner)
		elif board.flag_captured('white'):
			print('Black wins!')
			winner = 'b1'
			running = False
			winscreen.draw(screen, winner)
		elif board.flag_crossed('black') and board.flag_search('black').is_revealed():
			print('Black wins!')
			winner = 'b2'
			running = False
			winscreen.draw(screen, winner)
		elif board.flag_crossed('white') and board.flag_search('white').is_revealed():
			print('White wins!')
			winner = 'w2'
			running = False
			winscreen.draw(screen, winner)
		# Draw the board
		draw(screen)
