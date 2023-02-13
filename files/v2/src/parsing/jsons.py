##
# EPITECH PROJECT, 2022
# makator_v2 (Workspace)
# File description:
# jsons.py
##

import json


class JsonParsing:
    def __init__(self, json_path: str) -> None:
        self.json_path = json_path
        self.json_content = dict()

    def get_content(self, filepath: str) -> dict:
        """ Get the content of a json file """
        f = open(filepath, "r", encoding="utf-8")
        content = f.read()
        f.close()
        if content.isspace() == True or len(content) == 0:
            content = str(dict())
        json_file = json.loads(content)
        return json_file

    def update_json(self, src: dict, dest: dict, i: str, j: str) -> dict:
        """ Update the json file """
        if i in src:
            if j in src[i]:
                for h in src[i][j]:
                    dest[h] = src[i][j][h]
        return dest

    def start_parsing(self) -> None:
        """ Parse the content of the json file """
        self.json_content = self.get_content(self.json_path)
