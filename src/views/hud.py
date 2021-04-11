import pygame
from src.data import *


class GameHud:

    def __init__(self, screen):
        self.screen = screen

    def draw(self, player):
        self.draw_health_bar(player)

    def draw_health_bar(self, player_hp):
        x = 5
        y = 5
        fill = (player_hp / PLAYER_HP) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(self.screen, GREEN, fill_rect)
        pygame.draw.rect(self.screen, WHITE, outline_rect, 2)