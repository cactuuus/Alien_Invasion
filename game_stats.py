"""Tracks the game's statiscs and score."""

class GameStats():
    """Tracks statistics for Alien Invasion."""

    def __init__(self, settings):
        """Initialises statistics."""
        self.settings = settings
        self.reset_stats()

        # Initialises the high score.
        self.high_score = 0
        self.get_high_score()

        # Starts Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initialises statistics that can change throughout the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self):
        """Retrieves the current high score, if available."""
        hs_filename = self.settings.high_score_filename
        try:
            with open(hs_filename, 'r') as high_score_txt:
                self.high_score = int(high_score_txt.read())
        except FileNotFoundError:
                pass
