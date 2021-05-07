import pygame
from .Constant import ROWS, COLS, WHITE, BLACK, SQUARE_SIZE, BLACK_BISHOP, GREY, GREEN, WINNER_FONT, WIDTH, HEIGHT, FONT, RED
from .Pieces import Piece
from .Pawn import Pawn
from .Rook import Rook
from .Bishop import Bishop
from .King import King
from .Knight import Knight
from .Queen import Queen
import time
import random


class Board:
	def __init__(self, win):
		self.win = win
		self.board = []
		self.valid_moves = {}
		self.selected = None
		self.selected_row = self.selected_col = 0
		self.turn = None
		self.winner = None
		self.generate_random_turn()
		self.__create_board()

	def __init(self):
		"""
			Reset the game after someone loses.
		"""
		
		self.selected = None
		self.selected_row = self.selected_col = 0
		self.turn = WHITE
		self.winner = None
		self.valid_moves = {}
		self.__create_board()

	def reset(self):
		self.__init()

	def start(self):
		"""
			It will start the draw method which will draw everything.
		"""
		
		self.draw()
		pygame.display.update()
		if self.winner:
			time.sleep(2)
			self.__init()

	def __create_board(self):
		"""
			Create the board, like it will make board of 8x8 and place the pieces in their right places.
		"""

		self.piece_color = WHITE
		self.board = [[0 for x in range(COLS)] for _ in range(ROWS)]
		for row in range(ROWS):
			for col in range(COLS):
				if row == 0 or row  == 1:
					self.piece_color = WHITE
				elif row == 6 or row == 7:
					self.piece_color = BLACK

				if self.piece_color == BLACK:
					self.pieceInitialLetter = "B"

				if self.piece_color == WHITE:
					self.pieceInitialLetter = "W"

				if row == 0 or row == 7:
					if col == 0 or col == 7:
						self.board[row][col] = Rook(row, col, self.piece_color, f"{self.pieceInitialLetter}R")

					if col == 1 or col == 6:
						self.board[row][col] = Knight(row, col, self.piece_color, f"{self.pieceInitialLetter}N")

					if col == 2 or col == 5:
						self.board[row][col] = Bishop(row, col, self.piece_color, f"{self.pieceInitialLetter}B")

					if col == 3:
						self.board[row][col] = King(row, col, self.piece_color, f"{self.pieceInitialLetter}K")

					if col == 4:
						self.board[row][col] = Queen(row, col, self.piece_color, f"{self.pieceInitialLetter}Q")


				if row == 1 or row == 6:
					self.board[row][col] = Pawn(row, col, self.piece_color, f"{self.pieceInitialLetter}P")


	def draw_squares(self):
		"""
			Fill the screen with white color and draw the grey squares in pattern like chess board.
		"""
		
		self.win.fill(WHITE)
		for row in range(ROWS):
			for col in range(row%2 ,COLS, 2):
				pygame.draw.rect(self.win, GREY, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

	def draw_player_pos(self, row, col):
		"""
			Draw Player current pos.
		"""

		pygame.draw.rect(self.win, GREEN, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)


	def draw_valid_moves(self, moves):
		"""
			It will draw the valid moves. It will take moves (Type of Dict) as an arguments which have valid row and col where player can move.
		"""
		
		for move in moves:
			row, col = move
			pygame.draw.circle(self.win, GREEN, (col*SQUARE_SIZE+SQUARE_SIZE/2, row*SQUARE_SIZE+SQUARE_SIZE/2), 7)


	def draw(self):
		"""
			Handle bliting of everyting in game, e.g :- draw board, draw valid moves, draw player pos, rendering whose turn is right now, render who is the winner.
		"""
		
		self.draw_squares()

		for row in range(ROWS):
			for col in range(COLS):
				piece = self.board[row][col]
				if piece!=0:
					piece.draw(self.win)

		if self.selected and self.selected.color == self.turn:
			self.draw_valid_moves(self.valid_moves)

		self.draw_player_pos(self.selected_row, self.selected_col)
		self.render_turn()

		if self.winner:
			self.render_winner()


	def render_winner(self):
		"""
			Render the text which tell us about winner name when king has checked mate in other words when self.winner != None.	
		"""

		winner_name = self.set_name(self.winner)

		text = WINNER_FONT.render(f"{winner_name} Win!!", 1, GREEN)
		self.win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))

	def render_turn(self):
		"""
			Render the text which tell us about presend turns.			
		"""

		turn_name = self.set_name(self.turn)
		text = FONT.render(f"{turn_name} Turn", 1, RED)
		self.win.blit(text, (WIDTH-text.get_width()-10, 10))


	def move(self, piece, row, col):
		"""
			Move the piece and update the pos of that pieces in board.
		"""
		self.board[piece.row][piece.col], self.board[row][col] = 0, self.board[piece.row][piece.col]
		piece.move(row, col)

	def remove_piece(self, row, col):
		"""
			Remove the specific piece from the board.
		"""
		self.board[row][col] = 0


	def select(self, row, col):
		"""
			Call when user clicked on board and handle the movement of pieces if they are in valid moves.
		"""

		if self.selected:
			result = self.__move(row, col)
			if not result:
				self.selected = None
				self.select(row, col)

		self.selected_row, self.selected_col = row, col
		piece = self.board[row][col]
		self.selected = piece

		if piece != 0 and self.selected.color == self.turn:
			if isinstance(piece, Rook):
				self.valid_moves = piece.validate_rook(piece, self.board)
			elif isinstance(piece, Pawn):
				self.valid_moves = piece.validate_pawn(piece, self.board)
			elif isinstance(piece, Bishop):
				self.valid_moves = piece.validate_bishop(piece, self.board)
			elif isinstance(piece, King):
				self.valid_moves = piece.validate_king(piece, self.board)
			elif isinstance(piece, Knight):
				self.valid_moves = piece.validate_knight(piece, self.board)
			elif isinstance(piece, Queen):
				self.valid_moves = piece.validate_queen(piece, self.board)

			return True


	def __move(self, row, col):
		"""
			Check if the piece if eligible to move that specific row and col.
		"""

		piece = self.board[row][col]
		if self.selected and (row, col) in self.valid_moves and self.selected.color == self.turn:

			if isinstance(self.selected, Pawn):
				self.selected.is_moved_earlier = True
			self.remove_piece(row, col)
			self.move(self.selected, row, col)
			self.valid_moves = {}
			self.is_win(piece)

			self.change_turn()
		else:
			return False

		return True

	def change_turn(self):
		"""
			Change the turn.
		"""

		if self.turn == WHITE:
			self.turn = BLACK
		else:
			self.turn = WHITE

	def is_win(self, piece):
		"""
			Check if the King has checked mate.
		"""

		if isinstance(piece, King):
			if piece.color == WHITE:
				self.winner = BLACK
			else:
				self.winner = WHITE

			return True

		return False

	def set_name(self, obj1):
		"""
			Set the name White or Black name according to cond.
			## return name
		"""

		name = ""
		if obj1 == WHITE:
			name = "White"
		else:
			name = "Black"

		return name

	def generate_random_turn(self):
		"""
			Generate the random turns.
		"""

		self.turn = random.choice((WHITE, BLACK))