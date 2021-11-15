from PyQt5 import QtCore, QtGui, QtWidgets


class Ask_Add_Highscore_dialog(object):
    def setupUi(self, Dialog):
        self.add = False
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.yes_clicked(Dialog))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(lambda: self.no_clicked(Dialog))
        self.verticalLayout.addLayout(self.horizontalLayout)
        Dialog.setWindowTitle("Pregunta sobre añadir puntaje")
        self.label.setText("¿Añadir puntaje?")
        self.pushButton.setText("Sí")
        self.pushButton_2.setText("No")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def yes_clicked(self, Dialog):
        self.add = True
        Dialog.close()

    def no_clicked(self, Dialog):
        self.add = False
        Dialog.close()
