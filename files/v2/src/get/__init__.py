##
## EPITECH PROJECT, 2022
## v2
## File description:
## __init__.py
##

from .fold_content import FoldContent
from .libs import Libs
from .unit_tests import UnitTest

class Get(FoldContent, Libs, UnitTest):
    """ The class in charge of gathering content """
    def __init__(self) -> None:
        super().__init__()
        self.data_get = "ee"

    def test_get(self) -> str:
        """ Test the class Get """
        return "test class get"

