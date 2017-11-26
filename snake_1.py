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
    def __init__(self):
        slef.x = "Hisss!"

    def method_a(self, foo):
        print (self.x + ' ' + foo)


snake = Snake();
snake.method_a("Says the snake")
