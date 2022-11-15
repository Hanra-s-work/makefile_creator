##
## EPITECH PROJECT, 2021
## makefile_creator
## File description:
## run_me.py
##

__VERSION__ = "1"
__AUTHOR__ = "Henry Letellier"
__LICENSE__ = "UNLICENSED"
__DESCRIPTION__ = "This is a python script to compile python under any common computer system"

import os, platform, json
from sys import argv

class General:
    """ Basic functions for everybody """
    def __init__(self) -> None:
        pass
    
    def is_empty(self, string:str) -> bool:
        """ Check if a string is empty """
        if len(string) == 0:
            return True
        else:
            return False
    
    def is_only_blanks(self, string:str) -> bool:
        """ Check if a string is only blanks """
        for i in string:
            if i != " " or i != "\t":
                return False
        return True
    
    def which_extension_to_look_for(self, system:str=platform.system()) -> str:
        """ Check the system and return the extension """
        if system == "Windows":
            return ".exe"
        elif system == "Linux":
            return ""
        else:
            return ".dmg"

    def seperate_content_from_flag(self, string:str) -> list:
        """ Separate the content from the flag """
        content = ""
        flag = ""
        if "=" in string:
            string = string.split("=")
        elif "\t" in string:
            string = string.split("\t")
        elif " " in string:
            string = string.split(" ")
        else:
            pass
        if len(string) == 1:
            flag = string[0]
        elif len(string) == 2 and string[1] != "":
            flag = string[0]
            content = string[1]
        else:
            flag = string[0]

        return [flag, content]

    def element_in_list(self, element:str, flag_list:list) -> bool:
        """ Check if an element is in a list """
        if element in flag_list:
            return True
        return False

    def file_exists(self, filepath:str="") -> bool:
        """ Check if a file exists """
        if len(filepath) > 0:
            if os.path.exists(filepath) == True:
                if os.path.isfile(filepath) == True:
                    return True
                else:
                    return False
            else:
                return False
        return False

    def get_file_content(self, filepath:str, encoding:str="utf-8") -> dict[int, str]:
        """ Get the content of a file """
        result = {"status":True, "path":""}
        if self.file_exists(filepath) == True:
            file = open(filepath, "r", encoding=encoding)
            result["path"] = file.read()
            file.close()
            result["status"] = True
        else:
            result["path"] = ""
            result["status"] = False
        return result

class CompileProgram:
    """ The class in charge of compiling the code """
    def __init__(self, cwd:str=os.getcwd(), dest:str="../..", bin_name:str="makator", files:str="", icon_path:str="icon/cog.ico") -> None:
        """ The global variables of the class """
        self.cwd = cwd
        self.dest = dest
        self.bin_name = bin_name
        self.files = files
        self.icon = icon_path
        self.change_bin_name = False
        self.gi = General()
        self.system = platform.system()


    def already_has_an_extension(self, string:str) -> bool:
        """ Check if the string already has an extension """
        extension_type = self.gi.which_extension_to_look_for(self.system)
        if extension_type == "":
            return True
        elif string.find(extension_type) != -1:
            return True
        else:
            return False

    def get_bin_name(self) -> str:
        """ Compile the program """
        extension_type = self.gi.which_extension_to_look_for(self.system)
        if self.gi.is_empty(self.bin_name) == True or self.gi.is_only_blanks(self.bin_name) == True:
            if self.change_bin_name == True:
                found = 0
                while found == 0:
                    self.bin_name = input("Enter a name for the executable: ")
                    if self.gi.is_empty(self.bin_name) == False and self.gi.is_only_blanks(self.bin_name) == False:
                        if self.already_has_an_extension(self.bin_name) == False:
                            self.bin_name += extension_type
                        found = 1
                    else:
                        print("Please enter a name")
            else:
                self.bin_name = f"makator{extension_type}"
        else:
            if self.already_has_an_extension(self.bin_name) == False:
                self.bin_name += extension_type
        return self.bin_name
        
    def run_compilation(self, bin_name:str, files:list, icon_path:str="") -> None:
        """ Run the compilation """
        os.chdir(self.dest)
        if len(icon_path) == 0:
            os.system(f"python {files} -n {bin_name} --onefile")
        else:
            os.system(f"python {files} -n {bin_name} -i {icon_path} --onefile")
        os.chdir(self.cwd)
        print("Compilation done")
            
        

class UpdateFolders:
    """ Update the files in their respective folders """
    def __init__(self) -> None:
        self.a= ""
    def test(self) -> None:
        """ Test the program """
        print(self.a)

class Get:
    """ Get content following the arguments when required """
    def __init__(self) -> None:
        self.gi = General()
        self.keep_searching = -1

    def status_message(self, processed_flag:list[str,str]) -> dict[int, str]:
        """ generates the status message """
        result = dict()
        if len(processed_flag) >= 2:
            if processed_flag[1] != "":
                result["status"] = True
                result["path"] = processed_flag[1]
            else:
                result["status"] = False
                result["path"] = ""
        else:
            result["status"] = self.keep_searching
            result["path"] = ""
        return result
    
    def flag_content(self, to_find:list) -> dict[int, str]:
        """ Get the content of the flag """
        result = {"status":False, "path":""}
        for i, element in enumerate(argv):
            if self.gi.element_in_list(argv[i].lower(), to_find) == True:
                temp = self.gi.seperate_content_from_flag(element)
                result = self.status_message(temp)
                if result["status"] == True:
                    return result
                elif result["status"] == self.keep_searching:
                    pass
                else:
                    pass
        return result

    def json_content(self) -> dict[int, str]:
        """ Get the content of the json file """
        result = dict()
        to_find = ["--json", "-j", "json", "j", "--j", "-json", "/j", "/json", "/-json", "/-j", "/--json", "/--j"]
        result = self.flag_content(to_find)
        json_possible_content = ["{","}","[","]",":",",","\"","\'","\\","/","(",")"]
        if self.gi.element_in_list(result["path"], json_possible_content) == True:
            result["status"] = True
            try:
                result["path"] = json.load(result["path"])
            except json.decoder.JSONDecodeError:
                result["status"] = False
                result["path"] = ""
        else:
            if self.gi.file_exists(result["path"]) == True:
                result["status"] = True
                self.gi.
                try:
                    result["path"] = json.load(result["path"])
                except json.decoder.JSONDecodeError:
                    result["status"] = False
                    result["path"] = ""
        return result

    def icon_path(self) -> dict[int, str]:
        """ Get the icon path """
        result = {"status": False, "path": ""}
        to_find = [ "--icon", "-i", "icon", "i", "--i", "-icon", "/i", "/icon", "/-icon", "/-i", "/--icon", "/--i"]
        result = self.flag_content(to_find)
        return result
    
    def file_paths(self) -> dict[int, str]:
        """ Get the file paths """
        result = {"status": False, "path": ""}
        to_find = ["--file", "-f", "file", "f", "--f", "-file", "/f", "/file", "/-file", "/-f", "/--file", "/--f"]
        result = self.flag_content(to_find)
        return result
    
    def destination(self) -> dict[int, str]:
        """ Get the destination path """
        result = {"status": False, "path": ""}
        to_find = ["--dest", "-d", "dest", "d", "--d", "-dest", "/d", "/dest", "/-dest", "/-d", "/--dest", "/--d"]
        result = self.flag_content(to_find)
        return result
    
    def bin_name(self) -> dict[int, str]:
        """ Get the bin name """
        result = {"status": False, "path": ""}
        to_find = ["--bin", "-b", "bin", "b", "--b", "-bin", "/b", "/bin", "/-bin", "/-b", "/--bin", "/--b"]
        result = self.flag_content(to_find)
        return result


class Display:
    """ Display program related messages """
    def __init__(self) -> None:
        pass

    def help_info(self, argv:list) -> None:
        """ Display the help information """
        print("USAGE:")
        print(f"\t{argv[0]} [OPTIONS]")
        print("\nOPTIONS:")
        print("\t-j, --json\t\tUse a json file to pass information to the program")
        print("\t-h, --help\t\t\tDisplay this help message and exit")
        print("\t-v, --version\t\t\tDisplay the version of the program")
        print("\t-i, --icon\t\t\t\tSet the icon of the program")
        print("\t-f, --files\t\t\t\tReplace the default files by your own")
        print("\t-d, --destination\t\t\tSet the destination of the binary")
        print("\t-b, --bin-name,\n\t-e, --executable\n\t-o, --option\n\t\t\t\tChange the name of the executable")
    
    def version_info(self) -> None:
        """ Display the version information """
        print(f"Version: {__VERSION__}")

class Options:
    """ Get the launch options of the program """
    def __init__(self) -> None:
        self.argv = argv
        self.argc = len(argv)

    def is_json(self) -> bool:
        """ Check if the json file is used """
        if "--json" in self.argv or "-j" in self.argv or "json" in self.argv or "j" in self.argv or"--j" in self.argv or"-json" in self.argv or "/j" in self.argv or "/json" in self.argv or "/-json" in self.argv or "/--json" in self.argv or "/--j" in self.argv:
            return True
        else:
            return False

    def is_help(self):
        """ Check if the arguments contain the help option """
        if "--help" in self.argv or "-h" in self.argv or  "help" in self.argv or "h" in self.argv or"--h" in self.argv or"-help" in self.argv or "/?" in self.argv or "/h" in self.argv or "/help" in self.argv or "/-help" in self.argv or "/-h" in self.argv or "/--help" in self.argv or "/--h" in self.argv:
            Display().help_info(self.argv)
            return True
        else:
            return False
    
    def is_version(self):
        """ Check if the arguments contain the version option """
        if "--version" in self.argv or "-v" in self.argv or "version" in self.argv or "v" in self.argv or"--v" in self.argv or"-version" in self.argv or "/v" in self.argv or "/version" in self.argv or "/-version" in self.argv or "/-v" in self.argv or "/--version" in self.argv or "/--v" in self.argv:
            Display().version_info()
            return True
        else:
            return False

    def is_icon(self):
        """ Check if the arguments contain the icon option """
        if "--icon" in self.argv or "-i" in self.argv or "icon" in self.argv or "i" in self.argv or"--i" in self.argv or"-icon" in self.argv or "/i" in self.argv or "/icon" in self.argv or "/-icon" in self.argv or "/-i" in self.argv or "/--icon" in self.argv or "/--i" in self.argv:
            return True
        else:
            return False

    def is_files(self):
        """ Check if the arguments contain the files option """
        if "--files" in self.argv or "-f" in self.argv or "files" in self.argv or "f" in self.argv or"--f" in self.argv or"-files" in self.argv or "/f" in self.argv or "/files" in self.argv or "/-files" in self.argv or "/-f" in self.argv or "/--files" in self.argv or "/--f" in self.argv:
            return True
        else:
            return False

    def is_destination(self):
        """ Check if the arguments contain the destination option """
        if "--destination" in self.argv or "-d" in self.argv or "destination" in self.argv or "d" in self.argv or"--d" in self.argv or"-destination" in self.argv or "/d" in self.argv or "/destination" in self.argv or "/-destination" in self.argv or "/-d" in self.argv or "/--destination" in self.argv or "/--d" in self.argv:
            return True
        else:
            return False
    
    def is_bin_name(self):
        """ Check if the arguments contain the bin name option """
        if "--bin-name" in self.argv or "-b" in self.argv or "bin-name" in self.argv or "b" in self.argv or"--b" in self.argv or"-bin-name" in self.argv or "/b" in self.argv or "/bin-name" in self.argv or "/-bin-name" in self.argv or "/-b" in self.argv or "/--bin-name" in self.argv or "/--b" in self.argv:
            return True
        else:
            return False

class Main:
    def __init__(self) -> None:
        self.gni = General()
        self.ci = Compile_program(os.getcwd(), "../..", "makator", "", "icon/cog.ico")
        self.ui = UpdateFolders()
        self.gei = Get()
        self.di = Display()
        self.oi = Options()

    def main(self) -> None:
        """ Main function """
        if self.oi.is_help() == True or self.oi.is_version() == True:
            return 0
        elif self.oi.is_icon() == True:
            icon_path = self.gei.icon_path(argv)
            if icon_path["status"] == True:
                self.ci.icon_path = icon_path["path"]
        self.ci.run_compilation(self.ci.bin_name, self.ci.files, self.ci.icon_path)
        self.ui.test()
