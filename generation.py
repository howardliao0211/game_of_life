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
        self.generation_num = 0
        self.reset()

    def reset(self):
        self.generation_num = 0
        self.started = False
        self.cell_list = []

        BLOCK_SIZE  # Set the size of the grid block
        for x in range(0, GAME_WIDTH, BLOCK_SIZE):
            temp_cell_list = []
            for y in range(0, GAME_HEIGHT, BLOCK_SIZE):
                cell = CELL(self.screen, x, y, CellState.DEAD)
                temp_cell_list.append(cell)
            self.cell_list.insert(x, temp_cell_list)

    def draw_cell(self):
        for x in range(CELL_WIDTH):
            for y in range(CELL_HEIGHT):
                if self.cell_list[x][y].cell_state is CellState.ALIVE:
                    self.set_to_alive(x, y)
                else:
                    self.set_to_dead(x, y)

    def set_to_dead(self, x, y):
        self.cell_list[x][y].set_to_dead(self.screen)

    def set_to_alive(self, x, y):
        self.cell_list[x][y].set_to_alive(self.screen)

    def change_state(self, x, y):
        self.cell_list[x][y].change_state(self.screen)

    def start(self):
        self.started = True
    
    def pause(self):
        self.started = False

    def update(self):

        self.draw_cell()

        '''
        Update world
        '''
        if self.started:
            live_neighnor_num = 0
            cell_list_dc = copy.deepcopy(self.cell_list)
            self.generation_num += 1
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
        '''
        Update Labels
        '''
        font = pygame.font.SysFont('monospace', 16)
        gen_label = font.render('Generation: ' + str(self.generation_num), 1, WHITE)
        self.screen.blit(gen_label, (0, GAME_HEIGHT + PANEL_HEIGHT * 0.1))

        live_cell = 0
        for x in range(CELL_WIDTH):
            for y in range(CELL_HEIGHT):
                if self.cell_list[x][y].cell_state is CellState.ALIVE:
                    live_cell += 1
        live_cell_label = font.render('Live Cell: ' + str(live_cell), 1, WHITE)
        self.screen.blit(live_cell_label, (0, GAME_HEIGHT + PANEL_HEIGHT * 0.5))

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