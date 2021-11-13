import sys

sys.path.append('../ProyectoPython_IE0117_2021-II')

from mine_sweeper_backend.BoxClasses import BoxClass as BoxClass
from mine_sweeper_backend.BoxClasses import NumberBox as NumberBox
from mine_sweeper_backend.BoxClasses import MineBox as MineBox


# Testing parent class
my_parent_box = BoxClass()
print("Default Parent box:")
print("Constructora alone:")
print(my_parent_box.get_box_attributes())
print("Testing flags:")
print("Changing flag state:")
my_parent_box.set_flag_state("question mark flag")
print(my_parent_box.get_box_attributes())
print("Testing click:")
my_parent_box.click_this_box()
print("Clicking box:")
print(my_parent_box.get_box_attributes())


# Testing number box class
print("\nTesting NUmberBox child class")
my_default_number_box = NumberBox(5)
print("Constructora alone:")
print(my_default_number_box.get_box_attributes())
print("Changing flag state:")
my_default_number_box.set_flag_state("single_flag")
print(my_default_number_box.get_box_attributes())
my_default_number_box.click_this_box()
print("Clicking box:")
print(my_default_number_box.get_box_attributes())


# Testing mine box
print("\nTesting MineBox child class of BoxClass")
my_mine_box = MineBox()
print("Constructora alone:")
print(my_mine_box.get_box_attributes())
print("Changing flag state:")
my_mine_box.set_flag_state("single_flag")
print(my_mine_box.get_box_attributes())
my_mine_box.click_this_box()
print("Clicking box:")
print(my_mine_box.get_box_attributes())




