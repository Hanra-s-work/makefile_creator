##
# EPITECH PROJECT, 2022
# v2
# File description:
# main.py
##

from sys import argv as av
from src import Src

print("Hello  World")


class Main(Src):
    """ The class of the main program"""

    def __init__(self, json_file: str = "") -> None:
        super().__init__(av, json_file)

    def main(self, argv) -> None:
        """ The main function of the program """
        argc = len(argv)
        self.no_logo()
        self.must_show_debug()
        if self.gv.show_debug == True:
            print(f"argv = {argv}")
            print(f"argc = {argc}")
        if self.gv.display_logo == True:
            self.gui.disp.display_boot(self.gv.boot_data)
        if self.gv.show_debug == True:
            print("\n- Checking the arguments\n")
        self.check_options()
        if self.gv.show_debug == True:
            print("\n- Running the program\n")
        if self.gv.show_debug == True:
            print("\n- The program has ended\n")
        if self.gv.display_logo == True:
            self.gui.disp.display_end(self.gv.end_logo, self.gv.author)
        else:
            self.gui.disp.display_author(self.gv.author)


if __name__ == "__main__":
    SI = Src(av, "")
    MI = Main()
    MI.main(av)
