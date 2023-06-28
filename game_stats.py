"""Tracks the game's statiscs and score."""

class GameStats():
    """Tracks statistics for Alien Invasion."""

    def __init__(self, settings):
        """Initialises statistics."""
        self.settings = settings
        self.reset_stats()

        # High score (should never be reset).
        self.high_score = 0

        # Starts Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initialises statistics that can change throughout the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1