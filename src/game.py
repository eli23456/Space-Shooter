from src.controllers.controller import *


class Game(object):

    def __init__(self):
        self.state_machine = StateMachine()
        self.event_manager = EventManager()
        self.event_manager.register_listener(self)

        self.controller = Controller(self.state_machine, self.event_manager)

        self.running = False

    def notify(self, event):
        if event.name == Events.QUIT_EVENT:
            self.running = False

    def startup(self):
        self.event_manager.post(InitializeEvent())
        self.event_manager.post(StateChangeEvent(States.MAIN_STATE))
        self.event_manager.post(GameLoadEvent())

        self.running = True
        self.run()

    def run(self):
        while self.running:
            self.event_manager.post(TickEvent())