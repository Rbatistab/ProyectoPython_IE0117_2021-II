class mine_sweeper_backend:


  def dim_window():
    print("dimensioning window")
    # logica de crear una ventana en el backend

  def matrix_creation(n, m):
    matrix = []

    for _ in range(n):
        matrix.append([])

    for a in range(n):
        for _ in range(m):
            matrix[a].append([])

    return matrix


class Game:
    '''
    This class object contains information about the backend of the minesweeper
    game
    '''
    def __init__(self, n, m):
        game_matrix = matrix_creation(n, m)
        for a in range(n):
            for b in range(m):
                game_matrix[a][b] = Box(a, b)
        self.game_matrix = game_matrix


class Box:
    '''
    This class objects contain information about a box in the minesweeper game
    '''
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.content = ''
        self.state = ''