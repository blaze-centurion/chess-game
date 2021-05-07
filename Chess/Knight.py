from .Constant import *
from .Pieces import Piece

class Knight(Piece):
	def __init__(self, row, col, color, pieceName):
		super().__init__(row, col, color, pieceName)
		self.row = row
		self.col = col
		self.color = color
		self.pieceName = pieceName

	def validate_knight(self, piece, board):
		"""
			Validate knight moves. It will take piece and board as an arguement.
			## return moves.
		"""
		moves = {}

		if piece.row+2 <=7:
			moves.update(self._traverse_vertically(piece.row+2, piece, board))

		if piece.row-2 >=0:
			moves.update(self._traverse_vertically(piece.row-2, piece, board))

		if piece.col+2 <= 7:
			moves.update(self._traverse_horizontally(piece.col+2, piece, board))

		if piece.col-2 >=0:
			moves.update(self._traverse_horizontally(piece.col-2, piece, board))

		return moves

	def _traverse_vertically(self, row, piece, board):
		moves = {}

		if piece.col < 7:
			right_piece = board[row][piece.col+1]

			if right_piece != 0:
				if right_piece.color != piece.color:
					moves[(row, piece.col+1)] = [row, piece.col+1]
			else:
				moves[(row, piece.col+1)] = []

		if piece.col > 0:
			left_piece = board[row][piece.col-1]

			if left_piece != 0:
				if left_piece.color != piece.color:
					moves[(row, piece.col-1)] = [row, piece.col-1]
			else:
				moves[(row, piece.col-1)] = []

		return moves

	def _traverse_horizontally(self, col, piece, board):
		moves = {}

		if piece.row < 7:
			right_piece = board[piece.row+1][col]

			if right_piece != 0:
				if right_piece.color != piece.color:
					moves[(piece.row+1, col)] = [piece.row+1, col]
			else:
				moves[(piece.row+1, col)] = []

		if piece.row > 0:
			right_piece = board[piece.row-1][col]

			if right_piece != 0:
				if right_piece.color != piece.color:
					moves[(piece.row-1, col)] = [piece.row-1, col]
			else:
				moves[(piece.row-1, col)] = []

		return moves