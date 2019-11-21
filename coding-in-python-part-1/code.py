import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixels = neopixel.NeoPixel(board.A4, 5, brightness=.9, auto_write=True)

button = DigitalInOut(board.A3) #pin 0 on the board
button.direction = Direction.INPUT
button.pull = Pull.UP

def blinkRest():
    count = 0
    while (count < 5):
        for i in range(0,5):
            pixels[i] = (0, 100, 0)
            time.sleep(.5)
        for i in range(0,5):
            pixels[i] = (0, 0, 0)
            time.sleep(.5)
        count+=1

while True:
    buttonClicked = not button.value
    if buttonClicked:
        for i in range(0,5):
            pixels[i] = (0, 0, 100)
            time.sleep(5)

        blinkRest()

        for i in range(0,5):
            pixels[i] = (0,0,0)
    time.sleep(.2)
