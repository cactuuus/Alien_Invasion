import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialises the game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Creates a ship, a group of bullets and a group of aliens.
    ship = Ship(screen, settings)
    bullets = Group()
    aliens = Group()

    # Creates the fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens)

    # Starts the main loop for the game.
    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(settings, aliens)
        gf.update_screen(settings, screen, ship, bullets, aliens)

# Main.
run_game()