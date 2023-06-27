"""A class representing the game'scoreboard."""
import pygame.font

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, settings, screen, stats):
        """Initialises scorekeeping attributes."""
        self.screen = screen

        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepares the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turns the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)
        
        # Displays the score at the top of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)