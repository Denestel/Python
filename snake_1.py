import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint


WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH-2
MAX_Y = HEIGHT-2
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH+1
SNAKE_Y = 3
TIMEOUT = 100

class Snake(object):
    """docstring for Snake."""

    #This is the dictionary for key inputs
    #reverse direction map
    REV_DIR_MAP = {
        KEY_UP: KEY_DOWN,
        KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT,
        KEY_RIGHT: KEY_LEFT
    }

    def __init__(self, x, y, window):
        self.body_list = []
        self.hit_score = 0
        self.timeout = TIMEOUT

        for element in range(SNAKE_LENGTH, 0, -1):
            self.body_list.append(Body(x-element, y))

        #Define and append the snakes head
        self.body_list.append(Body(x, y, '0'))
        #Define the window
        self.window = window
        #Move the snake to the right when the game starts
        self.direction = KEY_RIGHT
        #Set the snakes last head coordinate
        self.last_head_coor = (x, y)
        #Define the direction map
        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
        }

    @property
    def score(self):
        return ("Score: {}".format(self.hit_score))

class Body(object):
    """docstring for Body."""

    #Initialize the body
    def __init__(self, x, y, char = '='):
        self.x = x
        self.y = y
        self.char = char

    @property
    #Set the coordinate
    def coor(self):
        return self.x, self.y

class Food(object):
    #Initialize Food
    def __init__(self, window, char = '*'):
        #Have food appear in a random position
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        self.char = char
        self.window = window

    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
