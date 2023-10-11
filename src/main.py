# A class for the game

import pygame
import sys
import os
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
        map_path = os.path.join(os.path.dirname(__file__), 'assets', 'map.json')
        with open(map_path) as f:
            self.map = json.load(f)
    
    def initializeHero(self, x, y):
        # Create a hero
        self.hero = Hero(self, x, y)

        # Add the hero to the group of sprites
        self.sprites.add(self.hero)
    
    def setUp(self):
        # Generate the sprites needed for the game based on the level
        self.loadLevel()
    
    def loadLevel(self):
        # Load the level
        levelMap = self.map[self.level]
        # Create tiles based on the values in the level array
        for y, row in enumerate(levelMap):
            for x, tile in enumerate(row):
                if tile > 0:
                    # A tile
                    self.sprites.add(Tile(self, x * self.settings.tile_width, 
                                        y * self.settings.tile_height, 
                                        self.settings.tile_codes[tile]))
                elif tile == -1:
                    # The hero
                    self.initializeHero(x * self.settings.tile_width, 
                                        y * self.settings.tile_height)
        # Print the positions of the sprites
        for sprite in self.sprites.sprites():
            print(f"x: {sprite.rect.x}, y: {sprite.rect.y}")

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
            self.sprites.update()

            # Draw sprites
            self.sprites.draw(self.screen)

            # Make the most recently drawn screen visible
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.setUp()
    game.run()
