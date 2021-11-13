class GeneralMatrix:
    def __init__(self, rows, cols, desired_object):
        '''
        This class returns a matrix with dimentions rows x cols filled
        with the desired object
        '''
        self.matrix = self.matrix_creation(rows, cols, desired_object)


    def matrix_creation(self, n, m, desired_object):
        '''
        Creates the matrix
        '''
        matrix = []
        for _ in range(n):
            matrix.append([])

        for a in range(n):
            for _ in range(m):
                matrix[a].append( desired_object )

        return matrix


    def set_element_value(self, row, col, value):
        '''
        Sets a single element in the matrix to a desired value
        '''
        self.matrix[row][col] = value