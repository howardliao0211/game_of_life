from constants import *
from generation import GENERATION
import pygame
import sys
import time

class GameFunction():
    def __init__(self):
        self.mouse_pressed = False
        self.last_coord = []

    def event_update(self, screen, generation: GENERATION):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not generation.started:
                    self.mouse_pressed = True
                    clicked_coord = self.__find_clicked_cell(event.pos)
                    if (clicked_coord is not None) and (clicked_coord != self.last_coord) :
                        generation.change_state(clicked_coord[0], clicked_coord[1])
                        self.last_coord = clicked_coord

            elif event.type == pygame.MOUSEMOTION:
                if (self.mouse_pressed is True):
                    clicked_coord = self.__find_clicked_cell(event.pos)
                    if (clicked_coord is not None) and (clicked_coord != self.last_coord) :
                        generation.change_state(clicked_coord[0], clicked_coord[1])
                        self.last_coord = clicked_coord

            elif event.type == pygame.MOUSEBUTTONUP:
                if not generation.started:
                    self.mouse_pressed = False

    def __find_clicked_cell(self, pos):
        for x in range(0, GAME_WIDTH, BLOCK_SIZE):
            for y in range(0, GAME_HEIGHT, BLOCK_SIZE):
                if (
                    x < pos[0]
                    and pos[0] < (x + BLOCK_SIZE)
                    and y < pos[1]
                    and pos[1] < (y + BLOCK_SIZE)
                ):
                    return [int(x / BLOCK_SIZE), int(y / BLOCK_SIZE)]
        
        return None
