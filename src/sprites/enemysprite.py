import pygame

from src.data import *
from src.util.image import *


class EnemySprite(pygame.sprite.Sprite):

    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, groups)

    def update(self):
        pass


class RegularEnemySprite(EnemySprite):

    def __init__(self, enemy_model, *groups):
        super().__init__(groups)

        self.enemy_model = enemy_model
        self.image = Image.load(REGULAR_ENEMY_IMG)
        self.image = Image.transform(self.image, REGULAR_ENEMY_WIDTH, REGULAR_ENEMY_HEIGHT)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.enemy_model.x
        self.rect.centery = self.enemy_model.y


class MovingEnemySprite(RegularEnemySprite):

    def __init__(self, enemy_model, *groups):
        super().__init__(enemy_model, groups)

    def update(self):
        self.rect.x = self.enemy_model.x

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.enemy_model.direction = "l"
        elif self.rect.left < 0:
            self.rect.left = 0
            self.enemy_model.direction = "r"