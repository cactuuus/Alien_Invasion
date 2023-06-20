"""A collection of functions used by the game."""
import sys
import pygame

from bullet import Bullet

def check_keydown_events(event, settings, screen, ship, bullets):
    """Responds to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        # Creates a new bullet and adds it to the bullets group.
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


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



def check_events(settings, screen, ship, bullets):
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship, bullets):
    """Updates images on the screen and flips to the new screen."""

    # Redraw the screen during each pass though the loop.
    screen.fill(settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Makes the most recently drawn screen visible.
    pygame.display.flip()
