##
## EPITECH PROJECT, 2022
## v2
## File description:
## __init__.py
##

from .content import Content

class Write(Content):
    """ Write the content of the processed data to a file """
    def __init__(self) -> None:
        super().__init__()
        self.data_write = "ee"

    def test_write(self) -> str:
        """ Test the class Write """
        return "test class write"
