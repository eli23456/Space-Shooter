from enum import Enum
from weakref import WeakKeyDictionary
from copy import deepcopy


class Events(Enum):
    BASE_EVENT = 1
    TICK_EVENT = 2
    INIT_EVENT = 3
    GAME_LOAD_EVENT = 4
    GAME_START_EVENT = 5
    GAME_PAUSE_EVENT = 6
    GAME_UNPAUSE_EVENT = 7
    GAME_OVER_EVENT = 8
    GAME_RESTART_EVENT = 9
    QUIT_EVENT = 10
    STATE_CHANGE_EVENT = 11
    INPUT_EVENT = 12
    PLAYER_MOVE_EVENT = 13
    SPAWN_REGULAR_ENEMY_EVENT = 14
    SPAWN_MOVING_ENEMY_EVENT = 15


class Event(object):

    def __init__(self):
        self.name = Events.BASE_EVENT

    def __str__(self):
        return repr(self.name)


class TickEvent(Event):

    def __init__(self):
        self.name = Events.TICK_EVENT


class InitializeEvent(Event):

    def __init__ (self):
        self.name = Events.INIT_EVENT


class GameLoadEvent(Event):

    def __init__(self):
        self.name = Events.GAME_LOAD_EVENT


class GameStartEvent(Event):

    def __init__(self):
        self.name = Events.GAME_START_EVENT


class GamePauseEvent(Event):

    def __init__(self):
        self.name = Events.GAME_PAUSE_EVENT


class GameUnpauseEvent(Event):

    def __init__(self):
        self.name = Events.GAME_UNPAUSE_EVENT


class GameOverEvent(Event):

    def __init__(self):
        self.name = Events.GAME_OVER_EVENT


class GameRestartEvent(Event):

    def __init__(self):
        self.name = Events.GAME_RESTART_EVENT


class QuitEvent(Event):

    def __init__(self):
        self.name = Events.QUIT_EVENT


class StateChangeEvent(Event):

    def __init__(self, state):
        self.name = Events.STATE_CHANGE_EVENT
        self.state = state

    def __str__(self):
        if self.state:
            return '%s pushed %s' % (repr(self.name), repr(self.state))
        else:
            return '%s popped' % (self.name, )


class InputEvent(Event):

    def __init__(self, type, key=None, clickpos=None):
        self.name = Events.INPUT_EVENT
        self.type = type
        self.key = key
        self.clickpos = clickpos

    def __str__(self):
        return '%s, char=%s, clickpos=%s' % (self.name, self.key, self.clickpos)


class PlayerMoveEvent(Event):

    def __init__ (self, direction):
        self.name = Events.PLAYER_MOVE_EVENT
        self.direction = direction


class SpawnRegularEnemyEvent(Event):

    def __init__(self):
        self.name = Events.SPAWN_REGULAR_ENEMY_EVENT


class SpawnMovingEnemyEvent(Event):

    def __init__(self):
        self.name = Events.SPAWN_MOVING_ENEMY_EVENT


class EventManager(object):

    def __init__(self):
        self.listeners = WeakKeyDictionary()

    def register_listener(self, listener):

        self.listeners[listener] = 1

    def unregister_listener(self, listener):

        if listener in self.listeners.keys():
            del self.listeners[listener]

    def post(self, event):

        if not isinstance(event, TickEvent):
            # print the event (unless it is TickEvent)
            print(event)
        listeners_copy = deepcopy(self.listeners)
        for listener in listeners_copy:
            listener.notify(event)