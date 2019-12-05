#Coding in Python Part 2

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixels = neopixel.NeoPixel(board.A4, 5, brightness=.9, auto_write=True)

for pixel in range(0,5):
    print(pixel)
    pixels[pixel] = (100, 0, 0)
    time.sleep(2)

print(pixel)
pixel = 1
print(pixel)

while True:
    pixels[0] = (255, 0, 0)
