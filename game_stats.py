"""Tracks the game's statiscs and score."""

class GameStats():
    """Tracks statistics for Alien Invasion."""

    def __init__(self, settings):
        """Initialises statistics."""
        self.settings = settings
        self.reset_stats()

    def reset_stats(self):
        """Initialises statistics that can change throughout the game."""
        self.ships_left = self.settings.ship_limit