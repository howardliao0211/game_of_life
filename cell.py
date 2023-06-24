from constants import *
import pygame

class CELL():

    def __init__(self, screen, x, y, cell_state: CellState):
        self.screen = screen
        self.x = x
        self.y = y
        self.cell_state = cell_state

        if cell_state is CellState.ALIVE:
            self.set_to_alive()
        elif cell_state is CellState.DEAD:
            self.set_to_dead()

    def set_to_dead(self):
        self.cell_state = CellState.DEAD
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE), 1)

    def set_to_alive(self):
        self.cell_state = CellState.ALIVE
        pygame.draw.rect(self.screen, CYAN, pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    def change_state(self):
        if self.cell_state is CellState.DEAD:
            self.set_to_alive()
        elif self.cell_state is CellState.ALIVE:
            self.set_to_dead()
