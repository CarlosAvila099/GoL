"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from tabulate import tabulate
from datetime import date
from cells import *

ON = 255
OFF = 0
vals = [ON, OFF]

existances = {'spaceship':0, 'glider':0, 'blinker':0, 'toad':0, 'beacon':0, 'block':0, 'beehive':0, 'loaf':0, 'boat':0, 'tub':0}

def randomGrid(width, height):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, width*height, p=[0.2, 0.8]).reshape(width, height)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, grid, width, height, generations):
    global generation_array
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
    generation_array.append(newGrid.copy())
    if len(generation_array) == generations:
        report_lifes(width, height)
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

def report_lifes(width, height):
    global generation_array
    file_text = f"Simulation at {date.today()}\n"
    file_text += f"Universe size {width} X {height}\n\n"
    for num, gen in enumerate(generation_array):
        print(f"Analizing ({num + 1}/{len(generation_array)})")
        file_text += f"Iteration: {num + 1}\n"
        for key in existances.keys():
            existances[key] = 0
        for x in range(len(gen)):
            for y in range(len(gen[x])):
                if gen[x, y] == 255:
                    cell_type = find_life_type(x, y, gen)
                    if cell_type:
                        existances[cell_type] += 1
        total_lifes = max(sum(existances.values()), 1)
        file_text += tabulate([ ["", "Count", "Percent"],
                                ["Block", existances['block'], round(existances['block'] / total_lifes * 100, 2)],
                                ["Beehive", existances['beehive'], round(existances['beehive'] / total_lifes * 100, 2)],
                                ["Loaf", existances['loaf'], round(existances['loaf'] / total_lifes * 100, 2)],
                                ["Boat", existances['boat'], round(existances['boat'] / total_lifes * 100, 2)],
                                ["Tub", existances['tub'], round(existances['tub'] / total_lifes * 100, 2)],
                                ["Blinker", existances['blinker'], round(existances['blinker'] / total_lifes * 100, 2)],
                                ["Toad", existances['toad'], round(existances['toad'] / total_lifes * 100, 2)],
                                ["Beacon", existances['beacon'], round(existances['beacon'] / total_lifes * 100, 2)],
                                ["Glider", existances['glider'], round(existances['glider'] / total_lifes * 100, 2)],
                                ["LG sp ship", existances['spaceship'], round(existances['spaceship'] / total_lifes * 100, 2)],
                                ["----------", "----------", "----------"],
                                ["Total", total_lifes, ""]],
                                headers="firstrow", tablefmt="psql") + "\n\n"
    output = open("Output.txt", "w")
    output.write(file_text[:-2])
    print("Finished analyzing, please check output.txt.")

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    print("1.- Use configuration on file named Input.txt")
    print("2.- Enter values")
    out = False
    while not out:
        read_file = int(input("Enter your choice: "))
        if read_file == 1:
            width, height, generations, grid = input_file()
            out = True
        elif read_file == 2:
            #declare size of universe
            width = int(input("Width of universe (default 100): ") or 100 ) 
            height = int(input("Height of universe (default 100): ") or 100) 

            # declare number of generations
            generations = int(input("Number of generations (default 200): ") or 200)
            
            # declare grid
            grid = np.array([])
            # populate grid with random on/off - more off than on
            grid = randomGrid(width, height)
            out = True

    # set animation update interval
    updateInterval = 50

    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(N*N).reshape(N, N)
    #addGlider(1, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, width, height, generations, ),
                                  frames = generations,
                                  interval=updateInterval,
                                  save_count=100,
                                  repeat=False)
    plt.show()

# call main
if __name__ == '__main__':
    generation_array = []
    main()