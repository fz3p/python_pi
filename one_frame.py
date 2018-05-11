from vrtneopixel import *
import time

LED_COUNT       = 64
LED_PIN         = 18
LED_FREQ        = 80000
LED_DMA         = 5
LED_BRIGHTNESS  = 8
LED_INVERT      = False

# initialize screen
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ, LED_DMA, LED_BRIGHTNESS, LED_INVERT)
strip.begin()

# create array
leds = [Color(0, 0, 0)] * 64

# color first line
for i in range(8):
    leds[i] = Color(255,0,0)

# color last line
for i in range(8):
    leds[56+i]=Color(255,0,0)

# color first column and last column
for i in range(1, 7):
    leds[8*i]=Color(255,0,0)
    leds[8*i+7]=Color(255,0,0)

# show all leds
for i in range(64):
    strip.setPixelColor(i, leds[i])
strip.show()

# wait 10 second
time.sleep(10)

# reinitialize
for i in range(64):
    leds[i] = Color(0,0,0)

# show all leds
for i in range(64):
    strip.setPixelColor(i, leds[i])
strip.show()
