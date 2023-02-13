##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## unit_testing.py
##

class UnitTesting:
    def __init__(self) -> None:
        pass

    def rule_tests_run(self) -> list[str]:
        """ Create the rule for testing the unit """
        res = list()
        res.append("test_run: compile_tests\n")
        res.append("\t./$(UNIT_NAME)\n")
        return res
