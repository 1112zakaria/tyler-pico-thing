from cpy_mfrc522 import MFRC522
import sound
import board

# Stuff that Tyler can modify
RED_CARD_SONG = sound.MP3Wrapper("slow.mp3")
BLUE_CARD_SONG = sound.WavWrapper("The_Boondocks_I_Want_My_Money.wav")
UNKNOWN_CARD_SONG = sound.WavWrapper("broke.wav")
# End of stuff that Tyler can modify

reader = MFRC522(
    sck=board.GP6,
    mosi=board.GP7,
    miso=board.GP4,
    rst=board.GP22,
    cs=board.GP5
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
                sound.play_audio(RED_CARD_SONG)
                
            elif card == 495638547:
                print("Card ID: "+ str(card)+" PASS: Blue Light Activated")
                sound.play_audio(BLUE_CARD_SONG)
                
            else:
                print("Card ID: "+ str(card)+" UNKNOWN CARD! Red Light Activated")
                sound.play_audio(UNKNOWN_CARD_SONG)
      