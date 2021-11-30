#!/usr/bin/python3

import sys

# sys.path.append('../ProyectoPython_IE0117_2021-II')
#
from mine_sweeper_backend.mine_sweeper_backend import *
#
# # Testing for a 6 x 4 matrix with 7 mines
#
# print("\nTesting for a 6 x 4 matrix with 7 mines")
#
# # get_empty_matrix()
# empty_matrix = get_empty_matrix(6, 4)
# print("\nTesting \'get_empty_matrix(6,4) method:\'")
# print( str(empty_matrix) )
#
# # get_random_coordinate()
# print("\nTesting \'get_random_coordinate(6,4):\'")
# random_coord = get_random_coordinate(6,4)
# print(random_coord)
#
# # coordinate_is_valid()
# print("\nTesting \'coordinate_is_valid( (6,4), [(6,4)])\': expected False")
# invalid_coord = coordinate_is_valid( (6,4), [(6,4)])
# print(invalid_coord)
# print("\nTesting \'coordinate_is_valid( (6,4), [(6,4)])\': expected True")
# valid_coord = coordinate_is_valid( (6,4), [(0,0)])
# print(valid_coord)
#
# # get_random_coordinate()
# print("\nTesting \'get_mines_coordinates(6,4,7): expected 7 mines\'")
# random_coord_list = get_mines_coordinates(6,4,7)
# print(random_coord_list)
#
# # add_mines_to_matrix()
# print("\nTesting \'add_mines_to_matrix(): expected 7 mines\'")
# add_mines_to_matrix(random_coord_list, empty_matrix)
# print( str(empty_matrix) )
#
# # add_numbers_to_matrix()
# print("\nTesting \'add_numbers_to_matrix():\'")
# add_numbers_to_matrix(empty_matrix)
# print( str(empty_matrix) )
#
#
#
# print("\nTesting \'get_game_matrix(6, 4, 7):\'")
# game_matrix = get_game_matrix(6, 4, 7)
# print(str(game_matrix))
#
#
#
# print("\nTesting \'get_game_matrix(9, 9, 60):\'")
# game_matrix = get_game_matrix(9, 9, 60)
# print(str(game_matrix))


def mock_up_matrix():
  mock_up_matrix_elems = [
  # [0  ,  1 ,  2 , 3,  4 , 5,  6  cols/rows
    [0, 0, 0, 0, 0, 0, 0, 0, 0],      # 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0],      # 1
    [1, 1, 0, 0, 0, 0, 0, 0, 0],      # 2
    ['*', 1, 0, 0, 0, 0, 0, 0, 0],    # 3
    ['*', 1, 0, 0, 0, 0, 0, 0, 0],    # 4
    [0, 1, '*', 2, 1, 0, 1, 1, 1],    # 5
    [0, 1, 2, '*', 1, 0, 1, '*', 1],  # 6
    [0, 0, 1, 1, 1, 0, 1, 2, 2],      # 7
    [0, 0, 0, 0, 0, 0, 0, 1, '*']     # 8
  ]

  mock_up = GeneralMatrix(9,9)
  for row_ind, row in enumerate(mock_up_matrix_elems):
    for col_ind, elem in enumerate(row):
      if elem == '*':
        curr_elem = MineBox()
      else:
        curr_elem = NumberBox(elem)
      mock_up.set_element_value(row_ind, col_ind, curr_elem)
  return mock_up

print("\nMock up Matrix:")
mock_up_mtrx = mock_up_matrix()
print(str(mock_up_mtrx))

# Testing

# pending_review = []
# perimeter = []
#
# print("neigbors (2, 2)")
# add_valid_neigbors(mock_up_mtrx, (2, 2), pending_review, perimeter)
# print(pending_review)

print("\nTesting \'get_perimeter(0,0,mock_up_mtrx):\'")

# for a in range(8):
#     for b in range(8):
#         print(mock_up_mtrx[a][b].number)

perimeter = get_perimeter(0,0,mock_up_mtrx)
print(perimeter)
print("")




# def matix_checking(matrix, perimeter):
#     for coord in perimeter:
#         rw = coord[0]
#         cl = coord[1]
#         matrix.get_element(rw,cl).number = 9
#
# print(mock_up_mtrx)
# matix_checking(mock_up_mtrx, perimeter)
# print(mock_up_mtrx)
