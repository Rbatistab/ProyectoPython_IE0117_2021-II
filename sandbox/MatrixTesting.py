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
