#Coding in Python Part 1

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixels = neopixel.NeoPixel(board.A4, 5, brightness=.9, auto_write=True)

while True:
    for pixel in range(0,5):
        print(pixel)
