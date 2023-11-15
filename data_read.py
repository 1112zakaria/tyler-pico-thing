from cpy_mfrc522 import MFRC522
import config
 
reader = MFRC522(
    sck=config.SCK_PIN,
    mosi=config.MOSI_PIN,
    miso=config.MISO_PIN,
    rst=config.RST_PIN,
    cs=config.CS_PIN
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
 