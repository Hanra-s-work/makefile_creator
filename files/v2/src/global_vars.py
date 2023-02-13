##
# EPITECH PROJECT, 2022
# makator_v2 (Workspace)
# File description:
# global_vars.py
##

import platform
from sys import argv
from datetime import datetime


class GlobalVars:
    """ The basic data of the program """

    def __init__(self, json_file: str = "") -> None:
        """ The local global variables """
        # ----- debug status -----
        self.show_debug = False
        # ----- Json data -----
        self.json_file = json_file
        self.json_content = dict()
        # ----- Program Name -----
        self.program_name = "Makator"
        # ----- Bin Name -----
        self.name = "a.out"
        # ----- Program Version -----
        self.version = "1.0.0"
        # ----- Help Options -----
        self.help = {
            "-h (or --help)": "Display this help section",
            "-v": "Display the version",
            "-a": "Display the name of the Author",
            "-mo <new_name>": "Change the default output name (Makefile)",
            "-nc": "Run this program without colors",
            "-nl": "Run this program without displaying any logos",
            "-oh <new_name>": "Specify the name of the header file",
            "-p <path>": "Change the directory in wich the program starts scanning\n\t\t\t(The default path is the directory in wich the program is running)",
            "-hi <path>": "Change the directory in wich the include folder is \n\t\t\t(if the include folder it not existent it will be created).",
            "-mi <path>": "Change the directory in wich the include folder is.\n\t\t\tThis is for when the program is generating a makefile.",
            "-hn <name>": "Change the name of the headerfile.",
            "-ht <title>": "Change the title for the header file's header\n\t\t\t(by default: header)",
            "-hd <description>": "Change the description for the header file's description\n\t\t\t(by default: jitter jitter)",
            "-mt <title>": "Change the title for the makefile header\n\t\t\t(by default: Makefile)",
            "-md <description>": "Change the description for the makefile's description\n\t\t\t(by default: jitter jitter)",
            "-mgdb <0 or 1>": "Choose to input (1) or not (0) a ligne to compile with debugging options\n\t\t\t(by default: 0)",
            "-cf <0 or 1>": "Change if to add (1) or not (0) the csfml libraries required for graphical compilation with the csfml library.",
            "-o <no_space_name>": "Change the output name of the generated file after compilation\n\t\t\t(the default name is a.out)",
            "-ccsfml <0 or 1>": "Check (1) or not (0) for csfml function declarations.\n\t\t\t(by default: 0)",
            "-co": "Clean the object files during the compilation.",
            "-s": "Silence the makefile.",
            "-nm": "Do not generate a makefile.",
            "-nh": "Do not generate a headerfile.",
            "--json": "Load a json file for having a quick way of loading the settings"
        }
        # ----- Color management -----
        self.colourise_output = True
        self.wich_system = platform.system()
        # ----- Makefile management -----
        self.makefile_content = list()
        # self.gen_a_makefile = True
        # self.include_csfml_flags = 0
        # self.makefile_name = "Makefile"
        # self.silent_makefile = ""
        # self.clean_object_files = False
        # self.makefile_debug_line = False
        # self.makefile_binary_name = "a.out"
        # self.makefile_header_title = "Makefile"
        # self.check_for_csfml_declarations = False
        # self.makefile_header_description = "jitter jitter"
        self.rules_c = {
            "add_all": True,
            "add_clean": True,
            "add_fclean": True,
            "add_re": True,
            "add_update_deps": True,
            "add_debug": False,
            "add_test": False,
            "add_test_run": False,
            "add_test_coverage": False,
            "add_retest": False,
            "add_test_run_valgrind": False,
            "add_functional": False,
            "add_old_standards_c90": False,
            "add_epitech_standards_c99": False,
            "add_restandard": False,
            "add_re_old_standards": False,
            "add_c11_standard": False,
            "add_as_lib": False,
            "add_re_c11": False,
            "add_phony": True
        }
        self.rules_lib = {
            "add_all": True,
            "add_clean": True,
            "add_fclean": True,
            "add_re": True,
            "add_update_deps": True,
            "add_debug": False,
            "add_test": False,
            "add_test_run": False,
            "add_test_coverage": False,
            "add_retest": False,
            "add_test_run_valgrind": False,
            "add_functional": False,
            "add_old_standards_c90": False,
            "add_epitech_standards_c99": False,
            "add_c11_standard": False,
            "add_restandard": False,
            "add_re_old_standards": False,
            "add_re_c11": False,
            "add_update_archive": True,
            "add_update_includes": True,
            "add_update_dynamic_archive": False,
            "add_build_all_types": False,
            "add_rebuild_all_types": False,
            "add_phony": True
        }
        self.rules_cpp = {
            "add_all": True,
            "add_clean": True,
            "add_fclean": True,
            "add_re": True,
            "add_update_deps": True,
            "add_debug": False,
            "add_test": False,
            "add_test_run": False,
            "add_test_coverage": False,
            "add_retest": False,
            "add_test_run_valgrind": False,
            "add_functional": False,
            "add_old_standards_c90": False,
            "add_epitech_standards_c99": False,
            "add_restandard": False,
            "add_re_old_standards": False,
            "add_c11_standard": False,
            "add_as_lib": False,
            "add_re_c11": False,
            "add_phony": True
        }
        self.compiling_c = {
            "gen_makefile_c": True,
            "header_name": "Makefile",
            "header_description": "jitter jitter",
            "bin_name": "a.out",
            "keep_object_files": True,
            "silent_makefile": True,
            "includes": "-I./include/",
            "flags": "-Wall -Wextra -Werror -Wpedantic",
            "call_dynamic": False,
            "add_optimisation_flag": False,
            "optimisation_level": 3,
            "convert_warnings_to_errors": False,
            "compiler": "gcc",
            "delete_command": "rm -f",
            "make_command": "make -C",
            "copy_command": "cp -uf",
            "unit_flags": "--coverage -lcriterion",
            "unit_test_path": "./test/",
            "unit_test_file": "test_main.c",
            "unit_test_name": "unit_test",
            "add_csfml_flags": False
        }
        self.compiling_lib = {
            "gen_makefile_lib": False,
            "header_name": "Makefile",
            "header_description": "jitter jitter",
            "keep_object_files": True,
            "silent_makefile": True,
            "path": "./lib/",
            "includes": "-I../../include/",
            "header_file_name": "{header_file_name}.h",
            "result_name": "lib{fold_name}.a",
            "flags": "-Wall -Wextra -Werror -Wpedantic",
            "dynamic": False,
            "add_optimisation_flag": False,
            "optimisation_level": 3,
            "convert_warnings_to_errors": False,
            "compiler": "gcc",
            "delete_command": "rm -f",
            "make_command": "make -C",
            "copy_command": "cp -uf",
            "unit_flags": "--coverage -lcriterion",
            "unit_test_path": "./test/",
            "unit_test_file": "test_main.c",
            "unit_test_name": "unit_test",
            "add_csfml_flags": False
        }
        self.compiling_cpp = {
            "gen_makefile_cpp": False,
            "header_name": "Makefile",
            "header_description": "jitter jitter",
            "bin_name": "a.out",
            "keep_object_files": True,
            "silent_makefile": True,
            "includes": "-I./include/",
            "flags": "-Wall -Wextra -Werror -Wpedantic",
            "call_dynamic": False,
            "add_optimisation_flag": False,
            "optimisation_level": 3,
            "convert_warnings_to_errors": False,
            "compiler": "g++",
            "delete_command": "rm -f",
            "make_command": "make -C",
            "copy_command": "cp -uf",
            "unit_flags": "--coverage -lcriterion",
            "unit_test_path": "./test/",
            "unit_test_file": "test_main.c",
            "unit_test_name": "unit_test",
            "add_csfml_flags": False
        }
        # ----- Headerfile management -----
        self.headerfile_content = list()
        self.headerfile_options = {
            "gen_a_headerfile": True,
            "include_folder": "./",
            "headerfile_name": "root.h",
            "header_name": "Makefile",
            "header_description": "jitter jitter",
            "pragma_once": False,
            "include_guard": True
        }
        # self.include_folder = "./"
        # self.gen_a_headerfile = True
        # self.headerfile_name = "root.h"
        # self.headerfile_header_title = "header"
        # self.headerfile_header_description = "jitter jitter"
        # ----- miscellaneous -----
        self.argv = argv
        self.argc = len(argv)
        self.langage = "eng"
        self.author = f"{chr(169)} Henry Letellier"
        self.scan_path = "./"
        self.system = platform.system()
        self.c_date = datetime.now().year
        # ----- TTY info -----
        self.display_logo = True
        self.app_logo = [
            " /$$      /$$           /$$                   /$$                        ",
            "| $$$    /$$$          | $$                  | $$                        ",
            "| $$$$  /$$$$  /$$$$$$ | $$   /$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ ",
            "| $$ $$/$$ $$ |____  $$| $$  /$$/ |____  $$|_  $$_/   /$$__  $$ /$$__  $$",
            "| $$  $$$| $$  /$$$$$$$| $$$$$$/   /$$$$$$$  | $$    | $$  \\ $$| $$  \\__/",
            "| $$\\  $ | $$ /$$__  $$| $$_  $$  /$$__  $$  | $$ /$$| $$  | $$| $$      ",
            "| $$ \\/  | $$|  $$$$$$$| $$ \\  $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      ",
            "|__/     |__/ \\_______/|__/  \\__/ \\_______/   \\___/   \\______/ |__/      "
        ]
        self.boot_data = {
            "logo": self.app_logo,
            "prog_name": self.program_name,
            "author": self.author,
            "version": self.version
        }
        self.end_logo = [
            "  /$$$$$$                            /$$ /$$                          ",
            " /$$__  $$                          | $$| $$                          ",
            "| $$  \\__/  /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$  /$$   /$$  /$$$$$$ ",
            "| $$ /$$$$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$| $$  | $$ /$$__  $$",
            "| $$|_  $$| $$  \\ $$| $$  \\ $$| $$  | $$| $$  \ $$| $$  | $$| $$$$$$$$",
            "| $$  \\ $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$_____/",
            "|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$|  $$$$$$$",
            " \\______/  \\______/  \\______/  \\_______/|_______/  \\____  $$ \\_______/",
            "                                                   /$$  | $$          ",
            "                                                  |  $$$$$$/          ",
            "                                                   \\______/    "
        ]
        # ----- GUI info -----
        self.c_time = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
