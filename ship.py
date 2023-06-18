"""Dictates the player's ship appearance and behaviour."""
import pygame

class Ship():
    """A class representing the player's ship."""

    def __init__(self, screen):
        """Initialises the ship and set its starting position."""
        self.screen = screen
        
        # Loads the image and gets its rect.
        self.image = pygame.image.load("images/player_ship.bmp")
        pygame.transform.scale(self.image, (50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starts each new ship at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

