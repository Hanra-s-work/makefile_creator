##
# EPITECH PROJECT, 2022
# v2
# File description:
# __init__.py
##

from .add import Add
from .get import Get
from .gui import GUI
from .set import Set
from .build import Build
from .rules import Rules
from .write import Write
from .parsing import Parsing
from .global_vars import GlobalVars


class Src(Write, GlobalVars):
    """The main sub class of the program"""

    def __init__(self, argv: list[str], json_file: str) -> None:
        super().__init__()
        self.parsing = Parsing
        self.add = Add()
        self.build = Build()
        self.gui = GUI().gui
        self.build = Build()
        self.get = Get()
        self.rules = Rules()
        self.set = Set()
        self.write = Write()
        self.global_vars = GlobalVars(json_file)
        self.gv = self.global_vars
        self.data_src = "eee"
        self.argv = argv
        self.argc = len(argv)

    def test_src(self) -> str:
        """Test the class Src of the program"""
        print(f"Add = {dir(self.add)}")
        print(f"Build = {dir(self.build)}")
        print(f"Get = {dir(self.get)}")
        print(f"GUI = {dir(self.gui)}")
        print(f"Rules = {dir(self.rules)}")
        print(f"Set = {dir(self.set)}")
        print(f"Write = {dir(self.write)}")
        print(f"GlobalVars = {dir(self.gv)}")
        return "test class src"

    def check_options(self) -> None:
        """The function in charge of checking the options passed"""
        if (self.has_help() is False and self.has_version() is False and self.has_author() is False):
            self.has_json()
            self.has_oh()
            self.no_logo()
            self.new_output()
            self.change_path()
            self.has_no_color()
            self.must_show_debug()
            self.create_makefile()
            self.check_for_csfml()
            self.create_headerfile()
            self.makefile_bin_name()
            self.check_include_path()
            self.silence_the_makefile()
            self.get_header_file_name()
            self.specify_makefile_type()
            self.get_makefile_header_title()
            self.check_makefile_debug_line()
            self.check_makefile_include_path()
            self.get_header_file_header_title()
            self.get_makefile_header_description()
            self.check_if_to_include_csfml_flags()
            self.get_header_file_header_description()
            self.clean_object_files_for_the_makefile()

    def has_help(self) -> bool:
        """check if the help symbols are in the call"""
        for i in range(self.argc):
            if ("-h" in self.argv[i].lower() or "-help" in self.argv[i].lower() or "--help" in self.argv[i].lower() or "\\?" in self.argv[i].lower() or "/?" in self.argv[i].lower() or "///?" in self.argv[i].lower() or "-?" in self.argv[i].lower() or "?" in self.argv[i].lower()):
                self.gui.disp.display_help(self.argv[0], self.gv.help)
                return True
        return False

    def has_version(self) -> bool:
        """Check if the version symbols are in the call"""
        for i in range(self.argc):
            if ("-v" in self.argv[i].lower() or "-version" in self.argv[i].lower() or "--version" in self.argv[i].lower()):
                self.gui.disp.display_version(self.gv.version)
                return True
        return False

    def has_author(self) -> bool:
        """Check if the author symbols are in the call"""
        for i in range(self.argc):
            if ("-a" in self.argv[i].lower() or "-author" in self.argv[i].lower() or "--author" in self.argv[i].lower()):
                self.gui.disp.display_author(self.gv.author)
                return True
        return False

    def has_no_color(self) -> bool:
        """check if the no color option is in the call"""
        for i in range(self.argc):
            if "-nc" in self.argv[i].lower() == True:
                self.gv.colourise_output = False
                return True
        return False

    def new_output(self) -> bool:
        """Check if the new output is in the call"""
        for i in range(self.argc):
            if ("-mo" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.compiling_c["bin_name"] = self.argv[i + 1]
                    self.gv.compiling_cpp["bin_name"] = self.argv[i + 1]
                    return True
        return False

    def has_oh(self) -> bool:
        """Check if the header rename output is in the call"""
        for i in range(self.argc):
            if ("-oh" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.headerfile_options["headerfile_name"] = self.argv[i + 1]
                    return True
        return False

    def change_path(self) -> bool:
        """Check if the starting directory will change"""
        for i in range(self.argc):
            if ("-p" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.scan_path = self.argv[i + 1]
                    return True
        return False

    def check_include_path(self) -> bool:
        """Check if the path for the include folder will change"""
        for i in range(self.argc):
            if ("-hi" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.headerfile_options["include_folder"] = self.argv[i + 1]
                    return True
        return False

    def check_makefile_include_path(self) -> bool:
        """Check if the path for the include folder will change"""
        for i in range(self.argc):
            if ("-mi" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.compiling_c["includes"] = self.argv[i + 1]
                    self.gv.compiling_lib["includes"] = self.argv[i + 1]
                    self.gv.compiling_cpp["includes"] = self.argv[i + 1]
                    return True
        return False

    def get_makefile_header_title(self) -> bool:
        """Check and get if the title of the header of the makefile has changed"""
        for i in range(self.argc):
            if ("-mt" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.compiling_c["header_name"] = self.argv[i + 1]
                    self.gv.compiling_lib["header_name"] = self.argv[i + 1]
                    self.gv.compiling_cpp["header_name"] = self.argv[i + 1]
                    return True
        return False

    def get_makefile_header_description(self) -> bool:
        """Check and get if the description of hte header of the makefile has changed"""
        for i in range(self.argc):
            if ("-md" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.compiling_c["header_description"] = self.argv[i + 1]
                    self.gv.compiling_lib["header_description"] = self.argv[i + 1]
                    self.gv.compiling_cpp["header_description"] = self.argv[i + 1]
                    return True
        return False

    def get_header_file_name(self) -> bool:
        """Check and get if the title of the header of the header file has changed"""
        for i in range(self.argc):
            if ("-hn" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.headerfile_options["headerfile_name"] = self.argv[i + 1]
                    return True
        return False

    def get_header_file_header_title(self) -> bool:
        """Check and get if the title of the header of the header file has changed"""
        for i in range(self.argc):
            if ("-ht" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.headerfile_options["header_name"] = self.argv[i + 1]
                    return True
        return False

    def get_header_file_header_description(self):
        """Check and get if the description of the header of the headerfile has changed"""
        for i in range(self.argc):
            if ("-hd" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.headerfile_options["header_description"] = self.argv[i + 1]
                    return True
        return False

    def check_if_to_include_csfml_flags(self) -> bool:
        """Get the status of the csfml flags"""
        for i in range(self.argc):
            if ("-cf" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    try:
                        self.gv.compiling_c["add_csfml_flags"] = bool(int(self.argv[i + 1]))
                        self.gv.compiling_lib["add_csfml_flags"] = bool(int(self.argv[i + 1]))
                        self.gv.compiling_cpp["add_csfml_flags"] = bool(int(self.argv[i + 1]))
                        return True
                    finally:
                        print("Failed to get the info for the csfml flags, they will thus, not be put into the makefile.")
        return False

    def makefile_bin_name(self) -> bool:
        """Get the binary output name if given"""
        for i in range(self.argc):
            if ("-o" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    self.gv.compiling_c["bin_name"] = f'"{self.argv[i+1]}"'
                    self.gv.compiling_lib["bin_name"] = f'"{self.argv[i+1]}"'
                    self.gv.compiling_cpp["bin_name"] = f'"{self.argv[i+1]}"'
                    return True
        return False

    def check_makefile_debug_line(self):
        """Get the status on if to put or not the debug line"""
        for i in range(self.argc):
            if ("-mgdb" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    try:
                        self.gv.compiling_c["add_debug"] = bool(int(self.argv[i + 1]))
                        self.gv.compiling_lib["add_debug"] = bool(int(self.argv[i + 1]))
                        self.gv.compiling_cpp["add_debug"] = bool(int(self.argv[i + 1]))
                        return True
                    finally:
                        print("Failed to get the info for the debug line, it will thus, not be put into the makefile.")
        return False

    def check_for_csfml(self):
        """Get the status on if to check for csfml functions or not"""
        for i in range(self.argc):
            if ("-ccsfml"
                    == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    try:
                        self.gv.compiling_c["add_csfml_flags"] = bool(int(self.argv[i + 1]))
                        self.gv.compiling_lib["add_csfml_flags"] = bool(int(self.argv[i + 1]))
                        self.gv.compiling_cpp["add_csfml_flags"] = bool(int(self.argv[i + 1]))
                        return True
                    finally:
                        print("Failed to get the info csfml calls, it will thus, not be taken into account.")
        return False

    def create_makefile(self):
        """Get if to create a makefile"""
        for i in range(self.argc):
            if "-nm" == self.argv[i].lower():
                self.gv.compiling_c["gen_makefile_c"] = False
                self.gv.compiling_lib["gen_makefile_lib"] = False
                self.gv.compiling_cpp["gen_makefile_cpp"] = False
                return True
        return False

    def specify_makefile_type(self) -> bool:
        """Check the specifics of the makefile"""
        for i in range(self.argc):
            if ("-t" == self.argv[i].lower() or "--t" == self.argv[i].lower() or "--type" == self.argv[i].lower() or "-type" == self.argv[i].lower()) and (i + 1 <= self.argc - 1):
                if self.argv[i + 1][0] != "-":
                    try:
                        arg_type = self.argv[i + 1].lower()
                        if arg_type == "c":
                            self.gv.compiling_c["gen_makefile_c"] = True
                            self.gv.compiling_lib["gen_makefile_lib"] = False
                            self.gv.compiling_cpp["gen_makefile_cpp"] = False
                        elif arg_type == "lib":
                            self.gv.compiling_c["gen_makefile_c"] = True
                            self.gv.compiling_lib["gen_makefile_lib"] = False
                            self.gv.compiling_cpp["gen_makefile_cpp"] = False
                        elif arg_type == "cpp" or arg_type == "c++":
                            self.gv.compiling_c["gen_makefile_c"] = True
                            self.gv.compiling_lib["gen_makefile_lib"] = False
                            self.gv.compiling_cpp["gen_makefile_cpp"] = False
                        return True
                    finally:
                        print("Failed to get the info for the makefile type, it will thus, be set to the default.")
        return False

    def create_headerfile(self):
        """Get if to create a headerfile"""
        for i in range(self.argc):
            if "-nh" == self.argv[i].lower():
                self.gv.headerfile_options["gen_a_headerfile"] = False
                return True
        return False

    def silence_the_makefile(self):
        """Get if to create a headerfile"""
        for i in range(self.argc):
            if "-s" == self.argv[i].lower():
                self.gv.compiling_c["silent_makefile"] = True
                self.gv.compiling_lib["silent_makefile"] = True
                self.gv.compiling_cpp["silent_makefile"] = True
                return True
        return False

    def clean_object_files_for_the_makefile(self):
        """Get if to create a headerfile"""
        for i in range(self.argc):
            if "-co" == self.argv[i].lower():
                self.gv.compiling_c["keep_object_files"] = False
                self.gv.compiling_lib["keep_object_files"] = False
                self.gv.compiling_cpp["keep_object_files"] = False
                return True
        return False

    def has_json(self) -> bool:
        """Check if a json file is provided"""
        for i in range(self.argc):
            if ((("-j" == self.argv[i].lower()) and (i + 1 <= self.argc - 1)) or (("--j" == self.argv[i].lower()) and (i + 1 <= self.argc - 1)) or (("--json" == self.argv[i].lower()) and (i + 1 <= self.argc - 1)) or (("-json" == self.argv[i].lower()) and (i + 1 <= self.argc - 1))):
                if self.argv[i + 1][0] != "-":
                    self.gv.json_file = self.argv[i + 1]
                    self.load_json(self.json_file)
                    return True
        return False

    def no_logo(self) -> bool:
        """ Check if the logo should be displayed or not """
        for i in range(self.argc):
            if "-nl" == self.argv[i].lower():
                self.gv.display_logo = False
                return True
        return False

    def must_show_debug(self) -> bool:
        """ Check if the debug should be displayed or not """
        for i in range(self.argc):
            if "-sd" == self.argv[i].lower():
                self.gv.show_debug = True
                return True
        return False

    def load_json(self, json: str) -> None:
        """The function in charge of loading the json file"""
        json_class = self.parsing().json_parsing(json)
        json_class.start_parsing()
        self.gv.json_content = json_class.json_content
        for i in self.gv.json_content:
            if "rule_options" == i:
                for j in self.gv.json_content[i]:
                    if "c" == j:
                        self.gv.rules_c = json_class.update_json(self.gv.json_content[i][j], self.gv.rules_c, i, j)
                    if "lib" == j:
                        self.gv.rules_lib = json_class.update_json(self.gv.json_content[i][j], self.gv.rules_lib, i, j)
                    if "cpp" == j:
                        self.gv.rules_cpp = json_class.update_json(self.gv.json_content[i][j], self.gv.rules_cpp, i, j)
            if "compiling_options" == i:
                for j in self.json_content[i]:
                    if "c" == j:
                        self.gv.compiling_c = json_class.update_json(
                            self.gv.json_content[i][j], self.gv.compiling_c, i, j)
                    if "lib" == j:
                        self.gv.compiling_lib = json_class.update_json(
                            self.gv.json_content[i][j], self.gv.compiling_lib, i, j)
                    if "cpp" == j:
                        self.gv.compiling_cpp = json_class.update_json(
                            self.gv.json_content[i][j], self.gv.compiling_cpp, i, j)
