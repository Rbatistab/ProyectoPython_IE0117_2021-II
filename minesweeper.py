#!/usr/bin/python3

class Box:
    '''
    This class objects contain information about a box in the minesweeper game
    '''
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.content = ''
        self.state = ''


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


class Boolean_Variables:
    '''
    This class contain boolean variables regarding the reset and closing state
    '''
    def __init__(self):
        self.close = False
        self.full_reset = False
        self.soft_reset = False


def dimensions_mines():
    # A window is presented that asks for dimensions, then, those dimensions
    # are validated. If there's an error the window asks again. The dimensions
    # n and m are saved
    n, m = dim_window()

    # A window is presented that asks for mine quantity, which is validated, if
    # there's an error this window asks again. The mine quantity is saved
    mines = mine_quantity_window()

    return n, m, mines


def initialize_game(n, m, mines):
    # A Game class object is created. The atribute game_matrix is an array
    # filled with box objects, that contain information about is its position,
    # an atribute with a mine or a number, and another atribute that indicates
    # the state: hidden, visible, flag or question mark.
    game = Game(n, m)

    # The defined quantity of mines are randomly placed on the boxes
    game.mine_placing(mines)

    # According to the mine placing, the numbers are written on the remaining
    # boxes
    game.number_writting()

    # A window with the game layout is created
    window_creation(n, m)

    # A Boolean_Variables object is created
    boolean = Boolean_Variables

    return game, boolean


def playing(game, boolean):
    # A window of the game is refreshed
    refresh_window(game)

    # On left click event the box array is refreshed
    game.refresh_boxes_left()

    # On right click event the box array is refreshed
    game.refresh_boxes_right()

    # When close button is clicked
    boolean.close = True

    # When soft reset button is clicked
    boolean.soft_reset = True

    # When full reset button is clicked
    boolean.full_reset = True


def exec():
    n, m, mines = dimensions_mines()

    while(not full_reset and not close):
        game, boolean = initialize_game()

        while(not soft_reset and not full_reset and not close):
            playing(game, boolean)

            if win:
                show_win(game)
                highscore()
            elif loose:
                show_loose(game)


def main():
    while(not close):
        exec()


if __name__ == '__main__':
    # Some global boolean variables are defined
    close = False
    full_reset = False
    soft_reset = False
    win = False
    loose = False

    main()
