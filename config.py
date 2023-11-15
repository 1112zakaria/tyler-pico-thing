import board
import song_wrapper

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
    song_wrapper.MP3Wrapper("slow.mp3"),
    song_wrapper.WavWrapper("The_Boondocks_I_Want_My_Money.wav"),
    song_wrapper.WavWrapper("He_got_money.wav"),
    song_wrapper.WavWrapper("broke.wav")
]

GREEN_CARD_SONG = song_wrapper.MP3Wrapper("slow.mp3")
BLUE_CARD_SONG = song_wrapper.WavWrapper("The_Boondocks_I_Want_My_Money.wav")
UNKNOWN_CARD_SONG = song_wrapper.WavWrapper("broke.wav")

PLAY_RANDOM_ON_GREEN       = True
PLAY_RANDOM_ON_UNKNOWN     = False

# Tyler's Card UID
TYLER_CARD_UID              = 111583217