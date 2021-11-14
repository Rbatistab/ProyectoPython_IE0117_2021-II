#!/usr/bin/python3

import random
from mine_sweeper_backend.GeneralMatrix import GeneralMatrix as GeneralMatrix
from mine_sweeper_backend.BoxClasses import MineBox as MineBox
from mine_sweeper_backend.BoxClasses import NumberBox as NumberBox


def get_game_matrix(rows, cols, mines):
    game_matrix = get_empty_matrix(rows, cols)
    sort_mines(mines, rows, cols, game_matrix)
    # add_numbers_to_matrix(game_matrix)
    return game_matrix
    

def get_empty_matrix(rows, columns, object_type = object):
    empty_matrix = GeneralMatrix(rows, columns)
    return empty_matrix


def sort_mines(mines, rows, cols, matrix):
    mines_coordinates = get_mines_coordinates(rows, cols, mines)
    add_mines_to_matrix(mines_coordinates, matrix)


def get_mines_coordinates(rows, cols, mines):
    mines_coordinates = []
    mines_already_set = 0
    while mines_already_set < mines:
        new_mine_coordinate = get_random_coordinate(rows, cols)
        if coordinate_is_valid(new_mine_coordinate, mines_coordinates):
            mines_coordinates.append(new_mine_coordinate)
            mines_already_set += 1

    return mines_coordinates

def get_random_coordinate(row_lim, col_lim):
    rand_row = random.randint(0, row_lim-1)
    rand_col = random.randint(0, col_lim-1)
    return (rand_row, rand_col)


def add_mines_to_matrix(mines_coordinates, matrix):
    for coordinate in mines_coordinates:
        new_mine = MineBox()
        row = coordinate[0]
        col = coordinate[1]
        matrix.set_element_value(row, col, new_mine)


def coordinate_is_valid(new_coordinate, existing_coordinates):
    if new_coordinate in existing_coordinates:
        return False
    return True


# def add_numbers_to_matrix(matrix):
    
        