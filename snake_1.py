import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint


WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100


class Snake(object):
    # docstring for Snake.

    # This is the dictionary for key inputs
    # reverse direction map
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
            self.body_list.append(Body(x - element, y))

        # Define and append the snakes head
        self.body_list.append(Body(x, y, '0'))
        # Define the window
        self.window = window
        # Move the snake to the right when the game starts
        self.direction = KEY_RIGHT
        # Set the snakes last head coordinate
        self.last_head_coor = (x, y)
        # Define the direction map
        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
        }

    @property
    def score(self):
        return ("Score: {}".format(self.hit_score))

    # Adds the snake body
    def add_body(self, body_list):
        self.body_list.extend(body_list)

    def eat_food(self, food):
        # Reset food
        food.reset()
        # Add on the new body part
        body = Body(self.last_head_coor[0], self.last_head_coor[1])
        self.body_list.insert(-1, body)
        # Update game Score
        self.hit_score += 1

        if self.hit_score % 3 == 0:
            self.timeout -= 5
            self.window.timeout(self.timeout)

    @property
    def collided(self):
        return any([body.coor == self.head.coor
                    for body in self.body_list[: -1]])

    def update(self):
        # remove and return the last object from the list
        last_body = self.body_list.pop(0)
        # Setting the head
        last_body.x = self.body_list[-1].x
        last_body.y = self.body_list[-1].y
        self.body_list.insert(-1, last_body)
        # Set the last head coordinate
        self.last_head_coor = (self.head.x, self.head.y)

        self.direction_map[self.direction]()

    # Change direction
    def change_direction(self, direction):
        # Get the REV_DIR_MAP
        if direction != Snake.REV_DIR_MAP[self.direction]:
            self.direction = direction

    # Make the render function
    def render(self):
        for body in self.body_list:
            self.wondow.addstr(body.y, body.x, body.char)

    @property
    # Define the snake head
    def head(self):
        return self.body_list[-1]

    @property
    def coor(self):
        return self.head.x, self.head.y

    # Move up function
    def move_up(self):
        self.head.y -= 1
        if self.head.y < 1:
            self.head.y = MAX_Y

    # Move down function
    def move_down(self):
        self.head.y += 1
        if self.head.y > MAX_Y:
            self.head.y = 1

    # Move left function
    def move_left(self):
        self.head.x -= 1
        if self.head.x < 1:
            self.head.x = MAX_X

    # Move right function
    def move_right(self):
        self.head.x += 1
        if self.head.x > MAX_X:
            self.head.x = 1


class Body(object):
    """docstring for Body."""

    # Initialize the body
    def __init__(self, x, y, char='='):
        self.x = x
        self.y = y
        self.char = char

    @property
    # Set the coordinate
    def coor(self):
        return self.x, self.y


class Food(object):
    # Initialize Food
    def __init__(self, window, char='*'):
        # Have food appear in a random position
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        self.char = char
        self.window = window

    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    # Resets the food to a new random location when eaten
    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)

# Directing python to the main source file so it can properly execute the code


if __name__ == '__main__':

    # Initialize curses
    curses.initscr()
    curses.beep()
    curses.beep()

    # Make the curses window
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    # Set window time out
    window.timeout(TIMEOUT)
    # Set keypad
    window.keypad(1)

    curses.noecho()
    # Set viibility
    curses.curs_set(0)
    # Set window border
    window.border(0)

    # Get the Snake and Food objects
    snake = Snake(SNAKE_X, SNAKE_Y, window)
    food = Food(window, '*')

    while True:
        # Clear the window
        window.clear()
        # Set the border
        window.border(0)
        # Render the snake
        snake.render()
        # Render the Food
        food.render()

        window.addstr(0, 5, snake.score)
        event = window.getch()

    curses.endwin()
