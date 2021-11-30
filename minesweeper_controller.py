#!/usr/bin/python3

from mine_sweeper_UI import mine_sweeper_UI as UI


class Reset_Variables:
    '''
    This class contain boolean variables regarding the reset and closing state
    '''

    def __init__(self):
        self.full_reset = False
        self.soft_reset = False
        self.close = False


def exec(RESET_BOOL):
    '''
    Executions gets the desired game information form the user and
    '''
    rows, columns, mines = UI.dimensions_mines()
    bool = RESET_BOOL
    bool.full_reset = False

    while(not bool.full_reset and not bool.close):
        bool.soft_reset = False
        print("inicializamos juego")
        print("Jugando")
        UI.game_window(rows, columns, mines, bool)


def main():
    RESET_BOOL = Reset_Variables()
    while(not RESET_BOOL.close):
        exec(RESET_BOOL)

    print("Finalizando juego")


if __name__ == '__main__':

    main()
