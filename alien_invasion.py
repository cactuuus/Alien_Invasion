import pygame
import game_functions as gf
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from audio import Audio

def run_game():
    # Sets proper default values for mixer before the pygame.init() call
    pygame.mixer.pre_init()

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

    # Loads audio effects and music
    audio = Audio()

    # Creates a ship, a group of bullets and a group of aliens.
    ship = Ship(screen, settings, audio)
    bullets = Group()
    aliens = Group()
    alien_bullets = Group()


    # Creates the fleet of aliens.
    gf.create_fleet(settings, screen, audio, ship, aliens)

    # Starts the main loop for the game.
    while True:
        gf.check_events(settings, screen, stats, audio, sb, play_button, ship,
                        aliens, bullets, alien_bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, audio, sb, ship, aliens,
                              bullets, alien_bullets)
            gf.update_aliens(settings, stats, screen, audio, sb, ship, aliens,
                             bullets, alien_bullets)

        gf.update_screen(settings, screen, stats, sb, ship, bullets, aliens,
                         play_button, alien_bullets)

# Main.
run_game()