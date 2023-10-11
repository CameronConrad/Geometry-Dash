# A class for the hero

import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()

        # Set the game instance
        self.game = game

        # Load the image
        self.image = pygame.Surface((self.game.settings.hero_size, self.game.settings.hero_size))
        self.image.fill(self.game.settings.hero_color)

        # Get the rect of the image
        self.rect = self.image.get_rect()

        # Set the position of the rect
        self.rect.x = x
        self.rect.y = y

        # Set game attributes
        self.alive = True
        self.jump = False
        self.acceleration = 0
    
    def draw(self):
        # Draw the hero
        self.game.screen.blit(self.image, self.rect)
    
    def update(self):
        # Check if jump is true
        if self.jump:
            self.acceleration = self.game.settings.jump_height
            
            
        