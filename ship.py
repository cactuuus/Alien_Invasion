"""Dictates the player's ship appearance and behaviour."""
import pygame
from pygame.sprite import Sprite
from time import sleep

class Ship(Sprite):
    """A class representing the player's ship."""

    def __init__(self, screen, settings, audio=None):
        """Initialises the ship and set its starting position."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.audio = audio
        
        # Loads the image and gets its rect.
        self.main_sprite =  pygame.image.load("images/player_ship.bmp")
        self.image = self.main_sprite
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starts each new ship at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        # Stores a decimal value for the ship's center.
        self.center = {"x" : float(self.rect.centerx),
                       "y" : float(self.rect.centery)}

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Exploding animation.
        self.explosion_sprites = []
        self.load_explosion_sprites()

    def update(self):
        """Updates the ship's position based on the movement flag."""
        # Updates the ship's value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center["x"] += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center["x"] -= self.settings.ship_speed_factor

        # Update rect object based on the self.center value.
        self.rect.centerx = self.center["x"]
        self.rect.centery = self.center["y"]

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Resets the ship's image and centers it to the screen."""
        self.image = self.main_sprite
        self.center["x"] = self.screen_rect.centerx
    
    def cannon_sound(self):
        """Plays the cannon sound effect."""
        self.audio.play(self.audio.ship_cannon)

    def explode(self):
        """Animation of the ship exploding."""
        self.audio.play(self.audio.ship_hit)

        # Cycle through each frame of the explosion animation and 
        # updates the screen.        
        for explosion_sprite in self.explosion_sprites:
            self.image = explosion_sprite
            self.screen.blit(self.settings.bg_image, self.screen.get_rect())
            self.blitme()
            pygame.display.update(self.rect)
            self.settings.clock.tick(120)
            sleep(0.1)

        # Briefly pauses the game, then clear the event queue from key
        # presses done during the animation.
        sleep(0.5)
        pygame.event.clear(pygame.KEYDOWN)

    def load_explosion_sprites(self):
         frame_no = 0
         while True:
            try:
                self.explosion_sprites.append(
                    pygame.image.load(f"images/ship_hit/{frame_no}.png"))
            except FileNotFoundError:
                break
            frame_no += 1