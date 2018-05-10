from vrtneopixel import *
import time

LED_COUNT       = 64
LED_PIN         = 18
LED_FREQ        = 80000
LED_DMA         = 5
LED_BRIGHTNESS  = 8
LED_INVERT      = False

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ, LED_DMA, LED_BRIGHTNESS, LED_INVERT)

strip.begin()
strip.setPixelColor(0, Color(255,0,0))
strip.show()

time.sleep(10)

