from .Constant import SQUARE_SIZE, IMAGES, ROWS, COLS, WHITE


class Piece:
	def __init__(self, row, col, color, pieceName="WP"):
		self.row = row
		self.col = col
		self.color = color
		self.pieceName = pieceName
		self.x = 0
		self.y = 0
		self.piece_image = IMAGES[self.pieceName]
		self.calc_pos()

	def calc_pos(self):
		self.x = SQUARE_SIZE * self.col + SQUARE_SIZE/2 - self.piece_image.get_width()/2
		self.y = SQUARE_SIZE * self.row + SQUARE_SIZE/2 - self.piece_image.get_height()/2

	def draw(self, win):
		win.blit(self.piece_image, (self.x, self.y))

	def move(self, row, col):
		self.row = row
		self.col = col
		self.calc_pos()