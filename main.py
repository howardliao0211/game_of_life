import sys
import pygame
import game_functions as gf
from constants import *
from generation import GENERATION
from button import Button


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(BLACK)
    generation = GENERATION(screen)

    start_button = Button(
        screen,
        screen.get_width() / 2 - (BUTTON_WIDTH / 2),
        screen.get_height() * 0.9,
        120,
        40,
        "Start",
        generation.start,
        True,
    )

    while True:
        gf.event_update(screen, generation)
        pygame.display.update()
        start_button.update()
        generation.update()

if __name__ == "__main__":
    main()
