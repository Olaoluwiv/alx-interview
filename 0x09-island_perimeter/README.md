#!/usr/bin/python3

'''0x09.Island Perimeter'''


def island_perimeter(grid):
       lst_max = len(grid[0]) - 1  # index of the last square in list

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # left and right
                if land_idx == 0:
                    # left side
                    counter += 1

                    # right side
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # right side
                    counter += 1
                else:
                    # left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # right side
                    if lst[land_idx + 1] == 0:
                        counter += 1

                # top and down
                if lst_idx == 0:
                    # top side
                    counter += 1

                    # bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    counter += 1
                else:
                    # top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return countermeter'''


def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    counter = 0
    grid_max = len(grid) - 1  # index of the last list in the grid
    lst_max = len(grid[0]) - 1  # index of the last square in list

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # left and right
                if land_idx == 0:
                    # left side
                    counter += 1

                    # right side
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # right side
                    counter += 1
                else:
                    # left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # right side
                    if lst[land_idx + 1] == 0:
                        counter += 1

                # top and down
                if lst_idx == 0:
                    # top side
                    counter += 1

                    # bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    counter += 1
                else:
                    # top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return counternd Perimeter

Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

- grid is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
