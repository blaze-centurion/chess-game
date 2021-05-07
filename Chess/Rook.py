from .Pieces import Piece
from .Constant import *


class Rook(Piece):
	def __init__(self, row, col, color, pieceName):
		super().__init__(row, col, color, pieceName)
		self.row = row
		self.col = col
		self.color = color
		self.pieceName = pieceName

	def validate_rook(self, piece, board):
		"""
			Validate rook moves. It will take piece and board as an arguement.
			## return moves.
		"""
		moves = {}
		if piece.row < 7:
			moves.update(self._traverse_row(piece.row+1, ROWS, 1, piece, board))

		if piece.row > 0:
			moves.update(self._traverse_row(piece.row-1, -1, -1, piece, board))

		if piece.col > 0:
			moves.update(self._traverse_col(piece.col-1, -1, -1, piece, board))

		if piece.col < 7:
			moves.update(self._traverse_col(piece.col+1, COLS, 1, piece, board))

		return moves


	def _traverse_row(self, start, stop, step, piece, board):
		moves = {}
		for r in range(start, stop, step):
			current = board[r][piece.col]
			if current !=0:
				if current.color == piece.color:
					break
				else:
					moves[(r, piece.col)] = [r, piece.col]
					break
			else:
				moves[(r, piece.col)] = []

		return moves


	def _traverse_col(self, start, stop, step, piece, board):
		moves = {}

		for c in range(start, stop, step):
			current = board[piece.row][c]
			if current !=0:
				if current.color == piece.color:
					break
				else:
					moves[(piece.row, c)] = [piece.row, c]
					break
			else:
				moves[(piece.row, c)] = []

		return moves


	@classmethod
	def validate_sides_moves_for_queen(cls, piece, board):
		moves = {}
		if piece.row < 7:
			moves.update(cls._traverse_row(cls, piece.row+1, ROWS, 1, piece, board))

		if piece.row > 0:
			moves.update(cls._traverse_row(cls, piece.row-1, -1, -1, piece, board))

		if piece.col > 0:
			moves.update(cls._traverse_col(cls, piece.col-1, -1, -1, piece, board))

		if piece.col < 7:
			moves.update(cls._traverse_col(cls, piece.col+1, COLS, 1, piece, board))

		return moves