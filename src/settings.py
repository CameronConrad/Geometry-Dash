# A class for the settings

class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Hero settings
        self.hero_size = 40
        self.hero_color = (255, 0, 0)

        # Tile settings
        self.tile_width = 50
        self.tile_height = 50
        self.tile_color = (0, 0, 255)

        # Gameplay settings
        self.speed = 1
        self.jump_height = 5

        # Graphics settings
        self.fps = 60

        # Tile types
        self.tile_codes = {
            0: "empty",
            1: "normal",
            2: "spike"
        }
        self.tile_colors = {
            "normal": self.tile_color,
            "spike": (255, 255, 0)
        }