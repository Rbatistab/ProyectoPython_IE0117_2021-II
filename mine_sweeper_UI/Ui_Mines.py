#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.Cantidad_de_minas_spin.setMaximum(max_mines)
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
