from src.data import *
from src.models.bullet import *


class Player:

    def __init__(self):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.hp = PLAYER_HP
        self.speed = PLAYER_SPEED

    def move_right(self):
        self.x += self.speed
        if self.x + (PLAYER_WIDTH / 2) > WIDTH:
            self.x = WIDTH - (PLAYER_WIDTH / 2)

    def move_left(self):
        self.x -= self.speed
        if self.x - (PLAYER_WIDTH / 2) < 0:
            self.x = 0 + (PLAYER_WIDTH / 2)

    def shoot(self):
        return PlayerBullet(self.x, self.y)