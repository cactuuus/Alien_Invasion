import pygame

class Settings():
    """A class used to handle all settings for the game."""

    def __init__(self):
        """Initialises the game's settings."""
        # Initialises clock.
        self.clock = pygame.time.Clock()
        self.fps_target = 120

        # High score file path.
        self.high_score_filename = "high_score.txt"

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = pygame.image.load("images/background.bmp")

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (242, 213, 24) # Yellow
        self.bullets_allowed = 6
        self.alien_bullet_color = (74, 201, 42) # Lime green

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up & score per alien increase
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.aggressiveness_scale = 1.3

        # Initialises dynamic settings of the game
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialises settings and alien points values."""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.3
        self.alien_bullet_speed_factor = 1
        # The higher the number, the higher the chance of aliens to fire
        self.alien_aggressiveness = 3

        # 1 = right ; -1 = left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increases speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_aggressiveness *= self.aggressiveness_scale

        self.alien_points = int(self.alien_points * self.score_scale)
