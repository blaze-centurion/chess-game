from .Pieces import Piece
from .Constant import *


class King(Piece):
	def __init__(self, row, col, color, pieceName):
		super().__init__(row, col, color, pieceName)
		self.row = row
		self.col = col
		self.color = color
		self.pieceName = pieceName

	def validate_king(self, piece, board):
		"""
			Validate king moves. It will take piece and board as an arguement.
			## return moves.
		"""
		
		moves = {}

		if piece.row < 7:
			moves.update(self._traverse_vertically(piece.row+1, piece.col, piece, board))

		if piece.row > 0:
			moves.update(self._traverse_vertically(piece.row-1, piece.col, piece, board))

		if piece.col < 7:
			moves.update(self._traverse_horizontally(piece.row, piece.col+1, piece, board))

		if piece.col > 0:
			moves.update(self._traverse_horizontally(piece.row, piece.col-1, piece, board))

		return moves

	def _traverse_vertically(self, row, col, piece, board):
		moves = {}

		front_piece = board[row][col]

		if front_piece != 0:
			if front_piece.color != piece.color:
				moves[(row, col)] = [row, col]
		else:
			moves[(row, col)] = []

		# Check for right diagonals
		if col < 7:
			right_diagonal_piece = board[row][col+1]
			if right_diagonal_piece != 0:
				if right_diagonal_piece.color != piece.color:
					moves[(row, col+1)] = [row, col+1]
			else:
				moves[(row, col+1)] = []

		# Check for left diagonals
		if col > 0:
			left_diagonal_piece = board[row][col-1]
			if left_diagonal_piece != 0:
				if left_diagonal_piece.color != piece.color:
					moves[(row, col-1)] = [row, col-1]
			else:
				moves[(row, col-1)] = []


		return moves


	def _traverse_horizontally(self, row, col, piece, board):
		moves = {}
		current_piece = board[row][col]

		if current_piece !=0:
			if current_piece.color != piece.color:
				moves[(row, col)] = [row, col]
		else:
			moves[(row, col)] = []

		return moves