from pygame import mixer

class Audio():
    """A class that contains the music and sounds effect of the game."""
    def __init__(self):
        """Initialises the game's audio"""
        self.init_bg_music()

        # Sound effects.
        self.ship_cannon = mixer.Sound("audio/ship_cannon.wav")
        self.ship_hit = mixer.Sound("audio/ship_hit.wav")
        self.alien_laser = mixer.Sound("audio/alien_laser.wav")
        self.alien_hit = mixer.Sound("audio/alien_hit.wav")

    def init_bg_music(self):
        """Loads and plays the background music."""
        mixer.music.load("audio/bg_music.wav")
        mixer.music.set_volume(0.3)
        mixer.music.play(loops=-1, fade_ms=1500)

    def play(self, sound):
        mixer.Sound.play(sound)