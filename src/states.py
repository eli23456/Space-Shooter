from enum import Enum


class States(Enum):
    INTRO_STATE = 1
    MAIN_STATE = 2
    PLAY_STATE = 3
    PAUSE_STATE = 4
    GO_STATE = 5
    HELP_STATE = 6
    ABOUT_STATE = 7
    LEAD_STATE = 8

class StateMachine(object):

    def __init__ (self):
        self.statestack = []

    def peek(self):
        try:
            return self.statestack[-1]
        except IndexError:
            # empty stack
            return None

    def pop(self):
        try:
            self.statestack.pop()
            return len(self.statestack) > 0
        except IndexError:
            # empty stack
            return None

    def push(self, state):
        self.statestack.append(state)
        return state