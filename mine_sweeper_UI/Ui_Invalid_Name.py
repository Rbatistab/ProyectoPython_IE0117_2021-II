from PyQt5 import QtCore, QtGui, QtWidgets


class Invalid_Name_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20,
                                           40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding
                                           )
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(
                                            20,
                                            40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding
                                            )
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(
                                            20,
                                            40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding
                                            )
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.ok_clicked(Dialog))
        spacerItem3 = QtWidgets.QSpacerItem(
                                            20,
                                            40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding
                                            )
        self.verticalLayout.addItem(spacerItem3)
        Dialog.setWindowTitle("Advertencia de nombre inválido")
        self.label.setText("El nombre debe ser de una línea")
        self.label_2.setText("Ingrese un nombre válido")
        self.pushButton.setText("OK")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ok_clicked(self, Dialog):
        Dialog.close()
