from enum import Enum

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
CYAN = (0, 255, 255)

GAME_HEIGHT = 400
GAME_WIDTH = 400
BLOCK_SIZE = 20

CELL_WIDTH  = GAME_WIDTH  / BLOCK_SIZE
CELL_HEIGHT = GAME_HEIGHT / BLOCK_SIZE

MAX_CELL_X = CELL_WIDTH - 1
MAX_CELL_Y = CELL_HEIGHT - 1

WINDOW_WIDTH = GAME_WIDTH
WINDOW_HEIGHT = GAME_WIDTH + 100

BUTTON_WIDTH  = 120
BUTTON_HEIGHT = 40

class CellState(Enum):
    DEAD = 0
    ALIVE = 1