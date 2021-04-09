from src.views.menuview import *
from src.views.gameview import *

class View:

    def __init__(self, state_machine, event_manager):
        self.state_machine = state_machine
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.bg_color = BLACK

    def notify(self, event):
        if event.name == Events.INIT_EVENT:
            self.initialize()
        elif event.name == Events.TICK_EVENT:
            self.tick()

    def initialize(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Space Shooter")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def tick(self):
        self.clock.tick(FPS)

    def create_menu_view(self):
        return MenuView(self.state_machine, self.event_manager, self.screen)

    def create_game_view(self):
        return GameView(self.state_machine, self.event_manager, self.screen, self.bg_color)