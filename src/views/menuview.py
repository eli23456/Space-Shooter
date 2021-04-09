from src.events import *
from src.states import *
from src.views.menus import *


class MenuView:

    def __init__(self, state_machine, event_manager, screen):
        self.state_machine = state_machine
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.screen = screen
        self.main_menu = MainMenu(self.screen)

    def notify(self, event):
        if event.name == Events.TICK_EVENT:
            current_state = self.state_machine.peek()
            if current_state == States.MAIN_STATE:
                self.main_menu.update()