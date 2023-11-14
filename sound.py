"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
"""
import audiomp3
import audiopwmio
import board

def play_audio():
    audio = audiopwmio.PWMAudioOut(board.GP13)

    decoder = audiomp3.MP3Decoder(open("slow.mp3", "rb"))

    audio.play(decoder)
    while audio.playing:
        pass

    print("Done playing!")

if __name__ == "__main__":
    play_audio()
