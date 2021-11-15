from PyQt5 import QtCore, QtGui, QtWidgets


class Resets_dialog(object):
    def setupUi(self, Dialog):
        self.soft_reset = False
        self.hard_reset = False
        Dialog.setObjectName("Dialog")
        Dialog.resize(672, 527)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.soft_clicked(Dialog))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(lambda: self.hard_clicked(Dialog))
        Dialog.setWindowTitle("Reinicio")
        self.pushButton.setText("Reinicio suave")
        self.pushButton_2.setText("Reinicio Fuerte")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def soft_clicked(self, Dialog):
        self.soft_reset = True
        Dialog.close()

    def hard_clicked(self, Dialog):
        self.hard_reset = True
        Dialog.close()
