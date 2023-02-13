##
## EPITECH PROJECT, 2022
## v2
## File description:
## __init__.py
##

from .ask_questions import AskQuestion as AQ
from .colourise_output import ColouriseOutput as CO

class TTY(AQ, CO):
    """ The class TTY in charge of managing the terminal interface """
    def __init__(self, human_type: dict = ..., illegal_characters_nb: str = "") -> None:
        super().__init__(human_type, illegal_characters_nb)
        self.data_tty = "eee"

    def test_tty(self) -> str:
        """ test the tty class """
        return "tty class test"
