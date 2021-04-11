from src.data import *


class Bullet(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = None
        self.dmg = None

    def update(self):
        pass


class PlayerBullet(Bullet):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.speed = PLAYER_BULLET_SPEED
        self.dmg = PLAYER_BULLET_DMG

    def update(self):
        self.y -= self.speed


class EnemyBullet(Bullet):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.speed = ENEMY_BULLET_SPEED
        self.dmg = ENEMY_BULLET_DAMAGE

    def update(self):
        self.y += self.speed