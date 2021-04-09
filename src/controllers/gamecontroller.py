from weakref import WeakSet

from src.events import *
from src.states import *
from src.models.player import *


class GameController(object):

    def __init__(self, state_machine, event_manager, view):
        self.state_machine = state_machine
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.view = view
        self.models = WeakSet()

    def notify(self, event):
        current_state = self.state_machine.peek()
        if current_state == States.PLAY_STATE:
            if event.name == Events.TICK_EVENT:
                self.update_models()
            elif event.name == Events.PLAYER_MOVE_EVENT:
                if event.direction == "r":
                    self.player.move_right()
                elif event.direction == "l":
                    self.player.move_left()

    def start(self):
        self.game_view = self.view.create_game_view()
        self.player = Player()
        self.game_view.create_player_sprite(self.player)

    def update_models(self):
        for m in self.models:
            m.update()