from src.data import *


class Bullet(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass


class PlayerBullet(Bullet):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.speed = PLAYER_BULLET_SPEED

    def update(self):
        self.y -= self.speed