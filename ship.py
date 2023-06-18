"""Dictates the player's ship appearance and behaviour."""
import pygame

class Ship():
    """A class representing the player's ship."""

    def __init__(self, screen, settings):
        """Initialises the ship and set its starting position."""
        self.screen = screen
        self.settings = settings
        
        # Loads the image and gets its rect.
        self.image = pygame.image.load("images/player_ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starts each new ship at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Stores a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position based on the movement flag."""
        # Updates the ship's value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        # Update rect object based on the self.center value.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

