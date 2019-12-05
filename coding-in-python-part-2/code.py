#Coding in Python Part 2

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixels = neopixel.NeoPixel(board.A4, 5, brightness=.9, auto_write=True)

while True:
    pixels[0] = (255, 0, 0)
