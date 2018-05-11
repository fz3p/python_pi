from vrtneopixel import *
import time

LED_COUNT       = 64
LED_PIN         = 18
LED_FREQ        = 80000
LED_DMA         = 5
LED_BRIGHTNESS  = 8
LED_INVERT      = False

# function
def clearScreen(leds):
    for i in range(64):
        leds[i]= Color(0,0,0)

def displayScreen (strip, leds):
    for i in range(64):
        strip.setPixelColor(i, leds[i])
    strip.show()

def addSnake(snake,leds):
    for x, y in snake:
        leds[x + y * 8] = Color(0, 255, 0)

def removeSnake(snake, leds):
    for x, y in snake:
        leds[x + y * 8] = Color(0, 0, 0)

def snakeUp(snake):
    snake.pop ()
    newLed_x, newLed_y = snake[0]
    if newLed_y == 0:
        newLed_y = 7
    else:
        newLed_y = newLed_y - 1
    snake.insert(0, (newLed_x, newLed_y))

def snakeDown(snake):
    snake.pop ()
    newLed_x, newLed_y = snake[0]
    if newLed_y == 7:
        newLed_y = 0
    else:
        newLed_y = newLed_y + 1
    snake.insert(0, (newLed_x, newLed_y))
    

if __name__ == '__main__':
    # create snake
    snake = [(2,3),(2,4),(2,5)]
    # create array
    leds = [Color(0, 0, 0)] * 64
    # nbr maximum
    maxi = 99


    # initialize screen
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ, LED_DMA, LED_BRIGHTNESS, LED_INVERT)
    strip.begin()

    while maxi > 0:
        addSnake(snake, leds)
        displayScreen(strip, leds)
        time.sleep(0.1)
        removeSnake(snake, leds)
        snakeDown(snake)
        maxi = maxi - 1


  

    # wait 10 second and reinitialize
    time.sleep(10)
    clearScreen(leds)
    displayScreen(strip, leds)


