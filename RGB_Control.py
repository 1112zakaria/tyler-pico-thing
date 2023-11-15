import sound
import config
import card_reader


def tyler_card_detector_callback(card):
    if card == config.TYLER_CARD_UID:
        print("Card ID: "+ str(card)+" PASS: Green Light Activated")
        if config.PLAY_RANDOM_ON_GREEN:
            sound.play_random_audio()
        else:
            sound.play_audio(config.GREEN_CARD_SONG)
        
    else:
        print("Card ID: "+ str(card)+" UNKNOWN CARD! Red Light Activated")
        if config.PLAY_RANDOM_ON_UNKNOWN:
            sound.play_random_audio()
        else:
            sound.play_audio(config.UNKNOWN_CARD_SONG)
 

if __name__ == "__main__":
    while True:
        print("Bring RFID TAG Closer...")
        print("")
        card_reader.read_card(tyler_card_detector_callback)
      