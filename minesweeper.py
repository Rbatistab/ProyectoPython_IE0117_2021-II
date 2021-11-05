#!/usr/bin/python3

class Box:
    '''
    This class contains information about a box in the minesweeper game
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


def initialization():
    # A window is presented that asks for dimensions, then, those dimensions
    # are validated. If there's an error the window asks again. The dimensions
    # n and m are saved
    n, m = dim_window()

    # A window is presented that asks for mine quantity, which is validated, if
    # there's an error this window asks again. The mine quantity is saved
    mines = mine_quantity_window()

    # An empty array with dimensions (n,m) is created
    box_array = matrix_creation(n, m)

    # This array is filled with box objects, that contain information about is
    # its position, an atribute with a mine of a number, and another atribute
    # that indicates the state: hidden, visible, flag or question mark.
    for a in range(n):
        for b in range(m):
            box_array[a][b] = Box(n, m)

    # The defined quantity of mines are randomly placed on the boxes
    box_array = mine_placing(box_array, mines)

    # According to the mine placing, the numbers are written on the remaining
    # boxes
    box_array = number_writting(box_array)

    # A window with the game layout is created
    window_creation(n, m)


def game():
    # A window of the game is refreshed
    refresh_window(box_array)

    # On left click event the box array is refreshed
    box_array = refresh_boxes_left(box_array)

    # On right click event the box array is refreshed
    box_array = refresh_boxes_right(box_array)


def exec():

    initialization()

    while(True):
        game()
        if reset:
            break
        elif win:
            show_win(box_array)
            highscore()
            break
        elif loose:
            show_loose(box_array)
            break


def main():
    while(True):
        exec()


if __name__ == '__main__':
    # Some global boolean variables are defined
    reset = False
    win = False
    loose = False

    main()
