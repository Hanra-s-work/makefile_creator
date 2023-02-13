##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## full_cleaning.py
##

class FullCleaning:
    def __init__(self) -> None:
        pass

    def rule_fclean(self) -> list[str]:
        """ Create the rule for cleaning the object files """
        res = list()
        res.append("fclean:\n")
        res.append("\t@rm -f $(NAME)\n")
        res.append("\t@rm -f $(NAME)_debug\n")
        return res

    def rule_fclean_libs(self, lib_paths:list[str]) -> list[str]:
        """ Create the rule for cleaning the libraries """
        res = list()
        res.append("fclean_libs:\n")
        for i in lib_paths:
            res.append(f"\t@make -C {i} fclean\n")
        return res

    def rule_fclean_tests(self) -> list[str]:
        """ Create the rule for cleaning the unit_tests files """
        res = list()
        res.append("fclean_tests:\n")
        res.append("\t@rm -f $(UNIT_NAME)\t\n")
        return res
