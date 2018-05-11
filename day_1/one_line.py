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

# show all leds
for i in range(64):
    strip.setPixelColor(i, leds[i])
strip.show()

# wait 10 second
time.sleep(10)

for i in range(8):
    leds[i] = Color(0,0,0)

# show all leds
for i in range(64):
    strip.setPixelColor(i, leds[i])
strip.show()
