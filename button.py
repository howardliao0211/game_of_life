import pygame
import time

class Button():
    def __init__(self, screen, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.buttonText = buttonText
        self.font = pygame.font.SysFont('Arial', 40)

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = self.font.render(self.buttonText, True, (20, 20, 20))
    
    def update(self):
        mousePos = pygame.mouse.get_pos()
        if not (self.onePress and self.alreadyPressed):
            self.buttonSurface.fill(self.fillColors['normal'])
            if self.buttonRect.collidepoint(mousePos):
                self.buttonSurface.fill(self.fillColors['hover'])
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.buttonSurface.fill(self.fillColors['pressed'])
                    if(self.onclickFunction is not None):
                        self.onclickFunction()
                        time.sleep(0.1)
                    self.alreadyPressed = True

        self.buttonSurf = self.font.render(self.buttonText, True, (20, 20, 20))
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)
    
    