#!/usr/bin/python3

# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from mine_sweeper_UI.Ui_Dimensions import Ui_Dimensions
from mine_sweeper_UI.Ui_Mines import Ui_Mines
from mine_sweeper_UI.Ui_Game import Ui_Game
from mine_sweeper_UI.Ui_Game import Ui_Show_Highscores
from mine_sweeper_UI.Ui_Game import Ui_Add_Highscores
# from mine_sweeper_backend.mine_sweeper_backend import matrix_creation
import sys


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


def game_window(n, m):
    '''
    Raises the main game window with the mine sweeper
    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Game()
    ui.setupUi(MainWindow, n, m)
    MainWindow.show()
    app.exec_()


def show_highscores_window():
    '''
    Raises a window showing the highscore's table
    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Show_Highscores()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()


def add_highscores_window(new_highscore):
    '''
    Raises the main game window with the mine sweeper
    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_Highscores()
    ui.setupUi(MainWindow, new_highscore)
    MainWindow.show()
    app.exec_()

# ----------------------- Mock ups to delete-----------------------------------
def dimensions_mines():
    # A window is presented that asks for dimensions, then, those dimensions
    # are validated. If there's an error the window asks again. The dimensions
    # n and m are saved
    n, m = dim_window()

    max_mines = n*m
    # A window is presented that asks for mine quantity, which is validated, if
    # there's an error this window asks again. The mine quantity is saved
    mines = mine_window(max_mines)
    print(mines)

    return n, m, mines


# ----------------------- Mock ups to delete-----------------------------------
def mine_quantity_window():
    # Linea real, descomentar cuando este lista:
    # return n, m
    # Linea de mockup, borrar
    return 4


class Board:  # Will we need this class?
    def create_board():
        print("board")


class PlayGame:  # Do we need this logic as a class?
    def playing(game, boolean):
        # A window of the game is refreshed
        refresh_window(game)

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

# Mock up

# Matriz 3 x 3:

# * 1 0
# 1 2 *
# 0 0 *
