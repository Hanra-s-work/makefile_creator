##
## EPITECH PROJECT, 2022
## v2
## File description:
## __init__.py
##

from .compiling import Compiling
from .cleaning import Cleaning
from .full_cleaning import FullCleaning
from .unit_testing import UnitTesting
from .coverage_testing import CoverageTesting
from .re import Re
from .phony import Phony

class Rules(Compiling, Cleaning, FullCleaning, UnitTesting, CoverageTesting, Re, Phony):
    """" The functions in charge of creating the required rules for a makefile """
    def __init__(self) -> None:
        super().__init__()
        self.data_rules = "ee"

    def test_rules(self) -> str:
        """ The function in charge of testing the class Rules """
        return "test function rules"
