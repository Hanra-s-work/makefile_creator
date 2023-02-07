##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## global_vars.py
##

import json

class GlobalVars:
    def __init__(self, json_file) -> None:
        self.json_file = json_file
        self.name = "a.out"
