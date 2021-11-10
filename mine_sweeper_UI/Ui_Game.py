#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Game(object):
    def __init__(self):
        self.icon_blank = "mine_sweeper_UI/imgs/blank.png"

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
                       QtGui.QPixmap(self.icon_blank),
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
