#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
# from mine_sweeper_UI import mine_sweeper_UI as UI
from mine_sweeper_UI.Ui_Show_Highscores import Show_highscores_dialog
from mine_sweeper_UI.Ui_Add_Highscores import Add_highscores_dialog


class grid_button(QtWidgets.QPushButton):
    def __init__(self, *args, **kargs):
        super(grid_button, self).__init__(*args, **kargs)
        self.position = [0, 0]


class Ui_Game(object):
    def __init__(self, game_matrix_object):
        self.back_matrix = game_matrix_object
        self.icon_0 = "mine_sweeper_UI/imgs/0.jpg"
        self.icon_1 = "mine_sweeper_UI/imgs/1.jpg"
        self.icon_2 = "mine_sweeper_UI/imgs/2.jpg"
        self.icon_3 = "mine_sweeper_UI/imgs/3.jpg"
        self.icon_4 = "mine_sweeper_UI/imgs/4.jpg"
        self.icon_5 = "mine_sweeper_UI/imgs/5.jpg"
        self.icon_6 = "mine_sweeper_UI/imgs/6.jpg"
        self.icon_7 = "mine_sweeper_UI/imgs/7.jpg"
        self.icon_8 = "mine_sweeper_UI/imgs/8.jpg"
        self.icon_blank = "mine_sweeper_UI/imgs/blank.png"
        self.icon_flag = "mine_sweeper_UI/imgs/flag.png"
        self.icon_mine = "mine_sweeper_UI/imgs/mine.png"
        self.icon_question = "mine_sweeper_UI/imgs/question.png"

        self.first_click = False
        self.flag_number = 0
        self.click_number = 0

    def setupUi(self, MainWindow, n, m, mines, bool):
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
        self.lcd_minas.display(mines - self.flag_number)
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
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.LCDEvent)
        self.s = 0
        self.verticalLayout_2.addWidget(self.lcd_tiempo)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_grid(n, m, mines, MainWindow)
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
        self.actionReinicio_suave.triggered.connect(
                                                    lambda:
                                                    self.soft_reset(
                                                                    MainWindow,
                                                                    bool
                                                                   )
                                                   )
        self.menuReinicio.addAction(self.actionReinicio_fuerte)
        self.actionReinicio_fuerte.triggered.connect(
                                                     lambda:
                                                     self.hard_reset(
                                                                    MainWindow,
                                                                    bool
                                                                    )
                                                    )
        self.menuPuntajes.addAction(self.actionVer_puntajes)
        self.actionVer_puntajes.triggered.connect(self.show_highscores_window)
        self.menubar.addAction(self.menuReinicio.menuAction())
        self.menubar.addAction(self.menuPuntajes.menuAction())
        MainWindow.setWindowTitle("Buscaminas")
        self.Bandera_signo_pregunta.setText("Etiquetar casilla oculta")
        self.Label_Minas.setText("Minas")
        self.Label_Tiempo.setText("Tiempo")
        self.menuReinicio.setTitle("Reinicio")
        self.menuPuntajes.setTitle("Puntajes")
        self.actionReinicio_suave.setText("Reinicio suave")
        self.actionReinicio_fuerte.setText("Reinicio fuerte")
        self.actionVer_puntajes.setText("Ver puntajes")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def icon(self, option):
        icon = QtGui.QIcon()
        if(option == "0"):
            location = self.icon_0
        elif(option == "1"):
            location = self.icon_1
        elif(option == "2"):
            location = self.icon_2
        elif(option == "3"):
            location = self.icon_3
        elif(option == "4"):
            location = self.icon_4
        elif(option == "5"):
            location = self.icon_5
        elif(option == "6"):
            location = self.icon_6
        elif(option == "7"):
            location = self.icon_7
        elif(option == "8"):
            location = self.icon_8
        elif(option == "blank"):
            location = self.icon_blank
        elif(option == "flag"):
            location = self.icon_flag
        elif(option == "mine"):
            location = self.icon_mine
        elif(option == "question"):
            location = self.icon_question

        icon.addPixmap(
                       QtGui.QPixmap(location),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off
                       )

        return icon

    def button_grid(self, n, m, mines, MainWindow):
        self.matrix = matrix_creation(n, m)
        font = QtGui.QFont()
        font.setPointSize(24)
        for a in range(n):
            for b in range(m):
                self.matrix[a][b] = grid_button(self.centralwidget)
                self.matrix[a][b].setObjectName("OK_Button{}{}".format(a, b))
                self.matrix[a][b].position = [a, b]
                # self.matrix[a][b].setFont(font)
                # self.matrix[a][b].setText("")
                self.matrix[a][b].setIcon(self.icon("blank"))
                self.matrix[a][b].setIconSize(QtCore.QSize(38, 38))
                self.gridLayout.addWidget(self.matrix[a][b], a, b, 1, 1)
                # print(a, b)
                self.matrix[a][b].clicked.connect(
                    lambda: self.button_click(MainWindow, mines)
                    )

    def button_click(self, MainWindow, mines):
        rbt = MainWindow.sender()
        i = rbt.position[0]
        j = rbt.position[1]

        if(not self.first_click):
            print("first")
            self.timer.start(1000)
            self.first_click = True

        if(self.Bandera_signo_pregunta.isChecked()):
            box = self.back_matrix.matrix[i][j]
            flag_state = box.flag_state
            if(flag_state == "no_flag_state"):
                self.flag_number = self.flag_number + 1
                self.matrix[i][j].setIcon(self.icon("flag"))
                box.set_flag_state("flag_state")
            elif(flag_state == "flag_state"):
                self.flag_number = self.flag_number - 1
                self.matrix[i][j].setIcon(self.icon("question"))
                box.set_flag_state("question_state")
            elif(flag_state == "question_state"):
                self.matrix[i][j].setIcon(self.icon("blank"))
                box.set_flag_state("no_flag_state")
        else:
            self.click_number = self.click_number + 1
            print(self.click_number)

        self.lcd_minas.display(mines - self.flag_number)

    def LCDEvent(self):
        self.s += 1
        self.lcd_tiempo.display(self.s)

    def show_highscores_window(self):
        Dialog = QtWidgets.QDialog()
        ui = Show_highscores_dialog()
        ui.setupUi(Dialog)
        Dialog.show()

    def add_highscores_window(self):
        Dialog = QtWidgets.QDialog()
        ui = Add_highscores_dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()
        name = ui.name

        return name

    def highcore_add_show(self):
        name = self.add_highscores_window()
        highscore = 0.1
        highscores_location = "highcores.txt"
        names_location = "highcores_names.txt"
        file = open(names_location, "a")
        file.write("{}\n".format(name))
        file.close()
        file = open(highscores_location, "a")
        file.write("{}\n".format(highscore))
        file.close()
        self.show_highscores_window()

    def soft_reset(self, MainWindow, bool):
        bool.soft_reset = True
        MainWindow.close()

    def hard_reset(self, MainWindow, bool):
        bool.full_reset = True
        MainWindow.close()


def matrix_creation(n, m):
    matrix = []

    for _ in range(n):
        matrix.append([])

    for a in range(n):
        for _ in range(m):
            matrix[a].append([])

    return matrix
