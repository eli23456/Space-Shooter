import pygame

from src.data import *

class Button(pygame.sprite.Sprite):
    def __init__(self, screen, color, centerx, centery, width, height, text='', *groups):
        pygame.sprite.Sprite.__init__(self, groups)
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.x = self.rect.x
        self.y = self.rect.y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, outline=None):
        pygame.draw.rect(self.screen, self.color, self.rect, 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, True, WHITE)
            self.screen.blit(text, (self.rect.x + (self.width/2 - text.get_width()/2), self.rect.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False