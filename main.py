# A class for the game

import pygame
import sys

from settings import Settings
from hero import Hero

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Create an instance of Settings
        self.settings = Settings()

        # Create the screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()

        # Set the caption
        pygame.display.set_caption("Geometry Dash")

        # Create the hero
        self.hero = Hero(self, 0, 0)

    def run(self):
        # Start the main loop for the game
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # Update sprites
            self.hero.update()

            # Draw sprites
            self.hero.draw()

            # Make the most recently drawn screen visible
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
