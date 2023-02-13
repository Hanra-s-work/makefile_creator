##
## EPITECH PROJECT, 2022
## v2
## File description:
## add.py
##

import datetime

class Add:
    def __init__(self):
        self.data_add = "ee"

    def header(self, title:str, description:str) -> list[str]:
        """ Create the header of the makefile """
        res = list()
        res.append("##")
        res.append(f"## EPITECH PROJECT, {datetime.datetime.now().year}")
        res.append(f"## {title}")
        res.append("## File description:")
        res.append(f"## {description}")
        res.append("##")
        return res

    def libs(self, lib_paths:list[str], lib_includes:list[str]) -> str:
        """ Create the libs part of the makefile """
        res = "LIBS\t=\t"
        for i in range(len(lib_includes)):
            res += f"\t\t-L{lib_paths[i]} "
            res += f"-l{lib_includes[i]}\t\\\n"
        return res
