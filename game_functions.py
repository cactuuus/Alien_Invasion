"""A collection of functions used by the game."""
import sys
import pygame

def check_events():
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, ship):
    """Updates images on the screen and flips to the new screen."""
    # Redraw the screen during each pass though the loop.
    screen.fill(settings.bg_color)
    ship.blitme()

    # Makes the most recently drawn screen visible.
    pygame.display.flip()
