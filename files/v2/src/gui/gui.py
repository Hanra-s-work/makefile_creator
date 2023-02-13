##
# EPITECH PROJECT, 2022
# v2
# File description:
# gui.py
##

from .tty import TTY
from .tkinter import Tkinter
from .options import Options
from .ncurse import Ncurse
from .tty.display import Display as Disp


class GUI:
    """ The graphic part of the program """

    def __init__(self) -> None:
        self.data_gui1 = "ee"
        self.tty = TTY
        self.tkinter = Tkinter
        self.options = Options
        self.ncurse = Ncurse
        self.disp = Disp()

    def test_function_gui(self) -> str:
        """ Test the function of the gui """
        return "Test Function GUI (inner file)"
