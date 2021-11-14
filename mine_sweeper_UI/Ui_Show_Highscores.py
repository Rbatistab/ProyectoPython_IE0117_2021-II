from PyQt5 import QtCore, QtGui, QtWidgets


class Show_highscores_dialog(object):
    def __init__(self):
        self.highscores_location = "highcores.txt"
        self.names_location = "highcores_names.txt"

    def setupUi(self, Dialog):
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

        Dialog.setObjectName("Dialog")
        Dialog.resize(685, 526)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(text)
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.ok_clicked(Dialog))
        Dialog.setWindowTitle("Puntajes")
        self.pushButton.setText("OK")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ok_clicked(self, Dialog):
        Dialog.close()
