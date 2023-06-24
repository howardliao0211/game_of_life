from constants import *
from cell import CELL
import pygame
import copy


class GENERATION:
    def __init__(self, screen):
        self.started = False
        self.cell_list = []
        self.draw_grid(screen)

    def draw_grid(self, screen):
        BLOCK_SIZE  # Set the size of the grid block
        for x in range(0, GAME_WIDTH, BLOCK_SIZE):
            temp_cell_list = []
            for y in range(0, GAME_HEIGHT, BLOCK_SIZE):
                cell = CELL(screen, x, y, CellState.DEAD)
                temp_cell_list.append(cell)
            self.cell_list.insert(x, temp_cell_list)

    def set_to_dead(self, x, y):
        self.cell_list[x][y].set_to_dead()

    def set_to_alive(self, x, y):
        self.cell_list[x][y].set_to_alive()

    def change_state(self, x, y):
        self.cell_list[x][y].change_state()

    def start(self):
        self.started = True

    def update(self):
        cell_list_deep_copy = copy.deepcopy(self.cell_list)

    def __find_live_neighbor_num(self, cell_list, x, y):
        live_neighbor = 0
        neighbor_dict = {
                         'top_left':    [x - 1, y - 1],
                         'top' :        [x, y - 1],
                         'top_right' :  [x + 1, y + 1],
                         'left' :       [x - 1, y],
                         'right' :      [x + 1, y],
                         'bot_left' :   [x - 1, y + 1],
                         'bot' :        [x, y + 1],
                         'bot_right' :  [x + 1, y + 1],
                        }
        pass