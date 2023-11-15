import board
import sound

# RF Card Reader Pin Layouts
SCK_PIN     = board.GP6
MOSI_PIN    = board.GP7
MISO_PIN    = board.GP4
RST_PIN     = board.GP22
CS_PIN      = board.GP5

# Speaker Pin Layouts
SPEAKER_PIN = board.GP13

# Song File Objects
# These will be used by sound.play_random_audio()
RANDOM_SONG_FILES = [
    sound.MP3Wrapper("slow.mp3"),
    sound.WavWrapper("The_Boondocks_I_Want_My_Money.wav"),
    sound.WavWrapper("He_got_money.wav"),
    sound.WavWrapper("broke.wav")
]

GREEN_CARD_SONG = sound.MP3Wrapper("slow.mp3")
BLUE_CARD_SONG = sound.WavWrapper("The_Boondocks_I_Want_My_Money.wav")
UNKNOWN_CARD_SONG = sound.WavWrapper("broke.wav")

PLAY_RANDOM_ON_GREEN       = True
PLAY_RANDOM_ON_UNKNOWN     = False