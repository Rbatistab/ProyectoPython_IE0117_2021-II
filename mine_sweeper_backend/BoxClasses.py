class BoxClass:
    '''
    General box class to represent a square box un the
    minesweeper
    '''
    def __init__(self, flag_state="no_flag_state"):
        self.flag_state = flag_state
        self.was_clicked = False

    def get_box_attributes(self):
        '''
        Returns the attributes of the box
        '''
        return {
            "flag_state": self.flag_state,
            "was_clicked": self.was_clicked
        }

    def set_flag_state(self, flag_state):
        '''
        Sets a flag state
        '''
        self.flag_state = flag_state

    def click_this_box(self):
        '''
        Clicks the box
        '''
        self.was_clicked = True


    def __str__(self):
        pass


class MineBox(BoxClass):
    '''
    Represents a box with a Mine
    '''
    def __str__(self):
        return '*'


class NumberBox(BoxClass):
    '''
    Represents a box with no Mine, but a number
    '''

    def __init__(self, number = -1):
        BoxClass.__init__(self)
        self.number = number

    def get_box_attributes(self):
        '''
        Aggregates number attribute
        '''
        attributes = super().get_box_attributes()
        attributes['number'] = self.number
        return attributes

    def __str__(self):
        '''
        Overwrite to the str() method
        '''
        return str( self.number )
