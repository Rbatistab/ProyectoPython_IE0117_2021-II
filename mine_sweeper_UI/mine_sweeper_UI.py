import sys
from mine_sweeper_backend.mine_sweeper_backend import get_game_matrix

from PyQt5 import QtWidgets
from mine_sweeper_UI.Ui_Dimensions import Ui_Dimensions
from mine_sweeper_UI.Ui_Mines import Ui_Mines
from mine_sweeper_UI.Ui_Game import Ui_Game


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
    mines_and_numbers_matrix = get_game_matrix(n, m, mines)
    ui = Ui_Game(mines_and_numbers_matrix)
    ui.setupUi(MainWindow, n, m, mines, bool)
    MainWindow.show()
    app.exec_()

    return


def dimensions_mines():
    '''
    A window is presented that asks for dimensions, then, those dimen-
    sions are validated. If there's an error the window asks again. The 
    dimensions n and m are saved
    '''
    n, m = dim_window()
    max_mines = n * m
    # A window is presented that asks for mine quantity, which is validated, if
    # there's an error this window asks again. The mine quantity is saved
    mines = mine_window(max_mines)

    return n, m, mines
