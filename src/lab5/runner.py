import sys

from UI.MenuBuilder import *
from UI.MenuItem import *
from Core.ThreeDArtService import ThreeDArtService


gen = ThreeDArtService(5, 0, False)

white = MenuItem("1", "White.", gen.change_color, [0])
red = MenuItem("2", "Red.", gen.change_color, [91])
blue = MenuItem("3", "Blue.", gen.change_color, [94])

change_color_menu = MenuBuilder([white, red, blue])

create_item = MenuItem("1", "Create a cube.", gen.print_art)
change_color = MenuItem("2", "Change art color.", change_color_menu.initialize)
change_size = MenuItem("3", "Change art size.", gen.change_size)
change_direction = MenuItem("4", "Change art direction.", gen.change_direction)
save_art = MenuItem("5", "Save art.", gen.save_art_into_file, ["./Data/art.txt"])
see_art = MenuItem("6", "See previous arts.", gen.get_art_archive, ["./Data/art.txt"])
exit_menu = MenuItem("9", "Exit.", sys.exit)

main_menu = MenuBuilder([create_item, change_color, change_size, change_direction, save_art, see_art, exit_menu])


def main():
    while True:
        main_menu.initialize()


if __name__ == "__main__":
    main()
