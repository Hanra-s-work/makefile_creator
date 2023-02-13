##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## cleaning.py
##

class Cleaning:
    def __init__(self) -> None:
        pass

    def rule_clean(self) -> list[str]:
        """ Create the rule for cleaning the object files """
        res = list()
        res.append("clean:\n")
        res.append("\t@rm -f $(OBJ)\n")
        return res

    def rule_clean_libs(self, lib_paths:list[str]) -> list[str]:
        """ Create the rule for cleaning the libraries """
        res = list()
        res.append("clean_libs:\n")
        for i in lib_paths:
            res.append(f"\t@make -C {i} clean\n")
        return res

    def rule_clean_tests(self) -> list[str]:
        """ Create the rule for cleaning the unit_tests files """
        res = list()
        res.append("clean_tests:\n")
        res.append("\t@rm -f *.gcda\t\n")
        res.append("\t@rm -f *.gcno\t\n")
        return res
