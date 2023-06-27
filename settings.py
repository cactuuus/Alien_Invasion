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
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60) # Dark gray
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up & score per alien increase
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # Initialises dynamic settings of the game
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialises settings and alien points values."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.5

        # 1 = right ; -1 = left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increases speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
