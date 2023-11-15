Rough notes:

rfid reads some sorta card
if rfid is detected, play a noise
play custom sound preferable

items:
raspberry pi pico
breadboard
rfid reader, model: RC522
speaker, headset speaker 8ohm
python, IDE - thonny

first 3 work together (mfrc522.py, data_read.py, RGB_control.py ?)
last 2 dont together (RGB_control.py, sound.py)

problem: RBG_control.py doesn't do what is wanted. currently does lights but instead of lights it does sound. Tyler found sound code but wants to combine the Card check functionality to do something else

extension:
- play a random sound based on a library of sounds given

new problem:
- sound.py uses circuitpython
- mfrc522.py uses micropython
- conflict in python types

Found this library mfrc522 card reader for circuitpython: https://github.com/domdfcoding/circuitpython-mfrc522
- Refer to the examples here to learn how to use the library: https://github.com/domdfcoding/circuitpython-mfrc522/tree/master/examples

Note: this library above seems to depend on adafruit-circuitpython-busdevice, which is not
built into CircuitPython and can be installed using the following instructions:
https://docs.circuitpython.org/projects/busdevice/en/latest/index.html#bus-device-installation

but.... it might also already be built-in? I do not know. You'd have to run it to figure it out.

Requirements for porting codebase to CircuitPython:
- machine is a micropython library, therefore you need get rid of all
references to this library
- board is a circuitpython library, you can keep this.

To determine which board pins to use, I used the Raspberry Pi Pico Datasheet:
https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf