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

        # Gameplay settings
        self.speed = 1
        self.gravity = 0.1
        self.jump_height = 5

        # Graphics settings
        self.fps = 60