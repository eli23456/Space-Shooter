from src.events import *


class StateController:

    def __init__(self, state_machine, event_manager):
        self.state_machine = state_machine
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

    def notify(self, event):
        if event.name == Events.STATE_CHANGE_EVENT:
            # pop request
            if not event.state:
                # false if no more states are left
                if not self.state_machine.pop():
                    self.event_manager.post(QuitEvent())
            else:
                # push a new state on the stack
                self.state_machine.push(event.state)