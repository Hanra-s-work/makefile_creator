##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## compiling.py
##

class Compiling:
    def __init__(self) -> None:
        pass

    def rule_all(self) -> list[str]:
        """ Create the rule in charge of compiling the files """
        res = list()
        res.append("all: $(NAME)\n\n")
        res.append("$(NAME): compile_libs $(OBJ)\n")
        res.append("\t$(CC) -o $(NAME) $(OBJ) $(LIB)\n")
        return res

    def rule_debug(self) -> list[str]:
        """ Create the debug rule """
        res = list()
        res.append("debug: CFLAGS\t+=\t-g3\n")
        res.append("debug: NAME\t:=\t$(NAME)_debug\n")
        res.append("debug: all\n")
        return res

    def rule_compile_libs(self, lib_paths:list[str]) -> list[str]:
        """" Create the rule in charge of compiling the libs of the program """
        res = list()
        res.append("compile_libs:\n")
        for i in lib_paths:
            res.append(f"\t@make -C {i}\n")
        return res

    def rule_compile_test(self) -> list[str]:
        """ Create the rule in charge of compiling the unit_tests """
        res = list()
        res.append("compile_tests:\n")
        res.append("\t$(CC) -o $(UNIT_NAME) $(UNIT_TESTS) $(LIB) $(CFLAGS)\t\\\n")
        return res

    def rule_as_c11(self) -> list[str]:
        """ Create the rule in charge of compiling the files using the c11 rule """
        res = list()
        res.append("as_c11: CFLAGS\t+=\t-std=c11\n")
        res.append("as_c11: all\n")
        return res

    def rule_as_c90(self) -> list[str]:
        """ Create the rule in charge of compiling the files using the c90 rule """
        res = list()
        res.append("as_c90: CFLAGS\t+=\t-std=c90\n")
        res.append("as_c90: all\n")
        return res

    def rule_as_c99(self) -> list[str]:
        """ Create the rule in charge of compiling the files using the c99 rule """
        res = list()
        res.append("as_c99: CFLAGS\t+=\t-std=c99\n")
        res.append("as_c99: all\n")
        return res

    def rule_as_lib(self) -> list[str]:
        """ Create the rule in charge of compiling the files as a library """
        res = list()
        res.append("as_lib: NAME\t:=\tlib$(NAME).a\n")
        res.append("as_lib: compile_libs $(PROG_OBJ)\n")
        res.append("\t$(SILENT)ar rc $(NAME) $(PROG_OBJ)\n")
        return res
