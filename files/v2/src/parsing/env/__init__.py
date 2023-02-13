##
## EPITECH PROJECT, 2022
## v2
## File description:
## __init__.py
##

from .constants import Const as CONST
from .env import Environment as Environmenti

class Environment(Environmenti):
    """ The environment class of the graphic part of the program """
    def __init__(self,error:int=CONST().ERROR, success:int=CONST().SUCCESS, env_file:str=CONST().ENV_FILE) -> None:
        super().__init__(error, success, env_file)
        self.data_environement = "ee"

    def test_env(self) -> str:
        """ Test function env"""
        return "test function env"
