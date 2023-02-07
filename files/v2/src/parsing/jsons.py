##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## jsons.py
##

import json

class JsonParsing:
    def __init__(self, json_path:str) -> None:
        self.json_content = self.get_content(json_path)

    def get_content(filepath:str) -> dict:
        """ Get the content of a json file """
        f = open(filepath, "r", encoding="utf-8")
        content = f.read()
        f.close()
        if content.isspace() == True or len(content) == 0:
            content = str(dict())
        json_file = json.loads(content)
        return json_file
