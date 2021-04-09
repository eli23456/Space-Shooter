from src.states import *
from src.events import *
from src.sprites.playersprite import *
from src.sprites.enemysprite import *
from src.sprites.bulletsprite import *


class GameView:

    def __init__(self, state_machine, event_manager, screen, bg):
        self.state_machine = state_machine
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.screen = screen
        self.bg_color = bg

        self.all_sprites = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

    def notify(self, event):
        if event.name == Events.TICK_EVENT:
            current_state = self.state_machine.peek()
            if current_state == States.PLAY_STATE:
                self.render()

    def render(self):
        self.screen.fill(self.bg_color)
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def create_player_sprite(self, player):
        return PlayerSprite(player, self.all_sprites)

    def create_player_bullet_sprite(self, bullet_model):
        PlayerBulletSprite(bullet_model, self.all_sprites, self.player_bullets)

    def create_regular_enemy_sprite(self, enemy):
        RegularEnemySprite(enemy, self.all_sprites, self.enemies)

    def create_moving_enemy_sprite(self, enemy):
        MovingEnemySprite(enemy, self.all_sprites, self.enemies)