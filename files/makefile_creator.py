#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## makefile creator - for PA and Leo
## File description:
## jitter jitter - created by (c) Henry Letellier
##

__VERSION__ = "1.0.0.0.0.0.0.0.0.0.0"
__AUTHOR__ = "Henry Letellier"
__NAME__ = "Makefile creator"
__LANG__ = "GB"

import os, sys, platform
from my_databases import databases as DB
from get import get_file_data
from datetime import datetime
from xdrlib import ConversionError

class root:
    """ The class containing the local globals """
    def __init__(self, name, lang, version, author, argc, argv):
        """ The local global variables """
        # ----- Color management -----
        self.color_pallet = {}
        self.colorise_output = True
        self.wich_system = platform.system()
        # ----- File management -----
        self.encoding = "utf-8"
        # ----- init vars -----
        self.filename = sys.argv[0]
        self.name = name
        # ----- Makefile management -----
        self.gen_a_makefile = True
        self.include_csfml_flags = 0
        self.makefile_name = "Makefile"
        self.silent_makefile = ""
        self.makefile_debug_line = False
        self.makefile_binary_name = "a.out"
        self.makefile_header_title = "Makefile"
        self.check_for_csfml_declarations = False
        self.makefile_header_description = "jitter jitter"
        # ----- Headerfile management -----
        self.include_folder = "./"
        self.gen_a_headerfile = True
        self.headerfile_name = "root.h"
        self.headerfile_header_title = "header"
        self.headerfile_header_description = "jitter jitter"
        # ----- miscellaneous -----
        self.argc = argc
        self.argv = argv
        self.langage = lang
        self.author = author
        self.scan_path = "./"
        self.version = version
        self.system = platform.system()
        self.c_date = datetime.now().year
        self.temp = []
        self.structs = []
        self.c_files_in_dirs = []
        self.header_functions = []

    def write_content(self, filename, content_list):
        """ Write content to a file """
        file_w = open(f"{filename}", "w", encoding=self.encoding)
        for i in range(len(content_list)):
            file_w.write(content_list[i])
        file_w.close()

    def dump_content(self, filename, content):
        """ Write content to a file without styling """
        file_c = open(f"{filename}", "w", encoding=self.encoding)
        file_c.write(f"{content}")
        file_c.close()

    def get_content(self, filepath):
        """ Get the content of a file """
        f=open(filepath, "r", encoding="utf-8")
        content = f.read()
        f.close()
        return content

class treat_header(root):
    """ This class contains the functions required to create and fill a headerfile """
    def compiling_all(self):
        """ Compile all the data gathered into a list and write it to a file """
        compiled = [f"/*\n** EPITECH PROJECT, {self.c_date}\n** {self.headerfile_header_title}\n** File description:\n** {self.headerfile_header_description}\n*/\n\n"]
        temp = ''
        for i in self.headerfile_name.upper():
            if i == ' ' or i == '.':
                temp+='_'
            else:
                temp+=i
        compiled.append(f"#ifndef {temp}_\n\t#define {temp}_\n")
        for i in range(len(self.structs)):
            compiled.append(f"{self.structs[i]}\n")
        compiled.append("\n")
        for i in range(len(self.header_functions)):
            compiled.append(self.header_functions[i])
        compiled.append("\n#endif\n")
        root.write_content(self, f"include/{self.headerfile_name}", compiled)

    def is_in_list(self, sentence, list_to_check):
        """ Check if a word is in a given list """
        for c in range(len(list_to_check)):
            if list_to_check[c] in sentence and '\t' not in sentence and '    ' not in sentence:
                return True
        return False

    def process_c_file(self, filecontent, csfml_declaration, c_declaration):
        """ extract the functions from a string """
        lines = filecontent.split('\n')
        for i in range(len(lines)):
            if self.check_for_csfml_declarations == True:
                if treat_header.is_in_list(self, lines[i], csfml_declaration) == True:
                    if ";" not in lines[i]:
                        self.header_functions.append(f"{lines[i]};\n")
                    else:
                        self.header_functions.append(f"{lines[i]}\n")
            if treat_header.is_in_list(self, lines[i], c_declaration) == True:
                if ";" not in lines[i]:
                    self.header_functions.append(f"{lines[i]};\n")
                else:
                    self.header_functions.append(f"{lines[i]}\n")

    def get_functions_for_the_header(self, csfml_declaration, c_declaration):
        """ get the functions in files for the header """
        treat_header.check_if_include_folder_exists(self)
        for i in range(len(self.c_files_in_dirs)):
            content = root.get_content(self, self.c_files_in_dirs[i])
            treat_header.process_c_file(self, content, csfml_declaration, c_declaration)
        treat_header.compiling_all(self)

    def check_if_include_folder_exists(self):
        """ Check if in the specified directory the include folder exists """
        if (os.path.exists(f"{self.include_folder}/include") == False):
            os.mkdir(f"{self.include_folder}/include")

class treat_makefile(root):
    """ This class contains the functions required to create and fill a makefile """
    def get_files_for_makefile(self):
        """ get the files in the directory """
        self.c_files_in_dirs = []
        folders = []
        folders = get_folders(self.scan_path, folders)
        for i in range(len(folders)):
            content = os.listdir(folders[i])
            for b in range(len(content)):
                temp = content[b].lower().split('.')
                if ("c" == temp[len(temp)-1] and os.path.isdir(f"{folders[i]}/{content[b]}") == False):
                    self.c_files_in_dirs.append(f"{folders[i]}/{content[b]}")

    def create_makefile(self):
        """ generate the content and write it to the makefile """
        treat_makefile.get_files_for_makefile(self)
        makefile_content = [f"##\n## EPITECH PROJECT, {self.c_date}\n## {self.makefile_header_title}\n## File description:\n## {self.makefile_header_description}\n##\n\n"]
        SRC_used = False
        for i in range(len(self.c_files_in_dirs)):
            if (SRC_used == False):
                makefile_content.append(f"SRC\t=\t{self.c_files_in_dirs[i]}\t\\\n")
                SRC_used = True
            elif i == len(self.c_files_in_dirs)-1:
                makefile_content.append(f"\t\t{self.c_files_in_dirs[i]}\n\n")
            else:
                makefile_content.append(f"\t\t{self.c_files_in_dirs[i]}\t\\\n")
        makefile_content.append("OBJ\t=\t$(SRC:.c=.o)\n\n")
        makefile_content.append("REM\t=\t*.gcno\t\\\n\t\t*.gcda\n\n")
        makefile_content.append("CC\t=\tgcc\n\n")
        makefile_content.append("CFLAGS\t=\t-Wall -Wextra\n\n")
        makefile_content.append("CPPFLAGS\t=\t-I./include\n\n")
        if (self.makefile_debug_line == True):
            makefile_content.append("CPPPFLAGS\t=\t-Wall -Wextra -g3\n\n")
        if (self.include_csfml_flags == 1) :
            makefile_content.append("CSFMLFLAGS\t=\t-lcsfml-graphics -lcsfml-audio -lcsfml-system -lcsfml-window\n\n")
        makefile_content.append(f"NAME\t=\t{self.makefile_binary_name}\n\n")
        makefile_content.append("all:\t$(NAME)\n\n")
        if (self.include_csfml_flags == 1):
            makefile_content.append(f"$(NAME):\t$(OBJ)\n\t{self.silent_makefile}gcc -o $(NAME) $(OBJ) $(CFLAGS) $(CPPFLAGS) $(CSFMLFLAGS)\n")
        else:
            makefile_content.append(f"$(NAME):\t$(OBJ)\n\t{self.silent_makefile}gcc -o $(NAME) $(OBJ) $(CFLAGS) $(CPPFLAGS)\n")
        makefile_content.append(f"\t{self.silent_makefile}make clean\n\n")
        if (self.makefile_debug_line == True):
            makefile_content.append(f"debug:\n\t$(CC) $(CPPPFLAGS) -o $(NAME) $(SRC)\n\t{self.silent_makefile}make clean\n\n")
        makefile_content.append(f"clean:\n\t{self.silent_makefile}rm -f $(OBJ)\n\n")
        makefile_content.append(f"fclean: clean\n\t{self.silent_makefile}rm -f $(NAME)\n\t{self.silent_makefile}rm unit_tests\n\n")
        makefile_content.append("re: fclean all clean\n\n")
        makefile_content.append(".PHONY: fclean all clean re\n\n")
        root.write_content(self, self.makefile_name, makefile_content)

class get_launch_arguments(root):
    """ a class in charge of treating the input arguments """
    def has_help(self):
        """ check if the help symbols are in the call """
        for i in range(self.argc):
            if ("-h" in self.argv[i].lower() or "-help" in self.argv[i].lower() or "--help" in self.argv[i].lower() or "\\?" in self.argv[i].lower() or "/?" in self.argv[i].lower() or "///?" in self.argv[i].lower() or "-?" in self.argv[i].lower() or "?" in self.argv[i].lower()):
                print("HELP SECTION:")
                print(f"USAGE:\n\t-\t{self.filename}\tRun the generator (the default name will be Makefile")
                print(f"\t-\t{self.filename} -h (or --help)\t Display this help section")
                print(f"\t-\t{self.filename} -mo <new_name>\tChange the default output name (Makefile)")
                print(f"\t-\t{self.filename} -nc\tRun this program without colors")
                print(f"\t-\t{self.filename} -oh <new_name>\tSpecify the name of the header file")
                print(f"\t-\t{self.filename} -p <path>\tChange the directory in wich the program starts scanning\n\t\t\t(The default path is the directory in wich the program is running)")
                print(f"\t-\t{self.filename} -hf <path>\tChange the directory in wich the include folder is \n\t\t\t(if the include folder it not existent it will be created)")
                print(f"\t-\t{self.filename} -ht <title>\tChange the title for the header file's header\n\t\t\t(by default: header)")
                print(f"\t-\t{self.filename} -hd <description>\tChange the description for the header file's description\n\t\t\t(by default: jitter jitter)")
                print(f"\t-\t{self.filename} -mt <title>\tChange the title for the makefile header\n\t\t\t(by default: Makefile)")
                print(f"\t-\t{self.filename} -md <description>\tChange the description for the makefile's description\n\t\t\t(by default: jitter jitter)")
                print(f"\t-\t{self.filename} -mgdb <0 or 1>\tChoose to input (1) or not (0) a ligne to compile with debugging options\n\t\t\t(by default: 0)")
                print(f"\t-\t{self.filename} -cf <0 or 1>\tChange if to add (1) or not (0) the csfml libraries required for graphical compilation with the csfml library.")
                print(f"\t-\t{self.filename} -o <no_space_name>\tChange the output name of the generated file after compilation\n\t\t\t(the default name is a.out)")
                print(f"\t-\t{self.filename} -ccsfml <0 or 1>\tCheck (1) or not (0) for csfml function declarations.\n\t\t\t(by default: 0)")
                print(f"\t-\t{self.filename} -s \tSilence the makefile.")
                print(f"\t-\t{self.filename} -nm\tDo not generate a makefile.")
                print(f"\t-\t{self.filename} -nh\tDo not generate a headerfile.")

                return True
        return False

    def has_no_color(self):
        """ check if the no color option is in the call """
        for i in range(self.argc):
            if ("-nc" in self.argv[i].lower() == True):
                self.colorise_output = False
                return True
        return False

    def new_output(self):
        """ Check if the new output is in the call """
        for i in range(self.argc):
            if (("-mo" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    self.makefile_name = self.argv[i+1]

    def has_oh(self):
        """ Check if the header rename output is in the call """
        for i in range(self.argc):
            if (("-oh" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    self.headerfile_name = self.argv[i+1]

    def change_path(self):
        """ Check if the starting directory will change """
        for i in range(self.argc):
            if (("-p" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    self.scan_path = self.argv[i+1]

    def check_include_path(self):
        """ Check if the path for the include folder will change """
        for i in range(self.argc):
            if (("-hf" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    self.include_folder = self.argv[i+1]

    def get_makefile_header_title(self):
        """ Check and get if the title of the header of the makefile has changed """
        for i in range(self.argc):
            if (("-ht" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    self.makefile_header_title = self.argv[i+1]

    def get_makefile_header_description(self):
        """ Check and get if the description of hte header of the makefile has changed """
        for i in range(self.argc):
            if (("-hd" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    self.makefile_header_description = self.argv[i+1]

    def get_header_file_header_title(self):
        """ Check and get if the title of the header of the header file has changed """
        for i in range(self.argc):
            if (("-mt" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    self.headerfile_header_title = self.argv[i+1]


    def get_header_file_header_description(self):
        """ Check and get if the description of the header of the headerfile has changed """
        for i in range(self.argc):
            if (("-md" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    self.headerfile_header_description = self.argv[i+1]


    def check_if_to_include_csfml_flags(self):
        """ Get the status of the csfml flags """
        for i in range(self.argc):
            if (("-cf" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    try:
                        self.headerfile_header_description = int(self.argv[i+1])
                    except ConversionError :
                        print("Failed to get the info for the csfml flags, they will thus, not be put into the makefile.")

    def makefile_bin_name(self):
        """ Get the binary output name if given """
        for i in range(self.argc):
            if (("-o" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    self.makefile_binary_name = f"\"{self.argv[i+1]}\""

    def check_makefile_debug_line(self):
        """ Get the status on if to put or not the debug line """
        for i in range(self.argc):
            if (("-mgdb" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    try:
                        self.makefile_debug_line = int(self.argv[i+1])
                    except ConversionError :
                        print("Failed to get the info for the debug line, it will thus, not be put into the makefile.")

    def check_for_csfml(self):
        """ Get the status on if to check for csfml functions or not """
        for i in range(self.argc):
            if (("-ccsfml" == self.argv[i].lower()) and (i+1 <= self.argc-1)):
                if (self.argv[i+1][0] != '-'):
                    try:
                        self.check_for_csfml_declarations = int(self.argv[i+1])
                    except ConversionError :
                        print("Failed to get the info csfml calls, it will thus, not be taken into account.")

    def create_makefile(self):
        """ Get if to create a makefile """
        for i in range(self.argc):
            if ("-nm" == self.argv[i].lower()):
                self.gen_a_makefile = False

    def create_headerfile(self):
        """ Get if to create a headerfile """
        for i in range(self.argc):
            if ("-nh" == self.argv[i].lower()):
                self.gen_a_headerfile = False

    def silence_the_makefile(self):
        """ Get if to create a headerfile """
        for i in range(self.argc):
            if ("-s" == self.argv[i].lower()):
                self.silent_makefile = "@"

class color(root):
    def display(self, color):
        if (self.colorise_output == True):
            if (self.wich_system == "Windows"):
                os.system(f"{self.color_pallet[color]}")
            else:
                os.system(f"echo -e \"{self.color_pallet[color]}\"")

    def init_pallet(self):
        if (self.wich_system != "Windows") :
            color_list = ["0 = 30","1 = 34","2 = 32","3 = 36","4 = 31","5 = 35","6 = 33","7 = 37","8 = 90","9 = 94","a = 92","b = 96","c = 91","d = 95","e = 93","f = 97","0"]
            color_list = ["30","34","32","36","31","35","33","37","90","94","92","96","91","95","93","97","0"]
            g=h=0
            for i in "0123456789ABCDEFr":
                h=0
                for b in "0123456789ABCDEFr":
                    self.color_pallet[f"{i}{b}"]=f"\\e[{color_list[g]}m\\e[{int(color_list[h])+10}m"
                    h+=1
                g+=1
        else:
            for i in "0123456789ABCDEFr":
                for b in "0123456789ABCDEFr":
                    if (i == 'r'):
                        if (b == 'r'):
                            self.color_pallet[f"{i}{b}"] = f"color 0A"
                        else:
                            self.color_pallet[f"{i}{b}"] = f"color 0{b}"
                    elif (b == 'r'):
                        self.color_pallet[f"{i}{b}"] = f"color {i}A"
                    else:
                        self.color_pallet[f"{i}{b}"] = f"color {i}{b}"


RI = root(__NAME__,__LANG__,__VERSION__,__AUTHOR__,len(sys.argv),sys.argv)
PI = get_file_data("declarations/c.mc", "declarations/csfml.mc")

def get_folders(scan_dir, dir_list):
    """ recursively list all the directory's and sub directory's of the specified path """
    for file in os.listdir(scan_dir):
        d = os.path.join(scan_dir, file)
        if os.path.isdir(d):
            dir_list.append(d)
            get_folders(d, dir_list)
    return dir_list

def check_inputs(self):
    """ check the possible inputs at call of the program """
    if (get_launch_arguments.has_help(self) is True):
        return True
    if (get_launch_arguments.has_no_color(self) is False):
        color.init_pallet(self)
    get_launch_arguments.has_oh(self)
    get_launch_arguments.new_output(self)
    get_launch_arguments.change_path(self)
    get_launch_arguments.check_for_csfml(self)
    get_launch_arguments.create_makefile(self)
    get_launch_arguments.makefile_bin_name(self)
    get_launch_arguments.create_headerfile(self)
    get_launch_arguments.check_include_path(self)
    get_launch_arguments.silence_the_makefile(self)
    get_launch_arguments.get_makefile_header_title(self)
    get_launch_arguments.check_makefile_debug_line(self)
    get_launch_arguments.get_header_file_header_title(self)
    get_launch_arguments.get_makefile_header_description(self)
    get_launch_arguments.check_if_to_include_csfml_flags(self)
    get_launch_arguments.get_header_file_header_description(self)
    return False

def main():
    # print(RI.argv)
    if (RI.argc > 1):
        if (check_inputs(RI) == True):
            return True
    # color.display(RI, "0A")
    try:
        result = get_file_data.sub_main(PI)
        csfml_declaration = result[0]
        c_declaration = result[1]
    except:
        DI = DB()
        csfml_declaration = DI.csfml_declaration
        c_declaration = DI.c_declaration
    # root.dump_content(RI, "my_databases.py", f"#!/usr/bin/env python3\n##\n## EPITECH PROJECT, 2022\n## makefile creator - for PA and Leo\n## File description:\n## jitter jitter - created by (c) Henry Letellier\n##\n\nclass databases:\n    \"\"\" The class in charge of storing the lists \"\"\"\n    def __init__(self):\n        \"\"\" The variables for the csfml database \"\"\"\n        self.csfml_declaration = {csfml_declaration}\n        self.c_declaration = {c_declaration}\n")
    if (RI.gen_a_makefile == True):
        treat_makefile.create_makefile(RI)
    if (RI.gen_a_headerfile == True):
        treat_header.get_functions_for_the_header(RI, csfml_declaration, c_declaration)
    print("Done.")
    print("Program (c) Created by Henry Letellier")
    # color.display(RI, "rr")

main()
