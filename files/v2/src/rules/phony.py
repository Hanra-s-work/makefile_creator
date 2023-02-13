##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## phony.py
##

class Phony:
    def __init__(self) -> None:
        pass

    def rule_phony(self, used_options:dict[str, bool]) -> list[str]:
        """ Create the .PHONY rule """
        res = ".PHONY:"
        max_counter = 3
        counter = 0
        for i in enumerate(used_options):
            if counter == max_counter:
                res += "\\\n"
                counter = 0
            if i[1] == True:
                res += f" {i[0]}\n\\"
                counter += 1
        final_res = list(res)
        return final_res
