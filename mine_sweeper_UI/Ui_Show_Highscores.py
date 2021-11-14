#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Show_Highscores(object):
    def __init__(self):
        self.highscores_location = "highcores.txt"
        self.names_location = "highcores_names.txt"

    def setupUi(self, MainWindow):
        file = open(self.highscores_location, "r")
        highcores_values = file.read().splitlines()
        file.close()
        file = open(self.names_location, "r")
        highcores_names = file.read().splitlines()
        file.close()
        length = len(highcores_values)
        vector_sort = []

        for a in range(length):
            vector_sort.append([a, float(highcores_values[a])])

        vector_sort.sort(key=lambda x: x[1], reverse=True)
        text = ""

        for a in range(length):
            sort_index = vector_sort[a][0]
            text = text + "{}. {}: {}\n".format(
                                              a+1,
                                              highcores_names[sort_index],
                                              highcores_values[sort_index]
                                             )

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(text)
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.ok_clicked(MainWindow))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowTitle("Puntajes")
        self.pushButton.setText("OK")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def ok_clicked(self, MainWindow):
        MainWindow.close()

    def takeSecond(elem):
        '''
        Gives the second element
        '''
        return elem[1]
