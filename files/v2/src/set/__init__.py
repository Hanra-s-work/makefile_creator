##
# EPITECH PROJECT, 2022
# v2
# File description:
# __init__.py
##

from .basic_flags import BasiFlags
from .coverage_flags import CoverageFlags
from .debug_flags import DebugFlags
from .grapical_flags import GraphicalFlags
from .retro_compatible_flags import RetroCompatibleFlags
from .unit_test_flags import UnitTestFlags


class Set(BasiFlags, DebugFlags, CoverageFlags, RetroCompatibleFlags, GraphicalFlags, UnitTestFlags):
    """ Set variables corresponding to the variable section in the file """

    def __init__(self) -> None:
        super().__init__()
        self.data_set = "eeee"

    def test_set(self) -> str:
        """ Test the class Set of the program """
        return "test class set"
