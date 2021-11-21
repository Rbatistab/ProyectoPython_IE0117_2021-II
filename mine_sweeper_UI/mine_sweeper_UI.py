import sys
# sys.path.append('../ProyectoPython_IE0117_2021-II')
from mine_sweeper_backend.mine_sweeper_backend import get_game_matrix

# from PyQt5 import QtCore, QtGui, QtWidgets
# from mine_sweeper_exceptions import mine_sweeper_exceptions as ms_exceptions
from PyQt5 import QtWidgets
from mine_sweeper_UI.Ui_Dimensions import Ui_Dimensions
from mine_sweeper_UI.Ui_Mines import Ui_Mines
from mine_sweeper_UI.Ui_Game import Ui_Game
# from mine_sweeper_UI.Ui_Show_Highscores import Ui_Show_Highscores
# from mine_sweeper_UI.Ui_Add_Highscores import Ui_Add_Highscores
# from mine_sweeper_backend.mine_sweeper_backend import matrix_creation


class GameMainWindow(QtWidgets.QMainWindow):
    def __init__(self, bool):
        super(GameMainWindow, self).__init__()
        self.bool = bool

    def closeEvent(self, event):
        if(not self.bool.soft_reset and not self.bool.full_reset):
            self.bool.close = True
            # raise ms_exceptions.TerminateMineSweeper


# ------------------------- Windows ------------------------------------------
def dim_window():
    '''
    This raises a window menu to get the desired dimensions of the matrix from
    the user, returns "n" rows and "m" columns
    '''
    app = QtWidgets.QApplication(sys.argv)
    Main_Dimensions_Window = QtWidgets.QMainWindow()
    Dimensions_Window = Ui_Dimensions()
    Dimensions_Window.setupUi(Main_Dimensions_Window)
    Main_Dimensions_Window.show()
    app.exec_()
    n = Dimensions_Window.n
    m = Dimensions_Window.m

    return n, m


def mine_window(max_mines):
    '''
    This raises a window menu to get the desired dimensions amount of mines
    from the user
    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Mines()
    ui.setupUi(MainWindow, max_mines)
    MainWindow.show()
    app.exec_()
    mines = ui.mines

    return mines


def game_window(n, m, mines, bool):
    '''
    Raises the main game window with the mine sweeper
    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = GameMainWindow(bool)
    # create and send BE matrix
    mines_and_numbers_matrix = get_game_matrix(n, m, mines)

    # -----------------------------------------
    # Testing unicamente, borramos este bloque:
    print("La matriz del juego es:")
    print(str(mines_and_numbers_matrix))
    # -----------------------------------------

    ui = Ui_Game(mines_and_numbers_matrix)
    ui.setupUi(MainWindow, n, m, mines, bool)
    MainWindow.show()
    app.exec_()

    return


def dimensions_mines():
    # A window is presented that asks for dimensions, then, those dimensions
    # are validated. If there's an error the window asks again. The dimensions
    # n and m are saved
    n, m = dim_window()

    max_mines = n * m
    # A window is presented that asks for mine quantity, which is validated, if
    # there's an error this window asks again. The mine quantity is saved
    mines = mine_window(max_mines)
    print(mines)

    return n, m, mines


# ----------------------- Mock ups to delete-----------------------------------
def show_highscores_window():
    '''
    Raises a window showing the highscore's table
    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Show_Highscores()  # noqa
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()


def add_highscores_window():
    '''
    Raises the main game window with the mine sweeper
    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_Highscores()  # noqa
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    name = ui.name

    return name


class Board:  # Will we need this class?
    def create_board():
        print("board")


class PlayGame:  # Do we need this logic as a class?
    def playing(game, boolean):
        # A window of the game is refreshed
        refresh_window(game)  # noqa

        # On left click event the box array is refreshed
        game.refresh_boxes_left()

        # On right click event the box array is refreshed
        game.refresh_boxes_right()

        # When close button is clicked
        boolean.close = True  # aqui va el terminate exception

        # When soft reset button is clicked
        boolean.soft_reset = True

        # When full reset button is clicked
        boolean.full_reset = True

    def initialize_game(n, m, mines):
        # A Game class object is created. The atribute game_matrix is an array
        # filled with box objects, that contain information about is its position, # noqa
        # an atribute with a mine or a number, and another atribute that indicates # noqa
        # the state: hidden, visible, flag or question mark.
        game = Game(n, m)  # noqa

        # The defined quantity of mines are randomly placed on the boxes
        game.mine_placing(mines)

        # According to the mine placing, the numbers are written on the remaining # noqa
        # boxes
        game.number_writting()

        # A window with the game layout is created
        window_creation(n, m)  # noqa

        # A Boolean_Variables object is created
        boolean = Boolean_Variables  # noqa

        return game, boolean

# Mock up

# Matriz 3 x 3:

# * 1 0
# 1 2 *
# 0 0 *
