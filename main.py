import sys
import pygame
from game_functions import GameFunction
from constants import *
from generation import GENERATION
from button import Button


def main():
    global start_button
    global generation

    pygame.init()
    pygame.display.set_caption("Conway's Game of life")

    gf = GameFunction()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(BLACK)
    generation = GENERATION(screen)
    

    start_button = Button(
        screen,
        screen.get_width()  * 0.6 - (160 / 2),
        GAME_HEIGHT + PANEL_HEIGHT * 0.1,
        160,
        40,
        "Start",
        start_button_click_function,
        False,
    )

    clear_button = Button(      
        screen,
        screen.get_width()  * 0.6 - (160 / 2),
        GAME_HEIGHT + PANEL_HEIGHT * 0.5,
        160,
        40,
        "Clear",
        generation.reset,
        False,
    )

    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        gf.event_update(screen, generation)
        start_button.update()
        clear_button.update()
        generation.update()
        pygame.display.flip()

def start_button_click_function():
    if(start_button.buttonText == 'Start'):
        start_button.buttonText = 'Pause'
        generation.start()

    elif(start_button.buttonText == 'Pause'):
        start_button.buttonText = 'Continue'
        generation.pause()

    elif(start_button.buttonText == 'Continue'):
        start_button.buttonText = 'Pause'
        generation.start()

if __name__ == "__main__":
    main()
