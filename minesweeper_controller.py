#!/usr/bin/python3

import sys
# from mine_sweeper_exceptions import mine_sweeper_exceptions as ms_exceptions
from mine_sweeper_UI import mine_sweeper_UI as UI


def terminate_mine_sweeper():
    # mensage de UI para el usuario de que se esta cerrando el programa
    print("Finalizando ejecution en terminate_mine_sweeper()")  # Delete this line when we are done  # noqa
    sys.exit()


class Reset_Variables:  # Necistamos crear objetos de esta clase aqui?
    '''
    This class contain boolean variables regarding the reset and closing state
    '''
    def __init__(self):
        self.full_reset = False
        self.soft_reset = False
        self.close = False


# def add_highscores(name, highscore):
#     highscores_location = "highcores.txt"
#     names_location = "highcores_names.txt"
#     file = open(names_location, "a")
#     file.write("{}\n".format(name))
#     file.close()
#     file = open(highscores_location, "a")
#     file.write("{}\n".format(highscore))
#     file.close()


def exec(RESET_BOOL):
    '''
    Executions gets the desired game information form the user and
    '''
    rows, columns, mines = UI.dimensions_mines()
    bool = RESET_BOOL

    while(not bool.full_reset and not bool.close):
        bool.soft_reset = False
        # game, boolean = initialize_game()
        print("inicializamos juego")
        # playing(game, boolean) #Lo hace el UI
        print("jugando")
        UI.game_window(rows, columns, mines, bool)


# def main():
#     try:
#         while(True):
#             exec()
#     except ms_exceptions.TerminateMineSweeper:
#         terminate_mine_sweeper()

def main():
    RESET_BOOL = Reset_Variables()
    while(not RESET_BOOL.close):
        exec(RESET_BOOL)

    print("Finalizando juego")


if __name__ == '__main__':
    # full_reset = False
    # soft_reset = False
    # En que parte queremos a usar estas variables?:
    # win = False
    # loose = False

    main()

# ----------------------- Mock ups to delete-----------------------------------

        # win = True # noqa
        # if(win): # noqa
        #     name = UI.add_highscores_window() # noqa
        #     highscore = input("Puntaje: ") # noqa
        #     add_highscores(name, highscore) # noqa
        #     print("Mostrando puntajes") # noqa
        #     UI.show_highscores_window() # noqa
        #     pass # noqa
        # raise ms_exceptions.TerminateMineSweeper # noqa
        # # noqa
        # Este reinicio se puede hacer con un boton en el UI, necesitamos meter esto en un loop? # noqa
        # while(not soft_reset and not full_reset): # noqa
        #     if win: # noqa
        #         print("Muestro puntajes") # noqa
        #         # show_win(game) #Lo hace el UI # noqa
        #         # highscore() #Lo hace el UI # noqa
        #     elif loose: # noqa
        #         print("Muestro puntajes perdida") # noqa
        #         # show_loose(game) #Lo hace el UI # noqa
