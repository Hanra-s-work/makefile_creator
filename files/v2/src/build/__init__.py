##
# EPITECH PROJECT, 2022
# v2
# File description:
# __init__.py
##

from .build import Build as Buildi


class Build:
    """ The build class of the build section of the program """

    def __init__(self) -> None:
        self.data_build2 = "ee"
        self.build = Buildi

    def test_build(self):
        """ Test the class Build """
        return "test class build"
