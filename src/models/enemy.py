import random
import pygame

from src.data import *
from src.models.bullet import *


class Enemy(object):

    def __init__(self):
        self.x = None
        self.y = None
        self.hp = None
        self.shot_delay = random.randrange(1000, 5000)
        self.last_shot = pygame.time.get_ticks()

    def can_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shot_delay:
            self.last_shot = now
            return True
        else:
            return False

    def shoot(self):
        return EnemyBullet(self.x, self.y)

    def take_dmg(self, dmg):
        self.hp -= dmg

    def update(self):
        pass


class RegularEnemy(Enemy):

    def __init__(self):
        super().__init__()

        self.x = random.randrange(WIDTH - REGULAR_ENEMY_WIDTH)
        self.y = random.choice((250, 300))
        self.hp = REGULAR_ENEMY_HP

    def update(self):
        pass


class MovingEnemy(RegularEnemy):

    def __init__(self):
        super().__init__()

        self.y = random.choice((150, 200))
        self.speed = MOVING_ENEMY_SPEED
        self.direction = random.choice(("r", "l"))
        self.hp = MOVING_ENEMY_HP

    def update(self):
        if self.direction == "r":
            self.x += self.speed
        elif self.direction == "l":
            self.x -= self.speed