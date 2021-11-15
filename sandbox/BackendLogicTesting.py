#!/usr/bin/python3

import sys

sys.path.append('../ProyectoPython_IE0117_2021-II')

from mine_sweeper_backend.mine_sweeper_backend import *

# Testing for a 6 x 4 matrix with 7 mines

print("\nTesting for a 6 x 4 matrix with 7 mines")

# get_empty_matrix()
empty_matrix = get_empty_matrix(6, 4)
print("\nTesting \'get_empty_matrix(6,4) method:\'")
print( str(empty_matrix) )

# get_random_coordinate()
print("\nTesting \'get_random_coordinate(6,4):\'")
random_coord = get_random_coordinate(6,4)
print(random_coord)

# coordinate_is_valid()
print("\nTesting \'coordinate_is_valid( (6,4), [(6,4)])\': expected False")
invalid_coord = coordinate_is_valid( (6,4), [(6,4)])
print(invalid_coord)
print("\nTesting \'coordinate_is_valid( (6,4), [(6,4)])\': expected True")
valid_coord = coordinate_is_valid( (6,4), [(0,0)])
print(valid_coord)

# get_random_coordinate()
print("\nTesting \'get_mines_coordinates(6,4,7): expected 7 mines\'")
random_coord_list = get_mines_coordinates(6,4,7)
print(random_coord_list)

# add_mines_to_matrix()
print("\nTesting \'add_mines_to_matrix(): expected 7 mines\'")
add_mines_to_matrix(random_coord_list, empty_matrix)
print( str(empty_matrix) )

# add_numbers_to_matrix()
print("\nTesting \'add_numbers_to_matrix():\'")
add_numbers_to_matrix(empty_matrix)
print( str(empty_matrix) )



print("\nTesting \'get_game_matrix(6, 4, 7):\'")
game_matrix = get_game_matrix(6, 4, 7)
print(str(game_matrix))



print("\nTesting \'get_game_matrix(9, 9, 60):\'")
game_matrix = get_game_matrix(9, 9, 60)
print(str(game_matrix))


def mock_up_matrix():
  mock_up_matrix_elems = [
  # [0  ,  1 ,  2 , 3,  4 , 5,  6  cols/rows
    [0  ,  1 ,  1 , 3, '*', 1,  0 ], # 0
    [0  ,  2 , '*', 4, '*', 1,  0 ], # 1 
    [0  ,  2 , '*', 3,  1 , 1,  0 ], # 2
    [0  ,  1 ,  0 , 1,  1 , 1,  1 ], # 3
    [0  ,  0 ,  0 , 1, '*', 2, '*'], # 4
    [0  ,  0 ,  0 , 0,  0 , 0,  0 ]  # 5
  ]
  
  mock_up = GeneralMatrix(6,7)
  for row_ind, row in enumerate(mock_up_matrix_elems):
    for col_ind, elem in enumerate(row):
      mock_up.set_element_value(row_ind,col_ind, elem)
  return mock_up

print("\nMock up Matrix:")
mock_up_mtrx = mock_up_matrix()
print(str(mock_up_mtrx))

# Testing 
print("\nTesting \'get_perimeter(0,0,mock_up_mtrx):\'")
perimeter1 = get_perimeter(0,0,mock_up_mtrx)
print(perimeter1)

# Testing 
print("\nTesting \'get_perimeter(0,2,mock_up_mtrx):\'")
perimeter = get_perimeter(0,2,mock_up_mtrx)
print(perimeter)


for row in game_matrix_object: # recorre filas
  for element in row: # recorre columnas de una fila
    if is_mine(element): 
      # procesa como mina
    else:
      number = element.number
      # procesa como numero