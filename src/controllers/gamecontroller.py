from weakref import WeakSet
import pygame

from src.events import *
from src.states import *
from src.models.player import *
from src.models.enemy import *


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
            elif event.name == Events.INPUT_EVENT:
                if event.key == pygame.K_SPACE:
                    bullet_model = self.player.shoot()
                    self.models.add(bullet_model)
                    self.game_view.create_player_bullet_sprite(bullet_model)
                elif event.key == pygame.K_ESCAPE:
                    self.event_manager.post(GamePauseEvent())
                    self.event_manager.post(StateChangeEvent(States.PAUSE_STATE))
            elif event.name == Events.PLAYER_MOVE_EVENT:
                if event.direction == "r":
                    self.player.move_right()
                elif event.direction == "l":
                    self.player.move_left()
            elif event.name == Events.SPAWN_REGULAR_ENEMY_EVENT:
                enemy_model = RegularEnemy()
                self.models.add(enemy_model)
                self.game_view.create_regular_enemy_sprite(enemy_model)
            elif event.name == Events.SPAWN_MOVING_ENEMY_EVENT:
                enemy_model = MovingEnemy()
                self.models.add(enemy_model)
                self.game_view.create_moving_enemy_sprite(enemy_model)

    def start(self):
        self.game_view = self.view.create_game_view()
        self.player = Player()
        self.game_view.create_player_sprite(self.player)

    def gameover(self):
        self.models.clear()
        self.game_view.clear()

    def restart(self):
        self.player = Player()
        self.game_view.create_player_sprite(self.player)

    def update_models(self):
        for m in self.models:
            m.update()

        self.check_player_health()
        self.check_enemy_shots()
        self.check_collisions()

    def check_player_health(self):
        if self.player.hp <= 0:
            self.event_manager.post(GameOverEvent())
            self.event_manager.post(StateChangeEvent(States.GAMEOVER_STATE))

    def check_enemy_shots(self):
        temp = []
        for m in self.models:
            if isinstance(m, Enemy):
                if m.can_shoot():
                    bullet_model = m.shoot()
                    temp.append(bullet_model)

        for bullet_model in temp:
            self.models.add(bullet_model)
            self.game_view.create_enemy_bullet_sprite(bullet_model)

    def check_collisions(self):
        # collision between enemies and player bullets
        collisions = pygame.sprite.groupcollide(self.game_view.enemies, self.game_view.player_bullets, False, True)
        for enemy_sprite, player_bullet in collisions.items():
            for i in range(len(player_bullet)):
                enemy_sprite.enemy_model.take_dmg(player_bullet[i].bullet_model.dmg)

        # collision between player and enemy bullets
        collisions = pygame.sprite.spritecollide(self.game_view.player_sprite, self.game_view.enemy_bullets, True)
        for enemy_bullet in collisions:
            self.game_view.player_sprite.player_model.take_dmg(enemy_bullet.bullet_model.dmg)