import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Initialises the game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Creates a ship.
    ship = Ship(screen)

    # Starts the main loop for the game.
    while True:

        # Watches for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass though the loop.
        screen.fill(settings.bg_color)
        ship.blitme()

        # Makes the most recently drawn screen visible.
        pygame.display.flip()


# Main.
run_game()