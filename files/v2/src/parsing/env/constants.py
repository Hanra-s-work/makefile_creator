##
## EPITECH PROJECT, 2021
## skin_changer
## File description:
## constants.py
##

class Const:
    """ The class containing the constants of the env module """
    def __init__(self) -> None:
        self.ERR = 84
        self.ERROR = 84
        self.SUCCESS = 0
        self.ENV_FILE = ".env"
        self.JSON_CONFIG = "config.json"
        self.__Name__ = "env++"
        self.__Author__ = f"{chr(169)} Henry Letellier"
        self.__Version__ = "1.0.0"
        self.__Licence__ = f"""
This program is provided as if and without any warranty.
The Author, {self.__Author__}, cannot be held responsible for any damage occurring on your computer.
The only provided warranty, is that this program, if downloaded from its original creator, and if it has been untouched, will be garrantied to work.
Use at your own risk.
Feel free to edit this program.
Quoting the original author {self.__Author__} would be appreciated.
"""
        self.__env_usage__ = """
USING THE .env FILE:

The .env file, contains a series a variables that you do not
necessarily want everybody to see.

USING VARIABLES:

In the environement files that are run through this program
it is possible to call some system variables such as the
username (%username%) or the current working directory (%pwd%)

To use these variables, add a % on either side of the variable
you wish to call.

Some variables have been system parsed (I have recreated them
based on the systems pre-existent variables to allow cross
platform .env files.)

Example:
pwd does not exist under Windows, so I have recreated it and
made it work the exact same way it would work under a linux
based system.

USING .env VARIABLES WITHIN THE .env FILE:

It is also possible to call environement variables within the
environement file. To do so, define your variable on its own
line, then call it in another variable using this syntax:
'text_before{<environement_variable>}text_after'

COMMENTING A VARIABLE:

Add a '#' in front of a variable, for it to be ignored by the program.
"""
        self.__Description__ = f"""
OVERVIEW:

This module aims to func up the env processing by adding
the possibility to load system variables into
the environement file as well as defining environement
environement variables and calling them within
the environement file.

{self.__env_usage__}
"""
        self.__DESCRIPTION__ = self.__Description__
