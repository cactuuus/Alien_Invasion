"""The game's settings."""

class Settings():
    """A class used to handle all settings for the game."""

    def __init__(self):
        """Initialises the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (136, 215, 247) # Sky blue

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60) # Dark gray
