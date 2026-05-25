"""This code is a Python port of David J. Eck's Mosaic class:
https://math.hws.edu/javanotes/source/chapter4/RandomMosaicWalk.java
"""

import mosaic
import random

# Constants for the grid
ROWS = 20
COLUMNS = 30
SQUARE_SIZE = 20

# Global variables to track the "disturbance"
current_row = ROWS // 2
current_col = COLUMNS // 2

def change_to_random_color(row, col):
    """Changes one square to a new randomly selected color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    mosaic.set_color(row, col, r, g, b)

def fill_with_random_colors():
    """Fills the window with randomly colored squares."""
    for row in range(ROWS):
        for col in range(COLUMNS):
            change_to_random_color(row, col)
            
def fill_with_black():
    """Fills the window with randomly colored squares."""
    for row in range(ROWS):
        for col in range(COLUMNS):
            mosaic.set_color(row, col, 0, 0, 0)
            
            
def increment_green(row, col):
    greenComp = mosaic.get_green(row, col)
    greenComp += 40
    if greenComp > 255:
        greenComp = 255
    mosaic.set_color(row, col, 0, greenComp, 0)

def random_move():
    """Moves the disturbance one space up, down, left, or right."""
    global current_row, current_col
    
    direction = random.randint(0, 3)
    
    if direction == 0:    # move up
        current_row -= 1
        if current_row < 0:
            current_row = ROWS - 1
    elif direction == 1:  # move right
        current_col += 1
        if current_col >= COLUMNS:
            current_col = 0
    elif direction == 2:  # move down
        current_row += 1
        if current_row >= ROWS:
            current_row = 0
    elif direction == 3:  # move left
        current_col -= 1
        if current_col < 0:
            current_col = COLUMNS - 1

def main():
    # 1. Open the window
    mosaic.open_window(ROWS, COLUMNS, SQUARE_SIZE)
    
    # 2. Fill the background
    #fill_with_random_colors()
    fill_with_black()
    
    # 3. Start the random walk loop
    while mosaic.is_open():
        #change_to_random_color(current_row, current_col)
        increment_green(current_row, current_col)
        random_move()
        mosaic.delay(5) # 5 millisecond delay

if __name__ == "__main__":
    main()