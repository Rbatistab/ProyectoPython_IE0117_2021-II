#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Game(object):
    def __init__(self):
        self.icon_blank = "mine_sweeper_UI/imgs/blank.png"

    def setupUi(self, MainWindow, n, m):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Bandera_signo_pregunta = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Bandera_signo_pregunta.setFont(font)
        self.Bandera_signo_pregunta.setIconSize(QtCore.QSize(16, 16))
        self.Bandera_signo_pregunta.setObjectName("Bandera_signo_pregunta")
        self.horizontalLayout.addWidget(self.Bandera_signo_pregunta)
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.Label_Minas = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Label_Minas.setFont(font)
        self.Label_Minas.setObjectName("Label_Minas")
        self.verticalLayout_1.addWidget(self.Label_Minas)
        self.lcd_minas = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_minas.setObjectName("lcd_minas")
        self.verticalLayout_1.addWidget(self.lcd_minas)
        self.horizontalLayout.addLayout(self.verticalLayout_1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_2")
        self.Label_Tiempo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Label_Tiempo.setFont(font)
        self.Label_Tiempo.setObjectName("Label_Tiempo")
        self.verticalLayout_2.addWidget(self.Label_Tiempo)
        self.lcd_tiempo = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_tiempo.setObjectName("lcd_tiempo")
        self.verticalLayout_2.addWidget(self.lcd_tiempo)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_grid(n, m)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuReinicio = QtWidgets.QMenu(self.menubar)
        self.menuReinicio.setObjectName("menuReinicio")
        self.menuPuntajes = QtWidgets.QMenu(self.menubar)
        self.menuPuntajes.setObjectName("menuPuntajes")
        MainWindow.setMenuBar(self.menubar)
        self.actionReinicio_suave = QtWidgets.QAction(MainWindow)
        self.actionReinicio_suave.setObjectName("actionReinicio_suave")
        self.actionReinicio_fuerte = QtWidgets.QAction(MainWindow)
        self.actionReinicio_fuerte.setObjectName("actionReinicio_fuerte")
        self.actionVer_puntajes = QtWidgets.QAction(MainWindow)
        self.actionVer_puntajes.setObjectName("actionVer_puntajes")
        self.menuReinicio.addAction(self.actionReinicio_suave)
        self.menuReinicio.addAction(self.actionReinicio_fuerte)
        self.menuPuntajes.addAction(self.actionVer_puntajes)
        self.menubar.addAction(self.menuReinicio.menuAction())
        self.menubar.addAction(self.menuPuntajes.menuAction())
        MainWindow.setWindowTitle("Buscaminas")
        self.Bandera_signo_pregunta.setText(
                                            "Agregar bandera/signo de pregunta"
                                           )
        self.Label_Minas.setText("Minas")
        self.Label_Tiempo.setText("Tiempo")
        self.menuReinicio.setTitle("Reinicio")
        self.menuPuntajes.setTitle("Puntajes")
        self.actionReinicio_suave.setText("Reinicio suave")
        self.actionReinicio_fuerte.setText("Reinicio fuerte")
        self.actionVer_puntajes.setText("Ver puntajes")
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
