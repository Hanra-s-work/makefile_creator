##
## EPITECH PROJECT, 2022
## v2
## File description:
## __init__.py
##

from .jsons import JsonParsing
from .env import Environment

class Parsing:
    """ Parse the content of the file """
    def __init__(self) -> None:
        super().__init__()
        self.data_parsing = "ee"
        self.json_parsing = JsonParsing
        self.environement = Environment

    def test_parsing(self) -> str:
        """ The function in charge of testing the class Parsing """
        return "test function parsing"
