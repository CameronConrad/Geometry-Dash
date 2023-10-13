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

        # Tile attributes
        self.tile_width = 50
        self.tile_height = 50

        # Set the position of the rect
        self.rect.x = x
        self.rect.y = y

        # Set game attributes
        self.alive = True
        self.jump = False
        self.velocity = 0
        self.acceleration = 0
    
    def draw(self):
        # Draw the hero
        self.game.screen.blit(self.image, self.rect)
    
    def update(self):
        # Check collisions
        if self.alive:
            self.check_key_presses()
            self.check_collisions()
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            self.acceleration += self.game.settings.gravity
    
    def jump(self):
        self.acceleration = -self.game.settings.jump_height
            
    def check_key_presses(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jump = True
    
    def check_if_in_screen(self):
        if self.rect.right < 0 or self.rect.left > self.game.screen_rect.width or self.rect.bottom < 0 or self.rect.top > self.game.screen_rect.height:
            self.alive = False

    def check_collisions(self):
        # Get the collision rect
        collision_rect = pygame.Rect(self.rect.x + self.game.settings.speed, self.rect.y + self.velocity, self.rect.width, self.rect.height)
        # Loop through each tile to check for collisions
        for tile in self.game.obstacles:
            if collision_rect.colliderect(tile.rect):
                # Check whether the hero collided with the top or bottom of the tile
                if tile.type == "spike":
                    self.alive = False
                    break
                # Check whether the hero collided with the left or right of the tile
                # If True, kill the hero
                # Check for collision with the right side of the tile
                if self.rect.left + self.velocity < tile.rect.right and self.rect.right > tile.rect.right:
                    self.alive = False
                # Check for collision with the left side of the tile
                elif self.rect.right + self.velocity > tile.rect.left and self.rect.left < tile.rect.left:
                    self.alive = False
                # Check for collision with the top of the tile
                elif self.rect.top + self.velocity < tile.rect.bottom:
                    # Set the velocity to 0
                    self.velocity = 0
                    # Set the top of the hero to the bottom of the tile
                    self.rect.bottom = tile.rect.top
                    # Set the acceleration to 0
                    self.acceleration = 0
                # Check for collision with the bottom of the tile
                elif self.rect.bottom + self.velocity > tile.rect.top:
                    # Set the velocity to 0
                    self.velocity = 0
                    # Set the bottom of the hero to the top of the tile
                    self.rect.top = tile.rect.bottom
                    # Set the acceleration to 0
                    self.acceleration = 0