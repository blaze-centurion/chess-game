from .Pieces import Piece
from .Constant import *
from .Rook import Rook
from .Bishop import Bishop

class Queen(Piece):
	def __init__(self, row, col, color, pieceName):
		super().__init__(row, col, color, pieceName)
		self.row = row
		self.col = col
		self.color = color
		self.pieceName = pieceName

	def validate_queen(self, piece, board):
		"""
			Validate queen moves. It will take piece and board as an arguement.
			## return moves.
		"""
		moves = {}

		moves.update(Rook.validate_sides_moves_for_queen(piece, board))
		moves.update(Bishop.validate_diagonal_moves_for_queen(piece, board))

		return moves
