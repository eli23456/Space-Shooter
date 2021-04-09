import pygame

from src.events import *


class InputController:

    def __init__(self, state_machine, event_manager):
        self.state_machine = state_machine
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

    def notify(self, event):
        if event.name == Events.TICK_EVENT:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.event_manager.post(QuitEvent())
                elif event.type == pygame.KEYDOWN:
                    self.event_manager.post(InputEvent(event.type, event.key))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.event_manager.post(InputEvent(event.type, None, event.pos))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.event_manager.post(PlayerMoveEvent("r"))
            elif keys[pygame.K_LEFT]:
                self.event_manager.post(PlayerMoveEvent("l"))