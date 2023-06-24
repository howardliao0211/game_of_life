from constants import *
import pygame

class CELL():

    def __init__(self, screen, x, y, cell_state: CellState):
        self.x = x
        self.y = y
        self.cell_state = cell_state

        if cell_state is CellState.ALIVE:
            self.set_to_alive(screen)
        elif cell_state is CellState.DEAD:
            self.set_to_dead(screen)

    def set_to_dead(self, screen):
        self.cell_state = CellState.DEAD
        pygame.draw.rect(screen, BACKGROUND_COLOR, pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, CELL_DEAD_COLOR, pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE), 1)

    def set_to_alive(self, screen):
        self.cell_state = CellState.ALIVE
        pygame.draw.rect(screen, CELL_ALIVE_COLOR, pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    def change_state(self, screen):
        if self.cell_state is CellState.DEAD:
            self.set_to_alive(screen)
        elif self.cell_state is CellState.ALIVE:
            self.set_to_dead(screen)
