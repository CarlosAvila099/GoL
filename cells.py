# -*- coding: utf-8 -*-
"""
cells.py
The cells that exist in Conway's Game of Life
"""
import numpy as np

class Cell:
    def __init__(self, cell_type, cell_array):
        self.cell = cell_array
        self.__cell_type = cell_type
        self.__get_range()

    def __get_range(self):
        broken = False
        for comp_x in range(len(self.cell)):
            for comp_y in range(len(self.cell[comp_x])):
                if self.cell[comp_x, comp_y] == 255:
                    self.__start_y = 0 - comp_x
                    self.__end_y = len(self.cell) - comp_x
                    self.__start_x = 0 - comp_y
                    self.__end_x = len(self.cell[comp_x]) - comp_y
                    broken = True
                    break
            if broken:
                break

    def compare(self, x, y, grid):
        if np.array_equal(grid[y+self.__start_y:y+self.__end_y, x+self.__start_x:x+self.__end_x], self.cell): 
            grid[y+self.__start_y:y+self.__end_y, x+self.__start_x:x+self.__end_x] = 0
            return True
        else: return False

    def get_cell_type(self, extended=False):
        if extended: return self.__cell_type
        else: 
            temp_type = self.__cell_type
            if "_" in self.__cell_type:
                if "90" in self.__cell_type:
                    temp_type = temp_type[:-3]
                else:
                    temp_type = temp_type[:-4]
            temp_type = temp_type[:-1]
            return temp_type

# Spaceships
SPACESHIP1 = Cell('spaceship1', np.array([   [0, 0, 0, 0, 0, 0, 0],
                                            [0, 255, 0, 0, 255, 0, 0],
                                            [0, 0, 0, 0, 0, 255, 0],
                                            [0, 255, 0, 0, 0, 255, 0],
                                            [0, 0, 255, 255, 255, 255, 0],
                                            [0, 0, 0, 0, 0, 0, 0] ]))

SPACESHIP1_90 = Cell('spaceship1_90', np.rot90(SPACESHIP1.cell))
SPACESHIP1_180 = Cell('spaceship1_180', np.rot90(SPACESHIP1.cell, 2))
SPACESHIP1_270 = Cell('spaceship1_270', np.rot90(SPACESHIP1.cell, 3))

SPACESHIP2 = Cell('spaceship2', np.array([   [0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 255, 255, 0, 0],
                                            [0, 255, 255, 0, 255, 255, 0],
                                            [0, 255, 255, 255, 255, 0, 0],
                                            [0, 0, 255, 255, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0] ]))
SPACESHIP2_90 = Cell('spaceship2_90', np.rot90(SPACESHIP2.cell))
SPACESHIP2_180 = Cell('spaceship2_180', np.rot90(SPACESHIP2.cell, 2))
SPACESHIP2_270 = Cell('spaceship2_270', np.rot90(SPACESHIP2.cell, 3))

SPACESHIP3 = Cell('spaceship3', np.array([   [0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 255, 255, 255, 255, 0],
                                            [0, 255, 0, 0, 0, 255, 0],
                                            [0, 0, 0, 0, 0, 255, 0],
                                            [0, 255, 0, 0, 255, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0] ]))
SPACESHIP3_90 = Cell('spaceship3_90', np.rot90(SPACESHIP3.cell))
SPACESHIP3_180 = Cell('spaceship3_180', np.rot90(SPACESHIP3.cell, 2))
SPACESHIP3_270 = Cell('spaceship3_270', np.rot90(SPACESHIP3.cell, 3))
                    
SPACESHIP4 = Cell('spaceship4', np.array([   [0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 255, 255, 0, 0, 0],
                                            [0, 255, 255, 255, 255, 0, 0],
                                            [0, 255, 255, 0, 255, 255, 0],
                                            [0, 0, 0, 255, 255, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0] ]))
SPACESHIP4_90 = Cell('spaceship4_90', np.rot90(SPACESHIP4.cell))
SPACESHIP4_180 = Cell('spaceship4_180', np.rot90(SPACESHIP4.cell, 2))
SPACESHIP4_270 = Cell('spaceship4_270', np.rot90(SPACESHIP4.cell, 3))

# Gliders
GLIDER1 = Cell('glider1', np.array([ [0, 0, 0, 0, 0],
                                    [0, 0, 255, 0, 0],
                                    [0, 0, 0, 255, 0],
                                    [0, 255, 255, 255, 0],
                                    [0, 0, 0, 0, 0] ]))
GLIDER1_90 = Cell('glider1_90', np.rot90(GLIDER1.cell))
GLIDER1_180 = Cell('glider1_180', np.rot90(GLIDER1.cell, 2))
GLIDER1_270 = Cell('glider1_270', np.rot90(GLIDER1.cell, 3))

GLIDER2 = Cell('glider2', np.array([ [0, 0, 0, 0, 0],
                                    [0, 255, 0, 255, 0],
                                    [0, 0, 255, 255, 0],
                                    [0, 0, 255, 0, 0],
                                    [0, 0, 0, 0, 0] ]))
GLIDER2_90 = Cell('glider2_90', np.rot90(GLIDER2.cell))
GLIDER2_180 = Cell('glider2_180', np.rot90(GLIDER2.cell, 2))
GLIDER2_270 = Cell('glider2_270', np.rot90(GLIDER2.cell, 3))

GLIDER3 = Cell('glider3', np.array([ [0, 0, 0, 0, 0],
                                    [0, 0, 0, 255, 0],
                                    [0, 255, 0, 255, 0],
                                    [0, 0, 255, 255, 0],
                                    [0, 0, 0, 0, 0] ]))
GLIDER3_90 = Cell('glider3_90', np.rot90(GLIDER3.cell))
GLIDER3_180 = Cell('glider3_180', np.rot90(GLIDER3.cell, 2))
GLIDER3_270 = Cell('glider3_270', np.rot90(GLIDER3.cell, 3))

GLIDER4 = Cell('glider4', np.array([ [0, 0, 0, 0, 0],
                                    [0, 255, 0, 0, 0],
                                    [0, 0, 255, 255, 0],
                                    [0, 255, 255, 0, 0],
                                    [0, 0, 0, 0, 0] ]))
GLIDER4_90 = Cell('glider4_90', np.rot90(GLIDER4.cell))
GLIDER4_180 = Cell('glider4_180', np.rot90(GLIDER4.cell, 2))
GLIDER4_270 = Cell('glider4_270', np.rot90(GLIDER4.cell, 3))

# Blinkers
BLINKER1 = Cell('blinker1', np.array([   [0, 0, 0],
                                        [0, 255, 0], 
                                        [0, 255, 0], 
                                        [0, 255, 0],
                                        [0, 0, 0] ]))

BLINKER2 = Cell('blinker2', np.array([   [0, 0, 0, 0, 0],
                                        [0, 255, 255, 255, 0],
                                        [0, 0, 0, 0, 0] ]))

# Toad
TOAD1 = Cell('toad1', np.array([ [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 255, 0, 0],
                                [0, 255, 0, 0, 255, 0],
                                [0, 255, 0, 0, 255, 0],
                                [0, 0, 255, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0] ]))
TOAD1_90 = Cell('toad1_90', np.rot90(TOAD1.cell))

TOAD2 = Cell('toad2', np.array([ [0, 0, 0, 0, 0, 0],
                                [0, 0, 255, 255, 255, 0],
                                [0, 255, 255, 255, 0, 0],
                                [0, 0, 0, 0, 0, 0] ]))
TOAD2_90 = Cell('toad2_90', np.rot90(TOAD2.cell))

# Beacon
BEACON1 = Cell('beacon1', np.array([ [0, 0, 0, 0, 0, 0],
                                    [0, 255, 255, 0, 0, 0],
                                    [0, 255, 255, 0, 0, 0],
                                    [0, 0, 0, 255, 255, 0],
                                    [0, 0, 0, 255, 255, 0],
                                    [0, 0, 0, 0, 0, 0] ]))
BEACON1_90 = Cell('beacon1_90', np.rot90(BEACON1.cell))

BEACON2 = Cell('beacon2', np.array([ [0, 0, 0, 0, 0, 0],
                                    [0, 255, 255, 0, 0, 0],
                                    [0, 255, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 255, 0],
                                    [0, 0, 0, 255, 255, 0],
                                    [0, 0, 0, 0, 0, 0] ]))
BEACON2_90 = Cell('beacon2_90', np.rot90(BEACON2.cell))

# Still
BLOCK = Cell('block1', np.array([[0, 0, 0, 0],
                                [0, 255, 255, 0], 
                                [0, 255, 255, 0],
                                [0, 0, 0, 0] ]))

BEEHIVE = Cell('beehive1', np.array([[0, 0, 0, 0, 0, 0],
                                    [0, 0, 255, 255, 0, 0],
                                    [0, 255, 0, 0, 255, 0],
                                    [0, 0, 255, 255, 0, 0],
                                    [0, 0, 0, 0, 0, 0] ]))
BEEHIVE_90 = Cell('beehive1_90', np.rot90(BEEHIVE.cell))

LOAF = Cell('loaf1', np.array([  [0, 0, 0, 0, 0, 0],
                                [0, 0, 255, 255, 0, 0],
                                [0, 255, 0, 0, 255, 0],
                                [0, 0, 255, 0, 255, 0],
                                [0, 0, 0, 255, 0, 0],
                                [0, 0, 0, 0, 0, 0] ]))
LOAF_90 = Cell('loaf1_90', np.rot90(LOAF.cell))
LOAF_180 = Cell('loaf1_180', np.rot90(LOAF.cell, 2))
LOAF_270 = Cell('loaf1_270', np.rot90(LOAF.cell, 3))

BOAT = Cell('boat1', np.array([  [0, 0, 0, 0, 0],
                                [0, 255, 255, 0, 0],
                                [0, 255, 0, 255, 0],
                                [0, 0, 255, 0, 0] ]))
BOAT_90 = Cell('boat1_90', np.rot90(BOAT.cell))
BOAT_180 = Cell('boat1_180', np.rot90(BOAT.cell, 2))
BOAT_270 = Cell('boat1_270', np.rot90(BOAT.cell, 3))

TUB = Cell('tub1', np.array([[0, 0, 0, 0, 0],
                            [0, 0, 255, 0, 0],
                            [0, 255, 0, 255, 0],
                            [0, 0, 255, 0, 0],
                            [0, 0, 0, 0, 0] ]))

all_cells = [   SPACESHIP1, SPACESHIP1_90, SPACESHIP1_180, SPACESHIP1_270, 
                SPACESHIP2, SPACESHIP2_90, SPACESHIP2_180, SPACESHIP2_270,
                SPACESHIP3, SPACESHIP3_90, SPACESHIP3_180, SPACESHIP3_270,
                SPACESHIP4, SPACESHIP4_90, SPACESHIP4_180, SPACESHIP4_270,
                GLIDER1, GLIDER1_90, GLIDER1_180, GLIDER1_270,
                GLIDER2, GLIDER2_90, GLIDER2_180, GLIDER2_270,
                GLIDER3, GLIDER3_90, GLIDER3_180, GLIDER3_270,
                GLIDER4, GLIDER4_90, GLIDER4_180, GLIDER4_270,
                BLINKER1,
                BLINKER2,
                TOAD1, TOAD1_90,
                TOAD2, TOAD2_90,
                BEACON1, BEACON1_90,
                BEACON2, BEACON2_90, 
                BLOCK,
                BEEHIVE, BEEHIVE_90,
                LOAF, LOAF_90, LOAF_180, LOAF_270,
                BOAT, BOAT_90, BOAT_180, BOAT_270,
                TUB]

def find_life_type(x, y, grid):
    cell_type = None
    for num, cell in enumerate(all_cells):
        if cell.compare(x, y, grid):
            cell_type = cell.get_cell_type()
            break
    return cell_type