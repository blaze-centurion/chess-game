from .Pieces import Piece
from .Constant import *

class Bishop(Piece):
	def __init__(self, row, col, color, pieceName):
		super().__init__(row, col, color, pieceName)
		self.row = row
		self.col = col
		self.color = color
		self.pieceName = pieceName

	def validate_bishop(self, piece, board):
		"""
			Validate bishop moves. It will take piece and board as an arguement.
			## return moves.
		"""

		moves = {}

		moves.update(self._traverse_right_diagonal(piece, board))
		moves.update(self._traverse_left_diagonal(piece, board))

		return moves

	def _traverse_right_diagonal(self, piece, board):
		moves = {}
		
		try:
			for x in [1,-1]:
				i = 1 if x > 0 else -1
				while True:
					row = piece.row + i
					col = piece.col + i
					if (row <=7 and row >=0) and (col<=7 and col>=0):
						current = board[row][col]
						if current !=0:
							if current.color == piece.color:
								break
							else:
								moves[(row, col)] = [row, col]
								break
						else:
							moves[(row, col)] = []
					else:
						break

					if i<0:
						i-=1
					else:
						i+=1

		except Exception as e:
			print(e)

		return moves

	def _traverse_left_diagonal(self, piece, board):
		moves = {}

		try:
			for x in [1,-1]:
				i = 1 if x > 0 else -1
				while True:
					row = piece.row + i
					col = piece.col - i
					if row <=7 and row >=0 and col<=7 and col>=0:
						current = board[row][col]
						if current !=0:
							if current.color == piece.color:
								break
							else:
								moves[(row, col)] = [row, col]
								break
						else:
							moves[(row, col)] = []
					else:
						break

					if i<0: i-=1
					else: i+=1

		except Exception as e:
			print(e)

		return moves

	@classmethod
	def validate_diagonal_moves_for_queen(cls, piece, board):
		"""
			Return diagonal valid moves for queen.
		"""

		moves = {}

		moves.update(cls._traverse_right_diagonal(cls, piece, board))
		moves.update(cls._traverse_left_diagonal(cls, piece, board))

		return moves