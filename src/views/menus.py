from src.gui.button import *


class Menu(pygame.sprite.Sprite):

    def __init__(self, screen):
        self.screen = screen
        self.all_sprites = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()

    def update(self):
        self.screen.fill(BLACK)
        for sprite in self.all_sprites:
            sprite.draw()
        pygame.display.flip()


class MainMenu(Menu):

    def __init__(self, screen):
        super().__init__(screen)

        Button(self.screen, GREEN, WIDTH/2, HEIGHT/5, 200, 50, "Play", self.all_sprites, self.buttons)