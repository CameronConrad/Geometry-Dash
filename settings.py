# A class for the settings

class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Hero settings
        self.hero_size = 50
        self.hero_color = (255, 0, 0)

        # Tile settings
        self.tile_width = 50
        self.tile_height = 50
        self.tile_color = (0, 0, 255)

        # Gameplay settings
        self.speed = 1
        self.direction = 1 # 1 for right, -1 for left
        self.gravity = 0.1
        self.jump_height = 5

        # Graphics settings
        self.fps = 60

        # Tile types
        self.tile_codes = {
            0: "empty",
            1: "normal",
            2: "spike"
        }
        self.tile_types = {
            "normal": self.tile_color,
            "spike": (255, 255, 0)
        }