import config
from cpy_mfrc522 import MFRC522

reader = MFRC522(
    sck=config.SCK_PIN,
    mosi=config.MOSI_PIN,
    miso=config.MISO_PIN,
    rst=config.RST_PIN,
    cs=config.CS_PIN
)

def read_card(callback_func: function):
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, raw_uid) = reader.anticoll()
        if reader.select_tag(raw_uid) == reader.OK:
            card = int.from_bytes(bytes(raw_uid),"little")
            # perform some sort of function with card uid
            # the function must take an int uid as argument
            callback_func(card)