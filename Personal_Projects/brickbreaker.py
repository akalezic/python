"""
File: brickbreaker.py
----------------
YOUR DESCRIPTION HERE
"""

import tkinter
import time
import random

# How big is the playing area?
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 8              # How many rows of bricks are there?
N_COLS = 10             # How many columns of bricks are there?
SPACING = 5             # How much space is there between each brick?
BRICK_START_Y = 50      # The y coordinate of the top-most brick
BRICK_HEIGHT = 20       # How many pixels high is each brick
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLS+1) * SPACING) / N_COLS

# Constants for the ball and paddle
BALL_SIZE = 40
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80

def main():
    # creates the canvas using the specified width and height
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Brick Breaker')
    # creates the bricks
    brick = make_bricks(canvas)
    # creates the ball
    ball = canvas.create_oval(280,380,320,420, fill = 'black')
    # creates the paddle
    paddle = canvas.create_rectangle(0, PADDLE_Y, PADDLE_WIDTH, CANVAS_HEIGHT - 20, fill="blue")

    # change in the ball's x direction
    dx = 10
    # change in the ball's y direction
    dy = 7
    while True:
        # TODO: 2. get the mouse location and react to it
        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(paddle, mouse_x, PADDLE_Y)

        # makes ball move and change direction when hitting the walls
        canvas.move(ball, dx, dy)
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            dx *= -1
        if hit_top_wall(canvas, ball):
            dy *= -1

        # if the ball hits the bottom wall the game quits
        if hit_bottom_wall(canvas,ball):
            break

        # TODO: 3. check if the ball hits the paddle, change its direction if it does
        if hit_brick_paddle(canvas, ball, paddle):
            dy *= -1
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1 / 50.)


# detects if the ball hits the brick or the paddle
def hit_brick_paddle(canvas, ball, paddle):
    ball_coords = canvas.coords(ball)
    # the list has four elements:
    x_1 = ball_coords[0]
    y_1 = ball_coords[1]
    x_2 = ball_coords[2]
    y_2 = ball_coords[3]
    # we can then get a list of all objects in that area
    results = canvas.find_overlapping(x_1, y_1, x_2, y_2)
    # if the ball hits the paddle then the function returns the results
    for object in results:
        if object == paddle or object == ball:
            return len(results) > 1
        # if the ball hits a brick then it deletes the brick
        else:
            canvas.delete(object)

def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0


def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0


def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH


def hit_bottom_wall(canvas, object):
    return get_bottom_y(canvas, object) >= CANVAS_HEIGHT


######## These helper methods use "lists" of the canvas coordinates ###########

def get_left_x(canvas, object):
    return canvas.coords(object)[0]


def get_top_y(canvas, object):
    return canvas.coords(object)[1]


def get_right_x(canvas, object):
    return canvas.coords(object)[2]


def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]
    canvas.mainloop()


def get_top_y(canvas, object):
    '''
    This friendly method returns the y coordinate of the top of an object.
    Recall that canvas.coords(object) returns a list of the object 
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 1 is the top-y
    '''
    return canvas.coords(object)[1]

def get_left_x(canvas, object):
    '''
    This friendly method returns the x coordinate of the left of an object.
    Recall that canvas.coords(object) returns a list of the object 
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 0 is the left-x
    '''
    return canvas.coords(object)[0]

def make_canvas(width, height, title):
    """
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

"""
creates the bricks with the number of specified rows and columns, fills them 
in with the colors of the list brick_colors
"""
def make_bricks(canvas):
    for row in range(N_ROWS):
        for col in range(N_COLS):
            x = col * (BRICK_WIDTH + SPACING)
            y = row * (BRICK_HEIGHT + SPACING)
            brick_colors = ['mediumblue', 'blue', 'royalblue', 'cornflowerblue',
                            'dodgerblue', 'deepskyblue', 'lightskyblue', 'skyblue']
            canvas.create_rectangle(x + SPACING, y + BRICK_START_Y, x + BRICK_WIDTH + SPACING,
                                    y + BRICK_START_Y + BRICK_HEIGHT, fill=brick_colors[row])

if __name__ == '__main__':
    main()
