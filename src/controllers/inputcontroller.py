import random
import pygame

from src.events import *


class InputController:

    def __init__(self, state_machine, event_manager):
        self.state_machine = state_machine
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.spawn_regular_enemy = None
        self.spawn_moving_enemy = None

    def notify(self, event):
        if event.name == Events.TICK_EVENT:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.event_manager.post(QuitEvent())
                elif event.type == pygame.KEYDOWN:
                    self.event_manager.post(InputEvent(event.type, event.key))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.event_manager.post(InputEvent(event.type, None, event.pos))
                elif event.type == self.spawn_regular_enemy:
                    self.event_manager.post(SpawnRegularEnemyEvent())
                    self.set_regular_enemy_timer()
                elif event.type == self.spawn_moving_enemy:
                    self.event_manager.post(SpawnMovingEnemyEvent())
                    self.set_moving_enemy_timer()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.event_manager.post(PlayerMoveEvent("r"))
            elif keys[pygame.K_LEFT]:
                self.event_manager.post(PlayerMoveEvent("l"))

    def start(self):
        self.spawn_regular_enemy = pygame.USEREVENT + 1
        self.spawn_moving_enemy = pygame.USEREVENT + 2
        self.set_regular_enemy_timer()
        self.set_moving_enemy_timer()

    def set_regular_enemy_timer(self):
        pygame.time.set_timer(self.spawn_regular_enemy, random.randrange(500, 1000))

    def set_moving_enemy_timer(self):
        pygame.time.set_timer(self.spawn_moving_enemy, random.randrange(1000, 2000))