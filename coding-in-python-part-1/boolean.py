#Coding in Python Part 1

import time
import board
import adafruit_dotstar

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
# Range: 0.05 - 1
led.brightness = 0 #0 to turn off

programRunning = True

print (programRunning)
print (not programRunning)

while True:
    led[0] = (255, 0, 0)
