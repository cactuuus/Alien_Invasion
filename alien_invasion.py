import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
    # Initialises the game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Makes the 'Play' button.
    play_button = Button(settings, screen, "Play")

    # Creates an instance to store game statistics and creates a scoreboard.
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    # Creates a ship, a group of bullets and a group of aliens.
    ship = Ship(screen, settings)
    bullets = Group()
    aliens = Group()


    # Creates the fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens)

    # Starts the main loop for the game.
    while True:
        gf.check_events(settings, screen, stats, play_button, ship, aliens,
                         bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(settings, screen, stats, sb, ship, bullets, aliens,
                         play_button)

# Main.
run_game()