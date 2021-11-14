import sys

sys.path.append('../ProyectoPython_IE0117_2021-II')

from mine_sweeper_backend.GeneralMatrix import GeneralMatrix as GeneralMatrix

# BoxClasses import BoxClass as BoxClass



def print_matrix_testing(matrix):
    for row in matrix:
      print("")
      for col in row:
          print(col, end=" ")


# Testing general matrix for int:
print("3x4 matrix of int objects")
matrix_test = GeneralMatrix(3,4,int).matrix
print_matrix_testing(matrix_test)


# Testing general matrix for object:
print("2x2 matrix of objects")
matrix_test = GeneralMatrix(2,2,object).matrix
print_matrix_testing(matrix_test)


# Testing general matrix for object:
print("9x7 matrix of 0")
general_matrix_object = GeneralMatrix(9,7,0)
matrix_test = general_matrix_object.matrix
print_matrix_testing(matrix_test)


# Testing object substitution matrix for object:
print("\n\nSubstituting 0 in (0,4) for \'x\''")
general_matrix_object.set_element_value(0,4,'x')
print_matrix_testing(matrix_test)


# Testing object substitution matrix for object:
print("\n\nTesting get_element(), expected: \'x\''")
get_elem_test = general_matrix_object.get_element(0,4)
print_matrix_testing(get_elem_test)


# Testing str():
print("\n\nTesting \'str()\' method:\n")
print(str(general_matrix_object))


# Testing get_matrix_dimensions:
print("\n\nTesting \'get_matrix_dimensions()\' method: expexted (9,7)\n")
size_of_general_matrix_object = general_matrix_object.get_matrix_dimensions()
print(size_of_general_matrix_object)


# Making a mock up matrix
def mock_up_matrix():
  mock_up_matrix_elems = [
  # [0  ,  1 ,  2 , 3,  4 , 5,  6  cols/rows
    [0  , 'a',  1 , 2, '*', 1,  0 ], # 0
    ['c', 'b', '*', 3, '*', 1,  0 ], # 1 
    [0  ,  2 , '*', 2,  1 , 1,  0 ], # 2
    [0  ,  1 ,  0 , 1,  1 , 1,  1 ], # 3
    [0  ,  0 ,  0 , 1, '*', 2, '*'], # 4
    [0  ,  0 ,  0 , 0,  0 , 0,  0 ]  # 5
  ]
  
  mock_up = GeneralMatrix(6,7)
  for row_ind, row in enumerate(mock_up_matrix_elems):
    for col_ind, elem in enumerate(row):
      mock_up.set_element_value(row_ind,col_ind, elem)
  return mock_up


print("\nPrinting a mock up matrix:\n")
mock_up = mock_up_matrix()
print(str(mock_up))


# Testing get_adjacent_elements:
print("\n\nTesting \'get_adjacent_elements(0,0)\' method: expexted ['a', 'c', 'b']\n")
mock_up_adjacent = mock_up.get_adjacent_elements(0,0)
print(mock_up_adjacent)

print("\n\nTesting \'get_adjacent_elements(4,4)\' method: expexted [1, 1, 1, 1, 2, 0, 0, 0]\n")
mock_up_adjacent = mock_up.get_adjacent_elements(4,4)
print(mock_up_adjacent)

# Testing Matrix iterator:
print("\n\nTesting \'__iter__()\' method: expexted the rows of the mock up matrix\n")
for row in mock_up:
  print(row)
print("\n\nTesting \'__iter__()\' with enumerator method: expexted the rows of the mock up matrix\n")
for ind_rw, row in enumerate(mock_up):
  print("Index: " + str(ind_rw))
  print(row)
