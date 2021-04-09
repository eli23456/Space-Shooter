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
        Button(self.screen, GREEN, WIDTH / 2, HEIGHT / 5 + 75, 200, 50, "Help", self.all_sprites, self.buttons)
        Button(self.screen, GREEN, WIDTH / 2, HEIGHT / 5 + 150, 200, 50, "About", self.all_sprites, self.buttons)
        Button(self.screen, GREEN, WIDTH / 2, HEIGHT / 5 + 225, 200, 50, "Lead", self.all_sprites, self.buttons)
        Button(self.screen, GREEN, WIDTH / 2, HEIGHT / 5 + 300, 200, 50, "Quit", self.all_sprites, self.buttons)


class HelpMenu(Menu):

    def __init__(self, screen):
        super().__init__(screen)

        Button(self.screen, GREEN, WIDTH/2, HEIGHT/5 + 375, 200, 50, "Back", self.all_sprites, self.buttons)


class AboutMenu(Menu):

    def __init__(self, screen):
        super().__init__(screen)

        Button(self.screen, GREEN, WIDTH/2, HEIGHT/5 + 375, 200, 50, "Back", self.all_sprites, self.buttons)


class LeaderboardMenu(Menu):

    def __init__(self, screen):
        super().__init__(screen)

        Button(self.screen, GREEN, WIDTH/2, HEIGHT/5 + 375, 200, 50, "Back", self.all_sprites, self.buttons)