import pygame
import random
from pygame.sprite import Sprite
from alien_bullet import AlienBullet

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, settings, screen, audio=None):
        """Initialises the alien and sets its starting position."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.audio = audio

        # Loads the alien image and set its rect attribute.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Starts each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Stores the alien's exact position.
        self.x = float(self.rect.x)

    def explode(self):
        """Animation of the alien exploding."""
        self.audio.play(self.audio.alien_hit)

    def blitme(self):
        """Draws the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self) -> bool:
        """Returns True if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):
        """Moves the alien right or left."""
        self.x += (self.settings.alien_speed_factor *
                   self.settings.fleet_direction)
        self.rect.x = self.x

    def try_shooting(self) -> AlienBullet:
        """Attempt at firing a bullet."""
        if random.randrange(10000)  <= self.settings.alien_aggressiveness:
            self.audio.play(self.audio.alien_laser)
            return AlienBullet(self.settings, self.screen, self)
        else:
            return None