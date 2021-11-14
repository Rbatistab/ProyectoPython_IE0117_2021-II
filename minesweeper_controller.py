#!/usr/bin/python3

import sys
from mine_sweeper_exceptions import mine_sweeper_exceptions as ms_exceptions
from mine_sweeper_UI import mine_sweeper_UI as UI


def terminate_mine_sweeper():
    # mensage de UI para el usuario de que se esta cerrando el programa
    print("Finalizando ejecution en terminate_mine_sweeper()")  # Delete this line when we are done
    sys.exit()


class Reset_Variables:  # Necistamos crear objetos de esta clase aqui?
    '''
    This class contain boolean variables regarding the reset and closing state
    '''
    def __init__(self):
        self.full_reset = False
        self.soft_reset = False


# def add_highscores(name, highscore):
#     highscores_location = "highcores.txt"
#     names_location = "highcores_names.txt"
#     file = open(names_location, "a")
#     file.write("{}\n".format(name))
#     file.close()
#     file = open(highscores_location, "a")
#     file.write("{}\n".format(highscore))
#     file.close()


def exec():
    '''
    Executions gets the desired game information form the user and
    '''
    # Descomentar esta linea en la version final
    # rows, columns, mines = UI.Menus.dimensions_mines()

    # Linea de testing:
    # rows, columns, mines = UI.Menus.dimensions_mines_mockup()
    rows, columns, mines = UI.dimensions_mines()
    print("rows: ", rows)
    print("cols: ", columns)
    print("mines: ", mines)

    bool = Reset_Variables()

    while(not bool.full_reset):
        # game, boolean = initialize_game()
        print("inicializamos juego")
        # playing(game, boolean) #Lo hace el UI
        print("jugando")
        UI.game_window(rows, columns, mines, bool)


def main():
    try:
        while(True):
            exec()
    except ms_exceptions.TerminateMineSweeper:
        terminate_mine_sweeper()


if __name__ == '__main__':
    # full_reset = False
    # soft_reset = False
    # En que parte queremos a usar estas variables?:
    # win = False
    # loose = False

    main()

# ----------------------- Mock ups to delete-----------------------------------

        # win = True
        # if(win):
        #     name = UI.add_highscores_window()
        #     highscore = input("Puntaje: ")
        #     add_highscores(name, highscore)
        #     print("Mostrando puntajes")
        #     UI.show_highscores_window()
        #     pass
        # raise ms_exceptions.TerminateMineSweeper
        #
        # Este reinicio se puede hacer con un boton en el UI, necesitamos meter esto en un loop?
        # while(not soft_reset and not full_reset):
        #     if win:
        #         print("Muestro puntajes")
        #         # show_win(game) #Lo hace el UI
        #         # highscore() #Lo hace el UI
        #     elif loose:
        #         print("Muestro puntajes perdida")
        #         # show_loose(game) #Lo hace el UI
