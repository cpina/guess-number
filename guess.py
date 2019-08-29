#!/usr/bin/env python3

from typing import List

GRIDS = {}

# Uses Mimi's GRID
GRIDS[1] = {7, 11, 8,
            6, 2, 10}

GRIDS[2] = {10, 4, 6,
            9, 3, 11}

GRIDS[3] = {8, 9, 11,
            7, 5, 10}

GRIDS[4] = {4, 6, 9,
            11, 1, 8}

# GRIDS[1] = {3, 5, 7, 9, 11, 1,
#             13, 15, 17, 19, 21, 23,
#             25, 27, 29, 31, 33, 35,
#             37, 39, 41, 43, 47,
#             49, 51, 53, 55, 57, 59}
#
# GRIDS[2] = {5, 6, 7, 13, 12, 4,
#             14, 15, 20, 21, 22, 23,
#             28, 29, 30, 31, 36, 37,
#             38, 39, 44, 45, 46, 47,
#             52, 53, 54, 55, 60, 13}
#
# GRIDS[3] = {9, 10, 11, 12, 13, 8,
#             14, 15, 24, 25, 26, 27,
#             28, 29, 30, 31, 40, 41,
#             42, 43, 44, 45, 46, 47,
#             56, 57, 58, 59, 60, 13}
#
# GRIDS[4] = {3, 6, 7, 10, 11, 2,
#             14, 15, 18, 19, 22, 23,
#             26, 27, 30, 31, 34, 35,
#             38, 39, 42, 43, 46, 47,
#             50, 51, 54, 55, 58, 59}
#
# GRIDS[5] = {17, 18, 19, 20, 21, 16,
#             22, 23, 24, 25, 26, 27,
#             28, 29, 30, 31, 48, 49,
#             50, 51, 52, 53, 54, 55,
#             56, 57, 58, 59, 60, 31}
#
# GRIDS[6] = {33, 34, 35, 36, 37, 32,
#             38, 39, 40, 41, 42, 43,
#             44, 45, 46, 47, 48, 49,
#             50, 51, 52, 53, 54, 55,
#             56, 57, 58, 59, 60, 46}

def find_maximum_number():
    maximum = float('-inf')

    for grid_number, grid in GRIDS.items():
        for number in grid:
            if maximum < number:
                maximum = number

    return maximum

def guess_number_pointing_at_grids(grid_numbers: List[int]) -> List[int]:
    """Mind reading - based on the numbers in the grids, not the fancy
    logic that a human would use (if the trick is known)
    
    :param grid_numbers: where the user said that the number is 
    :return: the number!
    """
    possible_numbers = None

    for grid_number, grid in GRIDS.items():
        if possible_numbers is None:
            possible_numbers = set(grid)
            continue

        if grid_number in grid_numbers:
            possible_numbers = possible_numbers.intersection(grid)
        else:
            for number in grid:
                possible_numbers.discard(number)

        if len(possible_numbers) == 1:
            break

    assert len(possible_numbers) == 1
    return possible_numbers.pop()


def find_grids_with_number(number: int) -> List[int]:
    """
    :param number: which number needs to be found in the grids
    :return: list of grids with the number in
    """
    grids_with_number = []

    for grid_number, grid in GRIDS.items():
        if number in grid:
            grids_with_number.append(grid_number)

    return grids_with_number


def main():
    # Part 1 Demo
    number_to_find = 1
    grids_with_number = find_grids_with_number(number_to_find)
    print('List of grids with the number', number_to_find)
    print(grids_with_number)

    # Part 2 Demo
    grids_to_find_number = [1,4]
    print('Which number if the user pointed at:', grids_with_number)
    number = guess_number_pointing_at_grids(grids_with_number)
    print(number)

    # Part 3 to help to find the pattern
    maximum_number = find_maximum_number()
    for number in range(1, maximum_number):
        print('Number:', number, 'in grids:', find_grids_with_number(number))


if __name__ == '__main__':
    main()
