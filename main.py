#! /usr/bin/python3

import pygame
from pygame.locals import *
import sys
from Chess.Board import Board
from Chess.Constant import WIDTH, HEIGHT, SQUARE_SIZE

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Chess:

	def __get_row_col_from_pos(self, pos):
		x,y = pos
		row = y//SQUARE_SIZE
		col = x//SQUARE_SIZE
		return row, col

	def __main(self):
		board = Board(WIN)
		row, col = 0, 0
		while True:
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE ):
					pygame.quit()
					sys.exit()

				if event.type == MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					row, col = self.__get_row_col_from_pos(pos)
					board.select(row, col)

				if event.type == KEYDOWN:
					if event.key == K_r:
						board.reset()

			board.start()

	def run(self):
		print("Welcome To PyChess!!")
		print("Press 'R' to restart the game.")
		self.__main()


game = Chess()
game.run()
