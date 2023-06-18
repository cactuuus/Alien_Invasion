"""A collection of functions used by the game."""
import sys
import pygame

def check_keydown_events(event, ship):
    """Responds to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True


def check_keyup_events(event, ship):
    """Responds to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False   
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False



def check_events(ship):
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship):
    """Updates images on the screen and flips to the new screen."""
    # Redraw the screen during each pass though the loop.
    screen.fill(settings.bg_color)
    ship.blitme()

    # Makes the most recently drawn screen visible.
    pygame.display.flip()
