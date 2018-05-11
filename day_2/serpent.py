from vrtneopixel import *
import time
import random

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

def snakeRight(snake):
    snake.pop()
    newLed_x, newLed_y = snake[0]
    if newLed_x == 7:
        newLed_x = 0
    else:
        newLed_x = newLed_x + 1
    snake.insert(0, (newLed_x, newLed_y))

def snakeLeft(snake):
    snake.pop()
    newLed_x, newLed_y = snake[0]
    if newLed_x == 0:
        newLed_x = 7
    else:
        newLed_x = newLed_x - 1
    snake.insert(0, (newLed_x, newLed_y))

# random direction
def changeDirection(direction):
    unauthorized = [1, 0, 3, 2]
    while True:
        newDirection = random.randint(0,3)
        if newDirection != unauthorized[direction]:
            return newDirection

if __name__ == '__main__':
    # create snake
    snake = [(2,3),(2,4),(2,5)]
    # create array
    leds = [Color(0, 0, 0)] * 64
    # nbr maximum
    maxi = 99
    # direction
    direction = 0


    # initialize screen
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ, LED_DMA, LED_BRIGHTNESS, LED_INVERT)
    strip.begin()

    while maxi > 0:
        addSnake(snake, leds)
        displayScreen(strip, leds)
        time.sleep(0.1)
        removeSnake(snake, leds)

        if maxi % 5 == 0:
            direction = changeDirection(direction)

        if direction == 0:
            snakeUp(snake)
        elif direction == 1:
            snakeDown(snake)
        elif direction == 2:
            snakeRight(snake)
        elif direction == 3:
            snakeLeft(snake)

        maxi = maxi - 1


  

    # wait 10 second and reinitialize

    clearScreen(leds)
    displayScreen(strip, leds)


