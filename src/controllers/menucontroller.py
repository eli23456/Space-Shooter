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
            elif current_state == States.HELP_STATE:
                self.handle_help_menu(event)
            elif current_state == States.ABOUT_STATE:
                self.handle_about_menu(event)
            elif current_state == States.LEADERBOARD_STATE:
                self.handle_leaderboard_menu(event)
            elif current_state == States.PAUSE_STATE:
                self.handle_pause_menu(event)

    def load(self):
        self.menu_view = self.view.create_menu_view()

    def handle_main_menu(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.menu_view.main_menu.buttons:
                if button.is_over(event.clickpos):
                    if button.text == "Play":
                        self.event_manager.post(GameStartEvent())
                        self.event_manager.post(StateChangeEvent(States.PLAY_STATE))
                    elif button.text == "Help":
                        self.event_manager.post(StateChangeEvent(States.HELP_STATE))
                    elif button.text == "About":
                        self.event_manager.post(StateChangeEvent(States.ABOUT_STATE))
                    elif button.text == "Lead":
                        self.event_manager.post(StateChangeEvent(States.LEADERBOARD_STATE))
                    elif button.text == "Quit":
                        self.event_manager.post(QuitEvent())

    def handle_help_menu(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.menu_view.help_menu.buttons:
                if button.is_over(event.clickpos):
                    if button.text == "Back":
                        self.event_manager.post(StateChangeEvent(None))

    def handle_about_menu(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.menu_view.about_menu.buttons:
                if button.is_over(event.clickpos):
                    if button.text == "Back":
                        self.event_manager.post(StateChangeEvent(None))

    def handle_leaderboard_menu(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.menu_view.leaderboard_menu.buttons:
                if button.is_over(event.clickpos):
                    if button.text == "Back":
                        self.event_manager.post(StateChangeEvent(None))

    def handle_pause_menu(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.menu_view.pause_menu.buttons:
                if button.is_over(event.clickpos):
                    if button.text == "Continue":
                        self.event_manager.post(StateChangeEvent(None))
                    elif button.text == "Quit":
                        self.event_manager.post(QuitEvent())