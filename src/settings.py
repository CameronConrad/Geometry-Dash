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

        # Gameplay settings
        self.speed = 1
        self.jump_height = 5
        self.gravity = 1

        # Graphics settings
        self.fps = 60

        # Tile types
        self.tile_codes = {
            0: "empty",
            1: "normal",
            2: "spike"
        }
        self.tile_attributes = {
            "normal": {
                "outline": (0, 0, 0),
                "color": (0, 0, 255),
                "width": 50,
                "height": 50,
                "xfatal": True,
                "yfatal": False
            },
            "spike": {
                "outline": (0, 0, 0),
                "color": (255, 0, 0),
                "width": 30,
                "height": 30,
                "xfatal": True,
                "yfatal": True,
            },
        }