#Coding in Python Part 2

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixels = neopixel.NeoPixel(board.A4, 5, brightness=.9, auto_write=True)

button = DigitalInOut(board.A3)
button.direction = Direction.INPUT
button.pull = Pull.UP

while True:
    buttonUp = button.value
    buttonDown = not buttonUp
    if buttonDown:
        for pixel in range(0,5):
            pixels[pixel] = (0, 100, 0)
    time.sleep(.2)
