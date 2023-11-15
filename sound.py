"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
"""
import board
import audiomp3
import audiocore
import audiopwmio
import random
import config

class SongWrapper():
    """
    Parent class of song file wrapper sub-classes.
    Defines the methods that should be implemented in
    subclasses. This class should not be instantiated.
    """
    def __init__(self, path):
        self.path = None
        self.decoder = None
    def get_decoder(self):
        return None
    def deinit(self):
        return None
    def get_song(self):
        return None

class MP3Wrapper(SongWrapper):
    """
    Wrapper for MP3 audio files.
    """
    def __init__(self, path):
        self.path = path
        self.decoder = None
    def get_decoder(self):
        self.decoder = audiomp3.MP3Decoder(self.path)
    def deinit(self):
        if self.decoder is not None:
            self.decoder.deinit()
    def get_song(self):
        return self.path

class WavWrapper(SongWrapper):
    """
    Wrapper for WAV audio files.
    """
    def __init__(self, path):
        self.path = path
        self.decoder = None
    def get_decoder(self):
        self.decoder = audiocore.WaveFile(self.path)
        return self.decoder
    def deinit(self):
        if self.decoder is not None:
            self.decoder.deinit()
    def get_song(self):
        return self.path


def pick_random_song():
    random_idx = random.randint(0, len(config.RANDOM_SONG_FILES) - 1)
    return config.RANDOM_SONG_FILES[random_idx]

def play_random_audio():
    random_song = pick_random_song()
    play_audio(random_song)

def play_audio(songWrapperObj: SongWrapper):
    audio = audiopwmio.PWMAudioOut(config.SPEAKER_PIN)
    
    decoder = songWrapperObj.get_decoder()

    print("Playing " + songWrapperObj.get_song())
    audio.play(decoder)
    while audio.playing:
        pass
    
    # call deinit method to free hardware resources for reuse
    decoder.deinit()
    audio.deinit()

    print("Done playing!")

if __name__ == "__main__":
    play_audio()
