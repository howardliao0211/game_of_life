from constants import *
from cell import CELL
import pygame
import sys
import copy

class GENERATION:
    def __init__(self, screen):
        self.screen = screen
        self.started = False
        self.cell_list = []
        self.draw_grid()

    def draw_grid(self):
        BLOCK_SIZE  # Set the size of the grid block
        for x in range(0, GAME_WIDTH, BLOCK_SIZE):
            temp_cell_list = []
            for y in range(0, GAME_HEIGHT, BLOCK_SIZE):
                cell = CELL(self.screen, x, y, CellState.DEAD)
                temp_cell_list.append(cell)
            self.cell_list.insert(x, temp_cell_list)

    def set_to_dead(self, x, y):
        self.cell_list[x][y].set_to_dead(self.screen)

    def set_to_alive(self, x, y):
        self.cell_list[x][y].set_to_alive(self.screen)

    def change_state(self, x, y):
        self.cell_list[x][y].change_state(self.screen)

    def start(self):
        self.started = True

    def update(self):

        if not self.started:
            return

        live_neighnor_num = 0
        cell_list_dc = copy.deepcopy(self.cell_list)

        for x in range(CELL_WIDTH):
            for y in range(CELL_HEIGHT):
                live_neighnor_num = self.__find_live_neighbor_num(cell_list_dc, x, y)
                if(self.cell_list[x][y].cell_state is CellState.ALIVE):
                    if(live_neighnor_num < 2):
                        self.set_to_dead(x, y)
                    elif(live_neighnor_num == 2 or live_neighnor_num == 3):
                        self.set_to_alive(x, y)
                    elif(live_neighnor_num > 3):
                        self.set_to_dead(x, y)
                else:
                    if(live_neighnor_num == 3):
                        self.set_to_alive(x, y)

    def __find_live_neighbor_num(self, cell_list, x, y):
        live_neighbor = 0
        neighbor_dict = {
                         'top_left':    [x - 1, y - 1],
                         'top' :        [x,     y - 1],
                         'top_right' :  [x + 1, y - 1],
                         'left' :       [x - 1, y],
                         'right' :      [x + 1, y],
                         'bot_left' :   [x - 1, y + 1],
                         'bot' :        [x,     y + 1],
                         'bot_right' :  [x + 1, y + 1],
                        }
        if x == 0:
            neighbor_dict['top_left'][0] = MAX_CELL_X
            neighbor_dict['left'][0] = MAX_CELL_X
            neighbor_dict['bot_left'][0] = MAX_CELL_X
        elif x == MAX_CELL_X:
            neighbor_dict['top_right'][0] = 0
            neighbor_dict['right'][0] = 0
            neighbor_dict['bot_right'][0] = 0
        if y == 0:
            neighbor_dict['top_left'][1] = MAX_CELL_Y
            neighbor_dict['top'][1] = MAX_CELL_Y
            neighbor_dict['top_right'][1] = MAX_CELL_Y
        elif y == MAX_CELL_Y:
            neighbor_dict['bot_left'][1] = 0
            neighbor_dict['bot'][1] = 0
            neighbor_dict['bot_right'][1] = 0

        for coord in neighbor_dict.values():
            if cell_list[coord[0]][coord[1]].cell_state == CellState.ALIVE:
                live_neighbor += 1

        return live_neighbor