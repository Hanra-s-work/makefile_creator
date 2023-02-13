##
## EPITECH PROJECT, 2022
## v2
## File description:
## folders.py
##

import os

class Folders:
    def __init__(self) -> None:
        self.data_folders = "ee"

    def get_folders(self, scan_dir:str, dir_list:list[str]) -> list[str]:
        """ recursively list all the directory's and sub directory's of the specified path """
        for file in os.listdir(scan_dir):
            d = os.path.join(scan_dir, file)
            if os.path.isdir(d):
                dir_list.append(d)
                self.get_folders(d, dir_list)
        return dir_list


    def get_all_the_files(self, dir_path:str) -> list [str]:
        """ get all the files in a directory and its subdirectories """
        res = list()
        dir_list = self.get_folders(dir_path, list())
        tmp = list()
        for i in dir_list:
            if ("__pycache__" in i.split('/')) or "__pycache__" in i.split('\\'):
                continue
            tmp = os.listdir(i)
            for j in tmp:
                if os.path.isfile(f"{i}/{j}"):
                    res.append(f"{i}/{j}\t\\\n")
        return res
