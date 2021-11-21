from mine_sweeper_backend.GeneralMatrix import GeneralMatrix
from mine_sweeper_backend.mine_sweeper_backend import is_mine
from mine_sweeper_backend.mine_sweeper_backend import get_perimeter
from PyQt5 import QtCore, QtGui, QtWidgets
from mine_sweeper_UI.Ui_Show_Highscores import Show_highscores_dialog
from mine_sweeper_UI.Ui_Add_Highscores import Add_highscores_dialog
from mine_sweeper_UI.Ui_Win import Win_dialog
from mine_sweeper_UI.Ui_Lose import Lose_dialog
from mine_sweeper_UI.Ui_Resets import Resets_dialog
from mine_sweeper_UI.Ui_Ask_Add_Highscore import Ask_Add_Highscore_dialog
from mine_sweeper_UI.Ui_Invalid_Name import Invalid_Name_dialog


class grid_button(QtWidgets.QPushButton):
    def __init__(self, *args, **kargs):
        '''
        Constructs a grid button object for the UI
        '''
        super(grid_button, self).__init__(*args, **kargs)
        self.position = [0, 0]


class Ui_Game(object):
    def __init__(self, game_matrix_object):
        '''
        Constructs a Ui_Game object
        '''
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
        self.icon_mine = "mine_sweeper_UI/imgs/mine.jpg"
        self.icon_question = "mine_sweeper_UI/imgs/question.png"

        self.first_click = False
        self.flag_number = 0
        self.click_number = 0

    def setupUi(self, MainWindow, n, m, mines, bool):
        '''
        Sets up the Ui features
        '''
        self.hidden = n*m
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
        self.button_grid(n, m, bool, mines, MainWindow)
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
        '''
        Returns and QIcon object with the desired icon option
        '''
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

        icon.addPixmap(
                       QtGui.QPixmap(location),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.On
                       )

        icon.addPixmap(
                       QtGui.QPixmap(location),
                       QtGui.QIcon.Disabled,
                       QtGui.QIcon.Off
                       )

        return icon

    def button_grid(self, n, m, bool, mines, MainWindow):
        '''
        Creates a grid of buttons with "n" rows and "m" columns and sets
        it to the matrix object of the class
        '''
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
                    lambda: self.button_click(MainWindow, bool, n, m, mines)
                    )

    def button_click(self, MainWindow, bool, n, m, mines):
        '''
        Adds the functionality of the click of a button, contemplating
        it's usecases
        '''
        rbt = MainWindow.sender()
        i = rbt.position[0]
        j = rbt.position[1]

        if(not self.first_click):
            self.timer.start(1000)
            self.first_click = True

        box = self.back_matrix.matrix[i][j]
        flag_state = box.flag_state

        if(self.Bandera_signo_pregunta.isChecked()):
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
            self.lcd_minas.display(mines - self.flag_number)
        else:
            if(flag_state == "flag_state"):
                box.set_flag_state("no_flag_state")
                self.flag_number = self.flag_number - 1

            self.click_number = self.click_number + 1

            if(not is_mine(self.back_matrix.matrix[i][j])):
                self.click_and_disable(i, j, self.back_matrix)
            else:
                self.back_matrix.matrix[i][j].click_this_box()
                self.matrix[i][j].setEnabled(False)

            number_matrix = matrix_creation(n, m)
            visible_matrix = matrix_creation(n, m)
            flag_matrix = matrix_creation(n, m)

            if(is_mine(self.back_matrix.matrix[i][j])):
                for a in range(n):
                    for b in range(m):
                        self.timer.stop()
                        self.back_matrix.matrix[a][b].click_this_box()
                        self.matrix[a][b].setEnabled(False)

            for a in range(n):
                for b in range(m):
                    box = self.back_matrix.matrix[a][b]
                    if(is_mine(box)):
                        number_matrix[a][b] = -1
                        visible_matrix[a][b] = box.was_clicked
                        flag_matrix[a][b] = box.flag_state
                    else:
                        number_matrix[a][b] = box.number
                        visible_matrix[a][b] = box.was_clicked
                        flag_matrix[a][b] = box.flag_state

            # if not (is_mine(self.back_matrix.matrix[i][j])):
            #     self.set_visible_perimeter(i,
            #                                j,
            #                                self.back_matrix,
            #                                visible_matrix
            #                                )

            print(visible_matrix)

            self.hidden = n*m
            for a in range(n):
                for b in range(m):
                    if(visible_matrix[a][b]):
                        self.hidden = self.hidden - 1

            print(self.hidden)
            print(number_matrix)

            if(self.hidden == mines):
                self.timer.stop()
                try:
                    highscore = self.click_number/self.s
                except ZeroDivisionError:
                    highscore = float('inf')
                for a in range(n):
                    for b in range(m):
                        if(number_matrix[a][b] == -1):
                            self.matrix[a][b].setIcon(self.icon("flag"))
                            self.matrix[a][b].setEnabled(False)
                        elif(number_matrix[a][b] == 0):
                            self.matrix[a][b].setIcon(self.icon("0"))
                        elif(number_matrix[a][b] == 1):
                            self.matrix[a][b].setIcon(self.icon("1"))
                        elif(number_matrix[a][b] == 2):
                            self.matrix[a][b].setIcon(self.icon("2"))
                        elif(number_matrix[a][b] == 3):
                            self.matrix[a][b].setIcon(self.icon("3"))
                        elif(number_matrix[a][b] == 4):
                            self.matrix[a][b].setIcon(self.icon("4"))
                        elif(number_matrix[a][b] == 5):
                            self.matrix[a][b].setIcon(self.icon("5"))
                        elif(number_matrix[a][b] == 6):
                            self.matrix[a][b].setIcon(self.icon("6"))
                        elif(number_matrix[a][b] == 7):
                            self.matrix[a][b].setIcon(self.icon("7"))
                        elif(number_matrix[a][b] == 8):
                            self.matrix[a][b].setIcon(self.icon("8"))

                self.lcd_minas.display(0)

                self.win(MainWindow, bool, highscore)

            else:
                self.lcd_minas.display(mines - self.flag_number)

                for a in range(n):
                    for b in range(m):
                        if(visible_matrix[a][b]):
                            if(number_matrix[a][b] == -1):
                                self.matrix[a][b].setIcon(self.icon("mine"))
                            elif(number_matrix[a][b] == 0):
                                self.matrix[a][b].setIcon(self.icon("0"))
                            elif(number_matrix[a][b] == 1):
                                self.matrix[a][b].setIcon(self.icon("1"))
                            elif(number_matrix[a][b] == 2):
                                self.matrix[a][b].setIcon(self.icon("2"))
                            elif(number_matrix[a][b] == 3):
                                self.matrix[a][b].setIcon(self.icon("3"))
                            elif(number_matrix[a][b] == 4):
                                self.matrix[a][b].setIcon(self.icon("4"))
                            elif(number_matrix[a][b] == 5):
                                self.matrix[a][b].setIcon(self.icon("5"))
                            elif(number_matrix[a][b] == 6):
                                self.matrix[a][b].setIcon(self.icon("6"))
                            elif(number_matrix[a][b] == 7):
                                self.matrix[a][b].setIcon(self.icon("7"))
                            elif(number_matrix[a][b] == 8):
                                self.matrix[a][b].setIcon(self.icon("8"))
                        else:
                            if(flag_matrix[a][b] == "no_flag_state"):
                                self.matrix[a][b].setIcon(self.icon("blank"))
                            elif(flag_matrix[a][b] == "flag_state"):
                                self.matrix[a][b].setIcon(self.icon("flag"))
                            elif(flag_matrix[a][b] == "question_state"):
                                self.matrix[a][b].setIcon(
                                                          self.icon(
                                                                    "question"
                                                                    )
                                                          )

            # print(number_matrix)
            # print(visible_matrix)
            # print(flag_matrix)

            if(is_mine(self.back_matrix.matrix[i][j])):
                self.lcd_minas.display(mines)
                self.lose(MainWindow, bool)

    # def set_visible_perimeter(self, row, col, game_matrix, visible_matrix):
    #     ''''
    #     Gets the perimeter for a non-mine box and sets its fields visible
    #     in the visible_matrix
    #     '''
    #     perimeter = get_perimeter(row, col, game_matrix)
    #     for coordinate in perimeter:
    #         row = coordinate[0]
    #         col = coordinate[1]
    #         visible_matrix[row][col] = True
    #         game_matrix

    def click_and_disable(self, row, col, game_matrix):
        perimeter = get_perimeter(row, col, game_matrix)

        print(perimeter)

        for coordinate in perimeter:
            a = coordinate[0]
            b = coordinate[1]
            self.back_matrix.matrix[a][b].click_this_box()
            self.matrix[a][b].setEnabled(False)

    def LCDEvent(self):
        '''
        Displays a Timer with the game time
        '''
        self.s += 1
        self.lcd_tiempo.display(self.s)

    def show_highscores_window(self):
        '''
        Pops a window with high scores to the user
        '''
        Dialog = QtWidgets.QDialog()
        ui = Show_highscores_dialog()
        ui.setupUi(Dialog)
        Dialog.show()

    def add_highscores_window(self):
        '''
        Pops the window that allows to add a high score
        '''
        Dialog = QtWidgets.QDialog()
        ui = Add_highscores_dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()
        name = ui.name

        return name

    def win(self, MainWindow, bool, highscore):
        '''
        Manages the usecase for when the user wins
        '''
        Dialog = QtWidgets.QDialog()
        ui = Win_dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()

        Dialog = QtWidgets.QDialog()
        ui = Ask_Add_Highscore_dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()
        add = ui.add

        if(add):
            invalid_name = True
            while(invalid_name):
                name = self.add_highscores_window()
                name_split = name.splitlines()
                if(len(name_split) == 1):
                    invalid_name = False
                if(invalid_name):
                    Dialog = QtWidgets.QDialog()
                    ui = Invalid_Name_dialog()
                    ui.setupUi(Dialog)
                    Dialog.exec_()

            highscores_location = "highcores.txt"
            names_location = "highcores_names.txt"
            file = open(names_location, "a")
            file.write("{}\n".format(name))
            file.close()
            file = open(highscores_location, "a")
            file.write("{}\n".format(highscore))
            file.close()

            Dialog = QtWidgets.QDialog()
            ui = Show_highscores_dialog()
            ui.setupUi(Dialog)
            Dialog.exec_()

        Dialog = QtWidgets.QDialog()
        ui = Resets_dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()
        soft = ui.soft_reset
        hard = ui.hard_reset

        if(soft):
            self.soft_reset(MainWindow, bool)
        elif(hard):
            self.hard_reset(MainWindow, bool)

    def lose(self, MainWindow, bool):
        '''
        Manages the usecase for when the user loses
        '''
        Dialog = QtWidgets.QDialog()
        ui = Lose_dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()
        soft = ui.soft_reset
        hard = ui.hard_reset

        if(soft):
            self.soft_reset(MainWindow, bool)
        elif(hard):
            self.hard_reset(MainWindow, bool)

    def soft_reset(self, MainWindow, bool):
        '''
        Allows the user to perform a reset of the current game but with-
        out having to select dimensions and mines again.
        It sets a new game for the same selected features
        '''
        bool.soft_reset = True
        MainWindow.close()

    def hard_reset(self, MainWindow, bool):
        '''
        Allows the user to perform a full reset of the game, it will
        call again the menus to choose dimensions and mines
        '''
        bool.full_reset = True
        MainWindow.close()


def matrix_creation(n, m):
    '''
    Returns a GeneralMatrix object with size nxm
    '''
    matrix = GeneralMatrix(n, m)

    return matrix

# ----------------------- Mock ups to delete-----------------------------------

# def highcore_add_show(self):
#     name = self.add_highscores_window()
#     highscore = 0.1
#     highscores_location = "highcores.txt"
#     names_location = "highcores_names.txt"
#     file = open(names_location, "a")
#     file.write("{}\n".format(name))
#     file.close()
#     file = open(highscores_location, "a")
#     file.write("{}\n".format(highscore))
#     file.close()
#     self.show_highscores_window()
