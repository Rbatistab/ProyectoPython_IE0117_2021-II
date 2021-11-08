#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dimensions(object):
    def setupUi(self, MainWindow):
        self.n = 1
        self.m = 1
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 233)
        sizePolicy = QtWidgets.QSizePolicy(
                                           QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred
                                           )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                                    MainWindow.sizePolicy().hasHeightForWidth()
                                    )
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Cantidad_de_columnas_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.Cantidad_de_columnas_spin.setMinimum(1)
        self.Cantidad_de_columnas_spin.setObjectName(
                                                    "Cantidad_de_columnas_spin"
                                                    )
        self.gridLayout.addWidget(self.Cantidad_de_columnas_spin, 1, 1, 1, 1)
        self.Cantidad_de_filas_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.Cantidad_de_filas_spin.setMinimum(1)
        self.Cantidad_de_filas_spin.setObjectName("Cantidad_de_filas_spin")
        self.gridLayout.addWidget(self.Cantidad_de_filas_spin, 1, 0, 1, 1)
        self.Cantidad_Filas_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Cantidad_Filas_label.setFont(font)
        self.Cantidad_Filas_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Cantidad_Filas_label.setObjectName("Cantidad_Filas_label")
        self.gridLayout.addWidget(self.Cantidad_Filas_label, 0, 0, 1, 1)
        self.Cantidad_columnas_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Cantidad_columnas_label.setFont(font)
        self.Cantidad_columnas_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Cantidad_columnas_label.setObjectName("Cantidad_columnas_label")
        self.gridLayout.addWidget(self.Cantidad_columnas_label, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(
                                           20,
                                           40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding
                                           )
        self.verticalLayout_2.addItem(spacerItem)
        self.OK_Button = QtWidgets.QPushButton(self.centralwidget)
        self.OK_Button.setObjectName("OK_Button")
        self.OK_Button.clicked.connect(lambda: self.ok_clicked(MainWindow))
        self.verticalLayout_2.addWidget(self.OK_Button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
                                            "MainWindow",
                                            "Dimensiones"
                                            )
                                  )
        self.Cantidad_Filas_label.setText(_translate(
                                                    "MainWindow",
                                                    "Cantidad de filas"
                                                    )
                                          )
        self.Cantidad_columnas_label.setText(_translate(
                                                        "MainWindow",
                                                        "Cantidad de columnas"
                                                        )
                                             )
        self.OK_Button.setText(_translate("MainWindow", "OK"))

    def ok_clicked(self, MainWindow):
        self.n = self.Cantidad_de_filas_spin.value()
        self.m = self.Cantidad_de_columnas_spin.value()
        MainWindow.close()


def dim_window():
    app = QtWidgets.QApplication(sys.argv)
    Main_Dimensions_Window = QtWidgets.QMainWindow()
    Dimensions_Window = Ui_Dimensions()
    Dimensions_Window.setupUi(Main_Dimensions_Window)
    Main_Dimensions_Window.show()
    app.exec_()
    n = Dimensions_Window.n
    m = Dimensions_Window.m

    return n, m


class Ui_Mines(object):
    def setupUi(self, MainWindow, max_mines):
        self.mines = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 233)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Cantidad_Minas_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Cantidad_Minas_label.setFont(font)
        self.Cantidad_Minas_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Cantidad_Minas_label.setObjectName("Cantidad_Minas_label")
        self.verticalLayout.addWidget(self.Cantidad_Minas_label)
        self.Cantidad_de_minas_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.Cantidad_de_minas_spin.setMinimum(1)
        self.Cantidad_de_minas_spin.setMaximum(max_mines - 1)
        self.Cantidad_de_minas_spin.setObjectName("Cantidad_de_minas_spin")
        self.verticalLayout.addWidget(self.Cantidad_de_minas_spin)
        spacerItem = QtWidgets.QSpacerItem(
                                           20,
                                           40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding
                                           )
        self.verticalLayout.addItem(spacerItem)
        self.OK_Button = QtWidgets.QPushButton(self.centralwidget)
        self.OK_Button.setObjectName("OK_Button")
        self.verticalLayout.addWidget(self.OK_Button)
        self.OK_Button.clicked.connect(lambda: self.ok_clicked(MainWindow))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minas"))
        self.Cantidad_Minas_label.setText(_translate(
                                                    "MainWindow",
                                                    "Cantidad de minas"
                                                    )
                                          )
        self.OK_Button.setText(_translate("MainWindow", "OK"))

    def ok_clicked(self, MainWindow):
        self.mines = self.Cantidad_de_minas_spin.value()
        MainWindow.close()


def mine_window(max_mines):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Mines()
    ui.setupUi(MainWindow, max_mines)
    MainWindow.show()
    app.exec_()
    mines = ui.mines

    return mines


class Menus():  # estos metodos deberian estar en una clase?

    def dim_window():
        # Linea real, descomentar cuando este lista:
        # return n, m
        # Linea de mockup, borrar
        return 9, 9

    def mine_quantity_window(self):
        # Linea real, descomentar cuando este lista:
        # return n, m
        # Linea de mockup, borrar
        return 4

    def dimensions_mines_mockup():
        # Mock up para probar controller
        return 3, 3, 4

    def dimensions_mines():
        # A window is presented that asks for dimensions, then, those dimensions
        # are validated. If there's an error the window asks again. The dimensions
        # n and m are saved
        n, m = dim_window()
        print(n)
        print(m)

        # A window is presented that asks for mine quantity, which is validated, if
        # there's an error this window asks again. The mine quantity is saved
        mines = self.mine_quantity_window(self)
        print(mines)

        return n, m, mines



class Board:
  def create_board():
    print("board")


class PlayGame:
    def playing(game, boolean):
        # A window of the game is refreshed
        refresh_window(game)

        # On left click event the box array is refreshed
        game.refresh_boxes_left()

        # On right click event the box array is refreshed
        game.refresh_boxes_right()

        # When close button is clicked
        boolean.close = True # aqui va el terminate exception

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
