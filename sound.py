"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
"""
import board
import audiomp3
import audiopwmio
import random

def pick_random_song():
    # add more song files here.
    song_files = [
        "slow.mp3",
    ]

    random_idx = random.randint(0, len(song_files) - 1)
    return song_files[random_idx]

def play_audio():
    audio = audiopwmio.PWMAudioOut(board.GP0)
    
    random_song = pick_random_song()
    decoder = audiomp3.MP3Decoder(open(random_song, "rb"))

    audio.play(decoder)
    while audio.playing:
        pass

    print("Done playing!")

if __name__ == "__main__":
    play_audio()
