import pygame

from src.data import *
from src.util.image import *


class BulletSprite(pygame.sprite.Sprite):

    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, groups)

    def update(self):
        self.rect.y = self.bullet_model.y

        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()


class PlayerBulletSprite(BulletSprite):

    def __init__(self, bullet_model, *groups):
        super().__init__(groups)

        self.bullet_model = bullet_model
        self.image = Image.load(PLAYER_BULLET_IMG)
        self.image = Image.transform(self.image, PLAYER_BULLET_WIDTH, PLAYER_BULLET_HEIGHT)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.bullet_model.x
        self.rect.centery = self.bullet_model.y


class EnemyBulletSprite(BulletSprite):

    def __init__(self, bullet_model, *groups):
        super().__init__(groups)

        self.bullet_model = bullet_model
        self.image = Image.load(ENEMY_BULLET_IMG)
        self.image = Image.transform(self.image, ENEMY_BULLET_WIDTH, ENEMY_BULLET_HEIGHT)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.bullet_model.x
        self.rect.centery = self.bullet_model.y