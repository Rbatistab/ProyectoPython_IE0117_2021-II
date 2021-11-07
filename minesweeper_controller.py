#!/usr/bin/python3

import sys
from mine_sweeper_UI import mine_sweeper_UI as UI

class TerminateMineSweeper(Exception):
    pass

def terminate_mine_sweeper():
    # mensage de UI para el usuario de que se esta cerrando el programa
    print("Finalizando ejecution en terminate_mine_sweeper()") # Delete this line when we are done
    sys.exit()


class Reset_Variables: # Necistamos crear objetos de esta clase aqui?
    '''
    This class contain boolean variables regarding the reset and closing state
    '''
    def __init__(self):
        self.full_reset = False
        self.soft_reset = False


def exec():
    # n, m, mines = dimensions_msines() # UI le pregunta al usuario por la dimension de las minas?
    print("Pedir dimensiones al usuario")

    while(not full_reset):
        # game, boolean = initialize_game()
        print("inicializamos juego")
        # playing(game, boolean) #Lo hace el UI
        print("jugando")
        print("Mostrando puntajes")
        raise TerminateMineSweeper


        # Este reinicio se puede hacer con un boton en el UI, necesitamos meter esto en un loop?
        # while(not soft_reset and not full_reset):
        #     if win:
        #         print("Muestro puntajes")
        #         # show_win(game) #Lo hace el UI
        #         # highscore() #Lo hace el UI
        #     elif loose:
        #         print("Muestro puntajes perdida")
        #         # show_loose(game) #Lo hace el UI


def main():
    try:
        while(True):
            exec()
    except TerminateMineSweeper:
        terminate_mine_sweeper()


if __name__ == '__main__':
    full_reset = False
    soft_reset = False
    # En que parte queremos a usar estas variables?:
    win = False
    loose = False

    main()
