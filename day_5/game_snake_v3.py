from vrtneopixel import *
import time
import random
import curses

LED_COUNT       = 64
LED_PIN         = 18
LED_FREQ        = 80000
LED_DMA         = 5
LED_BRIGHTNESS  = 8
LED_INVERT      = False

# function
# screen
def clearScreen(leds):
    for i in range(64):
        leds[i]= Color(0,0,0)

def displayScreen (strip, leds):
    for i in range(64):
        strip.setPixelColor(i, leds[i])
    strip.show()


#generique
def addElement(elt, leds, color):
    for (x, y) in elt:
        leds[x + y * 8] = color

# snake
def addSnake(snake,leds):
    addElement(snake, leds, Color(0, 255, 0))

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

def die(snake, leds, strip):
    for nb in range(5):
        for i in range(50):
            addElement(snake, leds, Color(0, 255-i*5, 5+i*5))
            displayScreen(strip, leds)
            time.sleep(0,1)
        for i in range(50):
            addElement(snake, leds, Color(0, 5+i*5, 255-i*5))
            displayScreen(strip, leds)
            time.sleep(0,1)

def isDead(snake):
    return snake[0] in snake[1:]
            

# food
def addFood(food, leds):
    addElement(food, leds, Color(255, 255, 0))

def detectFood(food, snakeHead):
    return snakeHead in food

def digestedFood(food, digest, snake):
    for food in digest:
        if food not in snake:
            digest.remove(food)
            snake.append(food)

# wall
def addWall(wall, leds):
    addElement(wall, leds, Color(255, 0, 0))

def detectWall(wall, snakeHead):
    return snakeHead in wall


# win
def isWinner(food, digest):
    return len(food) == 0 and len(digest) == 0

def displayBox(size, color, leds):
    for x in range(size, 8-size):
        for y in range(size, 8 - size):
            leds[x+y*8]=color

def victory(leds, strip):
    clearScreen(leds)
    displayScreen(strip, leds)
    for nb in range(5):
        for size in range(4):
            displayBox(size, Color(255-40*size, 50*size, 0), leds)
            displayScreen(strip, leds)
            time.sleep(0.2)
        for size in range(4, 0, -1):
            displayBox(size, Color(0,0,0), leds)
            displayScreen(strip, leds)
            time.sleep(0.2)
            
# unauthorized direction
def changeDirection(direction, newDirection):
    unauthorized = [1,0,3,2]
    if newDirection != unauthorized[direction]:
        return newDirection
    else:
        return direction


# start curses
def initCurses():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    stdscr.nodelay(1) # auto
    return stdscr

# close curses
def closeCurses(stdscr):
    stdscr.keypad(0)
    curses.nobreak()
    curses.echo()
    curses.endwin()
    

if __name__ == '__main__':
    # create snake
    snake = [(2,3),(2,4),(2,5)]
    # create food
    food = [(1,1),(5,3),(6,7)]
    # create Wall
    wall = [(0,0), (1,0), (7,7), (7,6), (3,3), (3,4)]
    # estomac
    estomac=[]
    #create array
    leds = [Color(0, 0, 0)] * 64

    direction = 0
    newDirection = direction


    # initialize screen
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ, LED_DMA, LED_BRIGHTNESS, LED_INVERT)
    strip.begin()

    stdscr = initCurses()

    while True:
        addSnake(snake, leds)
               
        # detect if snake eat
        if detectFood(food, snake[0]):
            estomac.append(snake[0])
            food.remove(snake[0])
        # detect Wall
        if detectWall(wall, snake[0]):
            die(snake, leds, strip)
            break

        digestedFood(food, estomac, snake)
        
        # add element
        addWall(wall, leds)                
        addFood(food, leds)
        displayScreen(strip, leds)
        time.sleep(0.1)

        if isDead(snake):
            die(snake, leds, strip)
            break

        if isWinner(food, estomac):
            victory(leds, strip)
            break
        
        removeSnake(snake, leds)
        deplacement = stdscr.getch()
        stdscr.refresh()

        if deplacement == curses.KEY_UP:
            newDirection = 0
        elif deplacement == curses.KEY_DOWN:
            newDirection = 1
        elif deplacement == curses.KEY_RIGHT:
            newDirection = 2
        elif deplacement == curses.KEY_LEFT:
            newDirection = 3
        elif deplacement == 27:
            closeCurses(stdscr)
            break       

        direction = changeDirection(direction, newDirection)
        
        if direction == 0:
            snakeUp(snake)
        elif direction == 1:
            snakeDown(snake)
        elif direction == 2:
            snakeRight(snake)
        elif direction == 3:
            snakeLeft(snake)

    # reinitialize
    clearScreen(leds)
    displayScreen(strip, leds)
