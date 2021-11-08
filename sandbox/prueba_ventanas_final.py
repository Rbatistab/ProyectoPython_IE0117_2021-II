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
        self.Cantidad_de_columnas_spin.setMaximum(30)
        self.gridLayout.addWidget(self.Cantidad_de_columnas_spin, 1, 1, 1, 1)
        self.Cantidad_de_filas_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.Cantidad_de_filas_spin.setMinimum(1)
        self.Cantidad_de_filas_spin.setObjectName("Cantidad_de_filas_spin")
        self.Cantidad_de_filas_spin.setMaximum(16)
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
        MainWindow.setWindowTitle("Dimensiones")
        self.Cantidad_Filas_label.setText("Cantidad de filas")
        self.Cantidad_columnas_label.setText("Cantidad de columnas")
        self.OK_Button.setText("OK")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowTitle("Minas")
        self.Cantidad_Minas_label.setText("Cantidad de minas")
        self.OK_Button.setText("OK")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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


class Ui_Game(object):
    def setupUi(self, MainWindow, n, m):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setIconSize(QtCore.QSize(16, 16))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_grid(n, m)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuReinicio = QtWidgets.QMenu(self.menubar)
        self.menuReinicio.setObjectName("menuReinicio")
        MainWindow.setMenuBar(self.menubar)
        self.actionReinicio_suave = QtWidgets.QAction(MainWindow)
        self.actionReinicio_suave.setObjectName("actionReinicio_suave")
        self.actionReinicio_fuerte = QtWidgets.QAction(MainWindow)
        self.actionReinicio_fuerte.setObjectName("actionReinicio_fuerte")
        self.menuReinicio.addAction(self.actionReinicio_suave)
        self.menuReinicio.addAction(self.actionReinicio_fuerte)
        self.menubar.addAction(self.menuReinicio.menuAction())
        MainWindow.setWindowTitle("Buscaminas")
        self.checkBox.setText("Colocar bandera")
        self.menuReinicio.setTitle("Reinicio")
        self.actionReinicio_suave.setText("Reinicio suave")
        self.actionReinicio_fuerte.setText("Reinicio fuerte")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def button_grid(self, n, m):
        self.matrix = matrix_creation(n, m)
        icon = QtGui.QIcon()
        icon.addPixmap(
                       QtGui.QPixmap("blank.png"),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off
                       )
        font = QtGui.QFont()
        font.setPointSize(24)
        for a in range(n):
            for b in range(m):
                self.matrix[a][b] = QtWidgets.QPushButton(self.centralwidget)
                self.matrix[a][b].setFont(font)
                self.matrix[a][b].setText("")
                self.matrix[a][b].setIcon(icon)
                self.matrix[a][b].setIconSize(QtCore.QSize(38, 38))
                self.gridLayout.addWidget(self.matrix[a][b], a, b, 1, 1)


def matrix_creation(n, m):
    matrix = []

    for _ in range(n):
        matrix.append([])

    for a in range(n):
        for _ in range(m):
            matrix[a].append([])

    return matrix


def game_window(n, m):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Game()
    ui.setupUi(MainWindow, n, m)
    MainWindow.show()
    app.exec_()


if __name__ == "__main__":
    n, m = dim_window()
    print('n es {} y m es {}'.format(n, m))
    mines = mine_window(n*m)
    print('La cantidad de minas es: {}'.format(mines))
    game_window(n, m)
