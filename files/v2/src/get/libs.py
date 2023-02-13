##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## libs.py
##

import os

class Libs:
    def __init__(self) -> None:
        self.data_libs = "ee"
    def get_lib_paths(self, path:str) -> list[str]:
        """Get the names of the libraries
        Args:
            path (str): The path to the folder containing the libs
        Returns:
            list[str]: The paths te the libraries
        """

        if "./" not in path:
            path = f"./{path}"

        content = os.listdir(path)
        content_list = []
        tmp_content = list()
        for i in content:
            tmp_content = os.listdir(i)
            if 'Makefile' in tmp_content:
                content_list.append(f"{path}/{i}")
        return content_list


    def get_lib_names(self, path:list[str]) -> list[str]:
        """Get the names of the libraries

        Args:
            path (list[str]): The paths to the libraries

        Returns:
            list[str]: The names of the libraries
        """
        content_list = []
        for i in path:
            lib_name = i.split('/')[-1]
            lib_name = lib_name.lower()
            content_list.append(lib_name)
        return content_list
