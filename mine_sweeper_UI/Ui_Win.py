from PyQt5 import QtCore, QtGui, QtWidgets


class Win_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(
                                           20,
                                           40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding
                                          )
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(40)
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
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.ok_clicked(Dialog))
        spacerItem2 = QtWidgets.QSpacerItem(
                                            20,
                                            40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding
                                           )
        self.verticalLayout.addItem(spacerItem2)
        Dialog.setWindowTitle("Ganaste")
        self.label.setText("¡Ganaste!")
        self.pushButton.setText("OK")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ok_clicked(self, Dialog):
        Dialog.close()
