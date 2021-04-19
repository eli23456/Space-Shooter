from src.views.view import *
from src.controllers.statecontroller import *
from src.controllers.inputcontroller import *
from src.controllers.menucontroller import *
from src.controllers.gamecontroller import *


class Controller(object):

    def __init__(self, state_machine, event_manager):
        self.state_machine = state_machine
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.view = View(self.state_machine, self.event_manager)

    def notify(self, event):
        if event.name == Events.INIT_EVENT:
            self.initialize()
        elif event.name == Events.GAME_LOAD_EVENT:
            self.load()
        elif event.name == Events.GAME_START_EVENT:
            self.start()
        elif event.name == Events.GAME_PAUSE_EVENT:
            self.pause()
        elif event.name == Events.GAME_UNPAUSE_EVENT:
            self.unpause()
        elif event.name == Events.GAME_OVER_EVENT:
            self.gameover()
        elif event.name == Events.GAME_RESTART_EVENT:
            self.restart()

    def initialize(self):
        self.state_controller = StateController(self.state_machine, self.event_manager)
        self.input_controller = InputController(self.state_machine, self.event_manager)
        self.menu_controller = MenuController(self.state_machine, self.event_manager, self.view)
        self.game_controller = GameController(self.state_machine, self.event_manager, self.view)

    def load(self):
        self.menu_controller.load()

    def start(self):
        self.game_controller.start()
        self.input_controller.start()

    def pause(self):
        self.input_controller.pause()

    def unpause(self):
        self.input_controller.unpause()

    def gameover(self):
        self.input_controller.pause()
        self.game_controller.gameover()

    def restart(self):
        self.input_controller.restart()
        self.game_controller.restart()