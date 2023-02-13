##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## fold_content.py
##

import os

class FoldContent:
    """ get the content of a folder """
    def __init__(self) -> None:
        self.data_fold_content = "ee"

    def get_content(self, path):
        """ get the content of a folder """
        content = os.listdir(path)
        return content

    def get_content_list(self, path):
        """ get all the content of a folder and return it as a list """
        content = self.get_content(path)
        content_list = []
        for i in content:
            content_list.append(i)
        return content_list
