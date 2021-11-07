#!/usr/bin/python3

import sys

class TerminateMineSweeper(Exception):
    pass

def terminate_mine_sweeper():
    # mensage de UI para el usuario de que se esta cerrando el programa
    sys.exit()


class Reset_Variables:
    '''
    This class contain boolean variables regarding the reset and closing state
    '''
    def __init__(self):
        self.full_reset = False
        self.soft_reset = False


def exec():
    # n, m, mines = dimensions_mines() # UI le pregunta al usuario por la dimension de las minas?
    print("Pedir dimensiones al usuario")

    while(not full_reset):
        # game, boolean = initialize_game()
        print("inicializamos juego")


        while(not soft_reset and not full_reset):
            # playing(game, boolean) #Lo hace el UI
            print("jugando")

            if win:
                print("Muestro puntajes")
                # show_win(game) #Lo hace el UI
                # highscore() #Lo hace el UI
            elif loose:
                print("Muestro puntajes perdida")
                # show_loose(game) #Lo hace el UI


def main():
    try:
        while(True):
            exec()
    except TerminateMineSweeper:
        terminate_mine_sweeper()


if __name__ == '__main__':
    close = False
    full_reset = False
    soft_reset = False
    win = False
    loose = False

    main()

# Archivo 1 -> consume al archivo 2  DONE!
# Logica de altisimo nivel
# Iniciar el juego
# Jugar
# cerrar

# Archivo 2 -> consume al archivo 3
# logica UI (segundo alto nivel):
# preguntar dimensiones
# preguntar minas
# Pintar matriz
# Permitir jugar
# Mostrar iconitos
# permitir reiniciar
# Permitir salir

# Archivo 3
# Logica de bajo nivel - backend
# Crear Matriz
# Distribuir minas