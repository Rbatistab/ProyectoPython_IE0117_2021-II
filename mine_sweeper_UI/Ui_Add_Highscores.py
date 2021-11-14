from PyQt5 import QtCore, QtGui, QtWidgets


class Add_highscores_dialog(object):
    def setupUi(self, Dialog):
        self.name = ""
        self.open = True
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.ok_clicked(Dialog))
        Dialog.setWindowTitle("Agregar puntaje")
        self.label.setText("Ingrese su nombre")
        self.pushButton.setText("OK")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ok_clicked(self, Dialog):
        self.name = self.plainTextEdit.toPlainText()
        Dialog.close()

    def closeEvent(self, event):
        self.open = False
