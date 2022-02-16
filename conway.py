"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(width, height):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, width*height, p=[0.2, 0.8]).reshape(width, height)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, grid, width, height):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = np.zeros(width*height).reshape(width, height)

    # TODO: Implement the rules of Conway's Game of Life
    for x in range(width):
        for y in range(height):
            neighbours = 0
            for row in range(x-1, x+2):
                if row >= 0 and row < width:
                    for col in range(y-1, y+2):
                        if col >= 0 and col < height:
                            if not (x == row and y == col) and grid[row, col] == ON: neighbours += 1

            if grid[x, y] == ON:
                if neighbours == 3 or neighbours == 2: newGrid[x, y] = ON
                else: newGrid[x, y] = OFF
            elif neighbours == 3: newGrid[x, y] = ON
            

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img, 

def input_file():
    file = open("Input.txt", "r")
    lines = file.read().split("\n")
    width, height = int(lines[0].split(" ")[0]), int(lines[0].split(" ")[1])
    generations = int(lines[1])
    grid = np.zeros(width*height).reshape(width, height)
    for line in lines[2:]:
        x, y = int(line.split(" ")[0]), int(line.split(" ")[1])
        grid[x, y] = ON
    file.close()
    return width, height, generations, grid

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    read_file = True
    if read_file:
        width, height, generations, grid = input_file()
    else:
        #declare size of universe
        width = int(input("Width of universe (default 100): "))
        height = int(input("Height of universe (default 100): "))

        # declare number of generations
        generations = int(input("Number of generations (default 200): "))
        
        # declare grid
        grid = np.array([])
        # populate grid with random on/off - more off than on
        grid = randomGrid(width, height)

    # set animation update interval
    updateInterval = 50

    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(N*N).reshape(N, N)
    #addGlider(1, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, width, height, ),
                                  frames = generations,
                                  interval=updateInterval,
                                  save_count=100,
                                  repeat=False)
    plt.show()

# call main
if __name__ == '__main__':
    main()