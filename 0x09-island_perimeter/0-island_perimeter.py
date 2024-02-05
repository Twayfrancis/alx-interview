#!/usr/bin/python3
"""
function def island_perimeter(grid): that returns
the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """returns perimeter of an island desc in grid"""
    # initialize the perimeter to 0
    perimeter = 0
    # loop through each row of the grid
    for i in range(len(grid)):
        # loop through each column of the grid
        for j in range(len(grid[i])):
            # if the cell is land (1)
            if grid[i][j] == 1:
                # add 4 to the perimeter
                perimeter += 4
                # subtract 2 for each adjacent land cell on the same row
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                # subtract 2 for each adjacent land cell on the same column
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    # return the final perimeter
    return perimeter
