from src.data import *
from src.util.image import *


class PlayerSprite(pygame.sprite.Sprite):

    def __init__(self, player_model, *groups):
        pygame.sprite.Sprite.__init__(self, groups)

        self.player = player_model
        self.image = Image.load(PLAYER_IMG)
        self.image = Image.transform(self.image, self.player.width, self.player.height)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.player.x
        self.rect.centery = self.player.y

    def set_speed(self, speed):
        self.speed = speed

    def update(self):
        self.rect.centerx = self.player.x

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0