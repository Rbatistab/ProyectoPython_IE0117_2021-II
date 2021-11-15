#!/usr/bin/python3

import random
from mine_sweeper_backend.GeneralMatrix import GeneralMatrix as GeneralMatrix
# from mine_sweeper_backend.BoxClasses import BoxClass, MineBox as MineBox
from mine_sweeper_backend.BoxClasses import MineBox as MineBox
from mine_sweeper_backend.BoxClasses import NumberBox as NumberBox


def get_game_matrix(rows, cols, mines):
    '''
    Gets a nuew game matrix, given the rows, columns and number of mines
    '''
    game_matrix = get_empty_matrix(rows, cols)
    sort_mines(mines, rows, cols, game_matrix)
    add_numbers_to_matrix(game_matrix)
    return game_matrix


def get_empty_matrix(rows, columns, object_type=object):
    '''
    Creates an empty matrix
    '''
    empty_matrix = GeneralMatrix(rows, columns)
    return empty_matrix


def sort_mines(mines, rows, cols, matrix):
    '''
    Distributes the desired amount of mines in a given matrix
    '''
    mines_coordinates = get_mines_coordinates(rows, cols, mines)
    add_mines_to_matrix(mines_coordinates, matrix)


def get_mines_coordinates(rows, cols, mines):
    '''
    Gets the coordinates of the mines in the matrix
    '''
    mines_coordinates = []
    mines_already_set = 0
    while mines_already_set < mines:
        new_mine_coordinate = get_random_coordinate(rows, cols)
        if coordinate_is_valid(new_mine_coordinate, mines_coordinates):
            mines_coordinates.append(new_mine_coordinate)
            mines_already_set += 1

    return mines_coordinates


def get_random_coordinate(row_lim, col_lim):
    '''
    Generates a random coordinate bounded by row and column size
    '''
    rand_row = random.randint(0, row_lim-1)
    rand_col = random.randint(0, col_lim-1)
    return (rand_row, rand_col)


def add_mines_to_matrix(mines_coordinates, matrix):
    '''
    Puts mines on the given mines_coordinates of a matrix
    '''
    for coordinate in mines_coordinates:
        new_mine = MineBox()
        row = coordinate[0]
        col = coordinate[1]
        matrix.set_element_value(row, col, new_mine)


def coordinate_is_valid(new_coordinate, existing_coordinates):
    '''
    Validate that the coordinate is valid, for the moment just avoids
    repeated values
    '''
    if new_coordinate in existing_coordinates:
        return False
    return True


def add_numbers_to_matrix(matrix):
    '''
    Creates NumberBoxes in the matrix
    '''
    for ind_rw, row in enumerate(matrix):
        for ind_cl, element in enumerate(row):
            if not (is_mine(element)):
                current_box_number = get_box_number(ind_rw, ind_cl, matrix)
                new_box = NumberBox(current_box_number)
                matrix.set_element_value(ind_rw, ind_cl, new_box)


def get_box_number(row, col, matrix):
    '''
    Gets the number of adjacent mines for a given box coordinates
    '''
    box_number = 0
    adjacent_boxes = matrix.get_adjacent_elements(row, col)
    for box in adjacent_boxes:
        if(is_mine(box)):
            box_number += 1
    return box_number


def is_mine(element):
    '''
    Determines if an element is a mine
    '''
    return (type(element) == MineBox)


def get_perimeter(row, col, game_matrix):
    # adjacent_boxes = game_matrix.get_adjacent_coordinates_and_elements(row,col)
    # print(adjacent_boxes)
    # for neighbor in adjacent_boxes:
    #     box = neighbor[2]
    #     print(box)
    #     # if not is_mine(box):
    #     if not is_mine_dummy_test(box):
    #         rw = neighbor[0]
    #         cl = neighbor[1]
    #         coords = (rw, cl)
    #         print(coords)
    #         if not coords in perimeter:
    #             perimeter.append( coords )
    #         # if box.number == 0:
    #         if box == 0:
    #             perimeter = get_perimeter(rw, cl, game_matrix, perimeter)
    #     else:
    #         print("no cords")
    return perimeter

def is_mine_dummy_test(elem):
    return '*' == elem

    

