##
# EPITECH PROJECT, 2022
# v2
# File description:
# __init__.py
##

from .gui import GUI as GUII


class GUI(GUII):
    """ The graphic part of the program """

    def __init__(self) -> None:
        """ The global vars of the class """
        self.data_gui2 = "ee"
        self.gui = GUII()

    def test_gui(self) -> str:
        """ test function """
        return "test function GUI"
