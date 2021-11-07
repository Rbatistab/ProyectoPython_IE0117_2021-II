class Menus():  # estos metodos deberian estar en una clase?

    def dim_window():
        # Linea real, descomentar cuando este lista:
        # return n, m
        # Linea de mockup, borrar
        return 9, 9

    def mine_quantity_window(self):
        # Linea real, descomentar cuando este lista:
        # return n, m
        # Linea de mockup, borrar
        return 4

    def dimensions_mines_mockup():
        # Mock up para probar controller
        return 3, 3, 4

    def dimensions_mines():
        # A window is presented that asks for dimensions, then, those dimensions
        # are validated. If there's an error the window asks again. The dimensions
        # n and m are saved
        n, m = dim_window()
        print(n)
        print(m)

        # A window is presented that asks for mine quantity, which is validated, if
        # there's an error this window asks again. The mine quantity is saved
        mines = self.mine_quantity_window(self)
        print(mines)

        return n, m, mines 



class Board:
  def create_board():
    print("board")


class PlayGame:
    def playing(game, boolean):
        # A window of the game is refreshed
        refresh_window(game)

        # On left click event the box array is refreshed
        game.refresh_boxes_left()

        # On right click event the box array is refreshed
        game.refresh_boxes_right()

        # When close button is clicked
        boolean.close = True # aqui va el terminate exception

        # When soft reset button is clicked
        boolean.soft_reset = True

        # When full reset button is clicked
        boolean.full_reset = True


    def initialize_game(n, m, mines):
        # A Game class object is created. The atribute game_matrix is an array
        # filled with box objects, that contain information about is its position,
        # an atribute with a mine or a number, and another atribute that indicates
        # the state: hidden, visible, flag or question mark.
        game = Game(n, m)

        # The defined quantity of mines are randomly placed on the boxes
        game.mine_placing(mines)

        # According to the mine placing, the numbers are written on the remaining
        # boxes
        game.number_writting()

        # A window with the game layout is created
        window_creation(n, m)

        # A Boolean_Variables object is created
        boolean = Boolean_Variables

        return game, boolean

# Mock up

# Matriz 3 x 3:

# * 1 0
# 1 2 *
# 0 0 *