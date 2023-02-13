##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## re.py
##

class Re:
    """ The class in charge of the rules for re doing an series of actions """
    def __init__(self) -> None:
        pass

    def rule_re(self) -> list[str]:
        """ Create the rule for re """
        res = list()
        res.append("re: fclean all\n")
        return res

    def rule_re_libs(self, lib_paths:list[str]) -> list[str]:
        """ Create the rule for re doing the libraries """
        res = list()
        res.append("re_libs:\n")
        for i in lib_paths:
            res.append(f"\t@make -C {i} re\n")
        return res

    def rule_re_tests(self) -> list[str]:
        """ Create the rule for re doing the unit_tests """
        res = list()
        res.append("re_tests: fclean_tests test_run\n")
        return res

    def rule_re_debug(self) -> list[str]:
        """ Create the rule for re running the program """
        res = list()
        res.append("re_debug: fclean debug\n")
        return res

    def rule_re_c11(self) -> list[str]:
        """ Create the rule for re running the program using the c11 rule """
        res = list()
        res.append("re_c11: fclean as_c11\n")
        return res

    def rule_re_c90(self) -> list[str]:
        """ Create the rule for re running the program using the c11 rule """
        res = list()
        res.append("re_c90: fclean as_c90\n")
        return res

    def rule_re_c99(self) -> list[str]:
        """ Create the rule for re running the program using the c11 rule """
        res = list()
        res.append("re_c99: fclean as_c99\n")
        return res
