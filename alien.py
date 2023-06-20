import pygame
from pygame.sprite import AbstractGroup, Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, settings, screen):
        """Initialises the alien and sets its starting position."""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Loads the alien image and set its rect attribute.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Starts each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Stores the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the alien at its current location."""
        self.screen.blit(self.image, self.rect)        