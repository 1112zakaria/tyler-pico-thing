from machine import Pin
from mfrc522 import MFRC522
import utime
import sound
       
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
 
print("Bring RFID TAG Closer...")
print("")
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            
            if card == 111583217:
                print("Card ID: "+ str(card)+" PASS: Green Light Activated")
                red.value(0)
                green.value(1)
                blue.value(0)
                sound.play_audio()
                
            elif card == 495638547:
                print("Card ID: "+ str(card)+" PASS: Blue Light Activated")
                red.value(0)
                green.value(0)
                blue.value(1)
                
            else:
                print("Card ID: "+ str(card)+" UNKNOWN CARD! Red Light Activated")
                red.value(1)
                green.value(0)
                blue.value(0)   