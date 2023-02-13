##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## coverage_testing.py
##

class CoverageTesting:
    def __init__(self) -> None:
        pass

    def rule_test_coverage(self) -> list[str]:
        """ Create the rule for testing the coverage """
        res = list()
        res.append("test_coverage:\n")
        res.append("\tgcovr .\n")
        return res
