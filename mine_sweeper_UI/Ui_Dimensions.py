#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets


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
