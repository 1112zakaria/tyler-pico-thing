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