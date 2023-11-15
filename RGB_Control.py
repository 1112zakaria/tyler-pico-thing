from cpy_mfrc522 import MFRC522
import sound
import config

reader = MFRC522(
    sck=config.SCK_PIN,
    mosi=config.MOSI_PIN,
    miso=config.MISO_PIN,
    rst=config.RST_PIN,
    cs=config.CS_PIN
)

print("Bring RFID TAG Closer...")
print("")
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, raw_uid) = reader.anticoll()
        if reader.select_tag(raw_uid) == reader.OK:
            card = int.from_bytes(bytes(raw_uid),"little")
            
            if card == 111583217:
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
      