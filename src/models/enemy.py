import random

from src.data import *


class Enemy(object):

    def __init__(self):
        self.x = None
        self.y = None

    def update(self):
        pass


class RegularEnemy(Enemy):

    def __init__(self):
        super().__init__()

        self.x = random.randrange(WIDTH - REGULAR_ENEMY_WIDTH)
        self.y = random.choice((250, 300))

    def update(self):
        pass


class MovingEnemy(RegularEnemy):

    def __init__(self):
        super().__init__()

        self.y = random.choice((150, 200))
        self.speed = MOVING_ENEMY_SPEED
        self.direction = random.choice(("r", "l"))

    def update(self):
        if self.direction == "r":
            self.x += self.speed
        elif self.direction == "l":
            self.x -= self.speed