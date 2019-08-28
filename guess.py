#!/usr/bin/env python3

from typing import List

grid = {}

grid[1] = {3, 5, 7, 9, 11, 1,
           13, 15, 17, 19, 21, 23,
           25, 27, 29, 31, 33, 35,
           37, 39, 41, 43, 47,
           49, 51, 53, 55, 57, 59}

grid[2] = {5, 6, 7, 13, 12, 4,
           14, 15, 20, 21, 22, 23,
           28, 29, 30, 31, 36, 37,
           38, 39, 44, 45, 46, 47,
           52, 53, 54, 55, 60, 13}

grid[3] = {9, 10, 11, 12, 13, 8,
           14, 15, 24, 25, 26, 27,
           28, 29, 30, 31, 40, 41,
           42, 43, 44, 45, 46, 47,
           56, 57, 58, 59, 60, 13}

grid[4] = {3, 6, 7, 10, 11, 2,
           14, 15, 18, 19, 22, 23,
           26, 27, 30, 31, 34, 35,
           38, 39, 42, 43, 46, 47}

grid[5] = {17, 18, 19, 20, 21, 16,
           22, 23, 24, 25, 26, 27,
           28, 29, 30, 31, 48, 49,
           50, 51, 52, 53, 54, 55,
           56, 57, 58, 59, 60, 31}

grid[6] = {33, 34, 35, 36, 37, 32,
           38, 39, 40, 41, 42, 43,
           44, 45, 46, 47, 48, 49,
           50, 51, 52, 53, 54, 55,
           56, 57, 58, 59, 60, 46}


def guess_number_pointing_at_grids(board_numbers: List[int]):
    possible_numbers = grid[1]

    for grid_number in range(2, 7):
        if grid_number in board_numbers:
            possible_numbers = possible_numbers.intersection(grid[grid_number])
        else:
            for number in grid[grid_number]:
                possible_numbers.discard(number)

        if len(possible_numbers) == 1:
            break

    return possible_numbers


def find_grids_for_number(number):
    grids = []

    for grid_number in range(1, 7):
        if number in grid[grid_number]:
            grids.append(grid_number)

    return grids


result = guess_number_pointing_at_grids([1, 2, 4, 5])
print(result)

for number in range(1, 61):
    print("number:", number, "in:", find_grids_for_number(number))
