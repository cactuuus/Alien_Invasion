"""A collection of functions used by the game."""
import sys
import pygame

from bullet import Bullet
from alien import Alien

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
        fire_bullet(settings, screen, ship, bullets)
    # Exits the game if 'q' is pressed.
    if event.key == pygame.K_q:
        sys.exit()


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


def update_screen(settings, screen, ship, bullets, aliens):
    """Updates images on the screen and flips to the new screen."""
    # Redraw the screen during each pass though the loop.
    screen.fill(settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Makes the most recently drawn screen visible.
    pygame.display.flip()

def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if the limit is not yet reached."""
    # Creates a new bullet and adds it to the bullets group.
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Updates position of bullets and gets rid of old bullets."""
    # Updates bullet position.
    bullets.update()
    
    # Gets rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_aliens_x(settings, alien_width) -> int:
    """Determine the number of aliens that fit in a row."""   
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x  = int(available_space_x / (2 * alien_width))         
    return number_aliens_x


def get_number_rows(settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (settings.screen_height - 
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    """Creates an alien and places it in the row"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(settings, screen, ship, aliens):
    """Creates a full fleet of aliens."""
    # Creates an alien and find the number of aliens in a row.
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height,
                                  alien.rect.height)

    # Creates the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)