class GeneralMatrix:
    def __init__(self, rows, cols, desired_object=object):
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
                matrix[a].append(desired_object)

        return matrix

    def set_element_value(self, row, col, value):
        '''
        Sets a single element in the matrix to a desired value
        '''
        self.matrix[row][col] = value

    def get_element(self, row, col):
        '''
        Gets a single element in the matrix
        '''
        return self.matrix[row][col]

    def get_matrix_dimensions(self):
        '''
        Returns size of the matrix
        '''
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        return (rows, cols)

    def get_adjacent_elements(self, row, col):
        '''
        Returns a list with the neighbor elements for an element
        in a given coordinate
        '''
        adjacent_elements = []
        for rw in range(row - 1, row + 2):
            if rw < 0:
                continue
            for cl in range(col - 1, col + 2):
                if not (cl < 0 or (cl == col and rw == row)):
                    try:
                        element = self.matrix[rw][cl]
                        adjacent_elements.append(element)
                    except IndexError:
                        pass
        return adjacent_elements

    def __str__(self):
        '''
        Returns a String representation of the matrix
        '''
        matrix_string = ""
        for rows in self.matrix:
            for element in rows:
                matrix_string += str(element) + " "

            matrix_string += "\n"
        return matrix_string

    def __iter__(self):
        '''
        Matrix iterator
        '''
        return GeneralMatrixIterator(self)


class GeneralMatrixIterator:
    '''
    Iterator class for GeneralMatrix
    '''
    def __init__(self, general_matrix):
        self._matrix = general_matrix.matrix
        self._index = 0
        self.row_size = len(self._matrix)

    def __next__(self):
        '''
        Gets next row in the matrix
        '''
        if self._index < self.row_size:
            return_row = self._matrix[self._index]
            self._index += 1
            return return_row
        raise StopIteration
