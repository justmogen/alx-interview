#!/usr/bin/python3

def island_perimeter(grid):
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                # Each land cell contributes 4 units to perimeter

                # check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
