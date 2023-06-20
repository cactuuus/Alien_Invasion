import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, settings, screen, ship):
        """Creates a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        # Creates a bullet rect at (0, 0), then sets correct position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Stores the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Moves the bullet up the screen."""
        # Updates the decimal position of te bullet.
        self.y -= self.speed_factor
        # Updates the rect position.
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draws the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)