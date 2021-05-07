import pygame

pygame.init()


WIDTH, HEIGHT = 800,800

ROWS, COLS = 8,8
SQUARE_SIZE = WIDTH//COLS


# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (124,124,124)
GREEN = (0,255,0)
RED = (255,0,0)

# Images

BLACK_BISHOP = pygame.transform.scale(pygame.image.load('assests/bB.png'), (65,65))
BLACK_ROOK = pygame.transform.scale(pygame.image.load('assests/bR.png'), (65,65))
BLACK_KING = pygame.transform.scale(pygame.image.load('assests/bK.png'), (65,65))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load('assests/bN.png'), (65,65))
BLACK_PAWN = pygame.transform.scale(pygame.image.load('assests/bp.png'), (65,65))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('assests/bQ.png'), (65,65))

WHITE_BISHOP = pygame.transform.scale(pygame.image.load('assests/wB.png'), (65,65))
WHITE_ROOK = pygame.transform.scale(pygame.image.load('assests/wR.png'), (65,65))
WHITE_KING = pygame.transform.scale(pygame.image.load('assests/wK.png'), (65,65))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load('assests/wN.png'), (65,65))
WHITE_PAWN = pygame.transform.scale(pygame.image.load('assests/wp.png'), (65,65))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('assests/wQ.png'), (65,65))


IMAGES = {
	"BB": BLACK_BISHOP,
	"BR": BLACK_ROOK,
	"BK": BLACK_KING,
	"BN": BLACK_KNIGHT,
	"BQ": BLACK_QUEEN,
	"BP": BLACK_PAWN,
	"WB": WHITE_BISHOP,
	"WR": WHITE_ROOK,
	"WK": WHITE_KING,
	"WN": WHITE_KNIGHT,
	"WQ": WHITE_QUEEN,
	"WP": WHITE_PAWN
}

# Fonts

WINNER_FONT = pygame.font.SysFont("comicsans", 100)
FONT = pygame.font.SysFont("comicsans", 40)