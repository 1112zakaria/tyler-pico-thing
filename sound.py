"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
"""
import board
import audiomp3
import audiocore
import audiopwmio
import random

class SongWrapper():
    def get_decoder(self):
        return None

class MP3Wrapper(SongWrapper):
    def __init__(self, path):
        self.path = path
    def get_decoder(self):
        return audiomp3.MP3Decoder(open(self.path, "rb"))

class WavWrapper(SongWrapper):
    def __init__(self, path):
        self.path = path
    def get_decoder(self):
        return audiocore.WaveFile(open(self.path, "rb"))


# Pin Configurations & Other stuff for Tyler
# If you want to change where you plug stuff in,
# you can modify the code here
# You can also update the list of songs, wrap it
# accordingly whether its MP3 or WAV
speaker_pin = board.GP13
wrapped_song_files = [
    MP3Wrapper("slow.mp3"),
    WavWrapper("The_Boondocks_I_Want_My_Money.wav")
]
# End of pin configurations


def pick_random_song():
    random_idx = random.randint(0, len(wrapped_song_files) - 1)
    return wrapped_song_files[random_idx]

def play_audio():
    audio = audiopwmio.PWMAudioOut(speaker_pin)
    
    random_song = pick_random_song()
    decoder = random_song.get_decoder()

    audio.play(decoder)
    while audio.playing:
        pass

    print("Done playing!")

if __name__ == "__main__":
    play_audio()
