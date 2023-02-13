##
# EPITECH PROJECT, 2022
# v2
# File description:
# __init__.py
##

from .add import Add as Addi


class Add:
    """ Class Add in charge of managing the add functions """

    def __init__(self) -> None:
        self.data_add = "ee"
        self.add = Addi

    def test_add(self) -> str:
        """ test function """
        return "test function"
