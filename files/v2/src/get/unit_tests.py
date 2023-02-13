##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## unit_tests.py
##

import os
from .folders import Folders

class UnitTest(Folders):
    """ The class in charge of getting unit_tests """
    def __init__(self) -> None:
        super().__init__()
        self.data_unit_test = "ee"
    
    def get_unit_tests(self, dir_path:str) -> list[str]:
        """ get all the unit_tests in a directory and its subdirectories """
        res = list()
        tmp = list()
        dir_list = self.get_folders(dir_path, list())
        for i in dir_list:
            tmp = os.listdir(i)
            for j in tmp:
                if os.path.isfile(f"{i}/{j}") and j.endswith(".c"):
                    res.append(f"{i}/{j}\t\\\n")
        return res
