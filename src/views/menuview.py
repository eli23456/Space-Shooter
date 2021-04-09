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
        self.help_menu = HelpMenu(self.screen)
        self.about_menu = AboutMenu(self.screen)
        self.leaderboard_menu = LeaderboardMenu(self.screen)

    def notify(self, event):
        if event.name == Events.TICK_EVENT:
            current_state = self.state_machine.peek()
            if current_state == States.MAIN_STATE:
                self.main_menu.update()
            elif current_state == States.HELP_STATE:
                self.help_menu.update()
            elif current_state == States.ABOUT_STATE:
                self.about_menu.update()
            elif current_state == States.LEADERBOARD_STATE:
                self.leaderboard_menu.update()