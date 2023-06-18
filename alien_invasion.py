import pygame

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

    # Creates a ship.
    ship = Ship(screen, settings)

    # Starts the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(settings, screen, ship)

# Main.
run_game()