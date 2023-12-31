import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, type):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Import the game instance
        self.game = game

        # Tile attributes
        self.type = type
        self.image = pygame.Surface((self.game.settings.tile_attributes[self.type]["width"], 
                                     self.game.settings.tile_attributes[self.type]["height"]))
        self.image.fill(self.game.settings.tile_attributes[self.type]["color"])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = 0
    
    def setPos(self, x, y):
        # Set the position of the tile
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        # code to draw the tile on the screen
        if self.rect.x > -self.rect.width and self.rect.x < self.game.settings.screen_width:
            if self.type == "normal":
                self.game.screen.blit(self.image, self.rect)
            elif self.type == "spike":
                pygame.draw.polygon(self.game.screen, self.game.settings.tile_types[self.type], [
                    (self.rect.x, self.rect.y),
                    (self.rect.x + self.rect.width, self.rect.y),
                    (self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height)
                ])

    def update(self):
        # code to update the tile's position or other properties
        # self.rect.x -= self.game.settings.speed * self.game.settings.direction
        # Check if the tile is off the screen
        if self.rect.x < -self.rect.width:
            self.kill()
