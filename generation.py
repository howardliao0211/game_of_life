from constants import *
from cell import CELL
import pygame

class GENERATION():

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
        pass