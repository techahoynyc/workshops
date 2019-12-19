#Coding in Python Part 3

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixels = neopixel.NeoPixel(board.A4, 5, brightness=.9, auto_write=True)

button = DigitalInOut(board.A3)
button.direction = Direction.INPUT
button.pull = Pull.UP

def startTimer():
    for pixel in range(0,5):
        pixels[pixel] = (0, 100, 20)
        time.sleep(0.5)

def bulbOn():
    for bulb in range(0,5):
        pixels[bulb] = (0,20,0)
    time.sleep(0.5)

def bulbOff():
    for bulb in range(0,5):
        pixels[bulb] = (0,0,0)
    time.sleep(0.5)

def effectWipeOut():
    bulbOff()
    for sequence in range(0,3):
        pixel1 = 2 - sequence
        pixel2 = 2 + sequencea
        pixels[pixel1] = (0, 20, 0)
        pixels[pixel2] = (0, 20, 0)
        time.sleep(0.5)
        pixels[pixel1] = (0 , 0, 0)
        pixels[pixel2] = (0 , 0, 0)
        time.sleep(0.2)

def knightRider():
    for sequence in range(0,4):
        print(sequence)
        pixels[sequence + 0] = (0, 20, 0)
        pixels[sequence + 1] = (0, 20, 0)
        if sequence != 3:
            pixels[sequence + 2] = (0, 20, 0)
        time.sleep(0.2)
        pixels.fill((0,0,0))
    for sequence in range(0,3):
        print(sequence)
        pixels[4 - sequence] = (0, 20, 0)
        pixels[3 - sequence] = (0, 20, 0)
        pixels[2 - sequence] = (0, 20, 0)
        time.sleep(0.2)
        pixels.fill((0,0,0))


def restPeriod():
    period = 0
    while period < 3:
        #effectWipeOut()
        knightRider()
        period = period + 1


while True:
    buttonUp = button.value
    buttonDown = not buttonUp
    if buttonDown:
        print("buttonDown")
        startTimer()
        restPeriod()

    time.sleep(0.5)
