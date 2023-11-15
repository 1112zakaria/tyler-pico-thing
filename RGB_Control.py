from cpy_mfrc522 import MFRC522
import sound
import board

#reader = MFRC522(sck=6, mosi=7, miso=4, rst=22, cs=5)
# reader = MFRC522(
#     sck=board.GP4,
#     mosi=board.GP5,
#     miso=board.GP2,
#     rst=board.GP17,
#     cs=board.GP3
# )
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
            card = int.from_bytes(bytes(raw_uid),"little",False)
            
            if card == 111583217:
                print("Card ID: "+ str(card)+" PASS: Green Light Activated")
                sound.play_audio()
                
            elif card == 495638547:
                print("Card ID: "+ str(card)+" PASS: Blue Light Activated")
                
            else:
                print("Card ID: "+ str(card)+" UNKNOWN CARD! Red Light Activated")
      