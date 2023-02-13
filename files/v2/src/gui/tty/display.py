##
# EPITECH PROJECT, 2022
# v2
# File description:
# display.py
##

class Display:
    """ The class in charge of displaying the help, version and author"""

    def __init__(self) -> None:
        self.data_display = "ee"

    def display_help(self, bin_name: str, help_data: dict[str, str]) -> None:
        """ Function in charge of displaying the help """
        print("HELP:\nTHE COMMAND:")
        for i in help_data:
            print(f"\t- {bin_name} {i}\t{help_data[i]}")

    def display_version(self, version: str) -> None:
        """ Function in charge of displaying the version """
        print(f"VERSION:\t{version}")

    def display_author(self, author: str) -> None:
        """ Function in charge of displaying the author """
        print(f"AUTHOR:\t{author}")

    def display_program_name(self, prog_name: str) -> None:
        """ Function in charge of displaying the program name """
        print(f"NAME:\t{prog_name}")

    def display_options(self, options: list[str]) -> None:
        """ Function in charge of displaying the options """
        print("OPTIONS:")
        for i in options:
            print(f"\t- {i}")

    def display_usage(self, usage: str) -> None:
        """ Function in charge of displaying the usage """
        print(f"USAGE:\t{usage}")

    def display_success(self, success: str) -> None:
        """ Function in charge of displaying the success """
        print(f"SUCCESS:\t{success}")

    def display_error(self, error: str) -> None:
        """ Function in charge of displaying the error """
        print(f"ERROR:\t{error}")

    def display_warning(self, warning: str) -> None:
        """ Function in charge of displaying the warning """
        print(f"WARNING:\t{warning}")

    def display_description(self, description: str) -> None:
        """ Function in charge of displaying the description """
        print(f"DESCRIPTION:\t{description}")

    def display_example(self, example: str) -> None:
        """ Function in charge of displaying the example """
        print(f"EXAMPLE:\t{example}")

    def display_return(self, return_value: str) -> None:
        """ Function in charge of displaying the return """
        print(f"RETURN:\t{return_value}")

    def display_exit(self, exit_value: str) -> None:
        """ Function in charge of displaying the exit """
        print(f"EXIT:\t{exit_value}")

    def display_error_code(self, error_code: str) -> None:
        """ Function in charge of displaying the error code """
        print(f"ERROR CODE:\t{error_code}")

    def display_program_logo(self, logo: list[str]) -> None:
        """ Function in charge of displaying the logo """
        if len(logo) > 0:
            for i in logo:
                print(f"{i}")

    def display_boot(self, data: dict) -> None:
        """ Function in charge of displaying the boot """
        print("BOOT:\n- The program is starting...")
        self.display_program_logo(data["logo"])
        print("")
        self.display_program_name(data["prog_name"])
        self.display_author(data["author"])
        self.display_version(data["version"])
        print("")

    def display_end(self, end_logo: list, author: str) -> None:
        """ Function in charge of displaying the end """
        self.display_program_logo(end_logo)
        self.display_author(author)
