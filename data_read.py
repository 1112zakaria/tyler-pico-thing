from cpy_mfrc522 import MFRC522
import board
 
reader = MFRC522(
    sck=board.GP6,
    mosi=board.GP7,
    miso=board.GP4,
    rst=board.GP22,
    cs=board.GP5
)
 
print("Bring TAG closer...")
print("")
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, raw_uid) = reader.anticoll()
        if reader.select_tag(raw_uid) == reader.OK:
            card = int.from_bytes(bytes(raw_uid),"little")
            print("CARD ID: "+str(card))
 