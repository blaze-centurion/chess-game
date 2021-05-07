from .Pieces import Piece
from .Constant import *


class Pawn(Piece):
	def __init__(self, row, col, color, pieceName):
		super().__init__(row, col, color, pieceName)
		self.row = row
		self.col = col
		self.color = color
		self.pieceName = pieceName
		self.is_moved_earlier = False  # Tell us that if piece has moved earlier or it his first time. So that we can check for how many moves it will take at a time.

	def validate_pawn(self, piece, board):
		"""
			Validate pawn moves. It will take piece and board as an arguement.
			## return moves.
		"""

		moves = {}

		# Return one move
		if self.is_moved_earlier:
			if piece.color == WHITE:
				if piece.row < 7:
					moves.update(self._traverse_pawn(piece.row+1, piece.row+2, 1, piece, board, piece.row+1))
			else:
				if piece.row > 0:
					moves.update(self._traverse_pawn(piece.row-1, piece.row-2, -1, piece, board, piece.row-1))

		# Return two move
		elif not self.is_moved_earlier:
			if piece.color == WHITE:
				if piece.row < 7:
					moves.update(self._traverse_pawn(piece.row+1, piece.row+3, 1, piece, board, piece.row+1))
			else:
				if piece.row > 0:
					moves.update(self._traverse_pawn(piece.row-1, piece.row-3, -1, piece, board, piece.row-1))

		return moves

	def _traverse_pawn(self, start, stop, step, piece, board, row):
		moves = {}

		for r in range(start, stop, step):
			
			if piece.col < 7:
				diagonal_positive_current = board[row][piece.col+1]  # Right diagonal piece

				# Check for right diagonal piece
				if diagonal_positive_current != 0:
					if diagonal_positive_current.color != piece.color:
						moves[(row, piece.col+1)] = [row, piece.col+1]

			if piece.col > 0:
				diagonal_negative_current = board[row][piece.col-1]  # Left diagonal piece

				# Check for left diagonal piece
				if diagonal_negative_current != 0:
					if diagonal_negative_current.color != piece.color:
						moves[(row, piece.col-1)] = [row, piece.col-1]


			current = board[r][piece.col]  # Front Piece
			# Check for front piece
			if current == 0:
				moves[(r, piece.col)] = []
			else:
				break

		return moves