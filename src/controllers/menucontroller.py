import pygame

from src.states import *
from src.events import *


class MenuController:

    def __init__(self, state_machine, event_manager, view):
        self.state_machine = state_machine
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.view = view

    def notify(self, event):
        if event.name == Events.INPUT_EVENT:
            current_state = self.state_machine.peek()
            if current_state == States.MAIN_STATE:
                self.handle_main_menu(event)

    def load(self):
        self.menu_view = self.view.create_menu_view()

    def handle_main_menu(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.menu_view.main_menu.buttons:
                if button.is_over(event.clickpos):
                    if button.text == "Play":
                        self.event_manager.post(GameStartEvent())
                        self.event_manager.post(StateChangeEvent(States.PLAY_STATE))