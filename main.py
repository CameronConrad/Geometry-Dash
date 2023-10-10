# A class for the game

import pygame
import sys
import json

from settings import Settings
from hero import Hero
from tile import Tile

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

        # Create a group for all sprites
        self.sprites = pygame.sprite.Group()

        # Create level variable
        self.level = 0

        # Load game map
        with open("map.json") as f:
            self.map = json.load(f)
    
    def initializeHero(self):
        # Create a hero
        self.hero = Hero(self, 100, 100)

        # Add the hero to the group of sprites
        self.sprites.add(self.hero)
    
    def setUp(self):
        # Initialize the hero
        self.initializeHero()
    
    def loadLevel(self, level):
        level = self.map[level]
        for row in level:
            for tile in row:
                if tile != 0:
                    self.sprites.add(Tile(self, row.index(tile) * self.settings.tile_width, 
                                          level.index(row) * self.settings.tile_height, 
                                          self.settings.tile_codes[tile]))

    def run(self):
        # Load the first level
        self.loadLevel(self.level)

        # Start the main loop for the game
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # Update sprites
            self.sprites.update()

            # Draw sprites
            self.sprites.draw(self.screen)

            # Make the most recently drawn screen visible
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.setUp()
    game.run()
