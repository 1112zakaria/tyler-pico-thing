"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
"""

import audiopwmio
import random
import config
from song_wrapper import *


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
    play_random_audio()
