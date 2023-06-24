from constants import *
from generation import GENERATION
import pygame
import sys

def find_clicked_cell(pos):
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

def event_update(screen, generation: GENERATION):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.button == 1) and (not generation.started):
                clicked_coord = find_clicked_cell(event.pos)
                if clicked_coord is not None :
                    generation.change_state(clicked_coord[0], clicked_coord[1])
