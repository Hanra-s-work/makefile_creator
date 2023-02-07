##
## EPITECH PROJECT, 2022
## Desktop_pet (Workspace)
## File description:
## colourise_output.py
##

"""
The file containing the code in charge of outputting
coloured text into the terminal.
"""

import os
import platform
import colorama as COC

class ColouriseOutput:
    """ The class in charge of adding colour to text """
    def __init__(self) -> None:
        self.author = "Henry Letellier"
        self.colour_pallet = {}
        self.unix_colour_pallet = dict()
        self.colourise_output = True
        self.wich_system = platform.system()

    def process_attributes(self, attributes:tuple=()) -> list:
        """ Convert the inputted tuple to a list containing the options """
        finall_attributes = ""
        attributes_length = len(attributes)
        if attributes_length > 0 and attributes[0] == True:
            finall_attributes+="\033[01m" #bold
        # if attributes_length > 1 and attributes[1] == True:
        #     finall_attributes.append("dark")
        if attributes_length > 2 and attributes[2] == True:
            finall_attributes+="\033[04m" #underline
        if attributes_length > 3 and attributes[3] == True:
            finall_attributes+="\033[05m" #blink
        # if attributes_length > 4 and attributes[4] == True:
            # finall_attributes.append("reverse")
        # if attributes_length > 5 and attributes[5] == True:
            # finall_attributes.append("concealed")
        return finall_attributes

    def display(self, colour:str, attributes:tuple=(), text:str="") -> None:
        """ Depending on the system, change the command used to output colour """
        processed_attributes = self.process_attributes(attributes)
        if (self.colourise_output == True):
            try:
                print(f"{self.unix_colour_pallet[colour]}{processed_attributes}{text}", end="")
            except IOError:
                if (self.wich_system == "Windows"):
                    os.system(f"{self.colour_pallet[colour]}")
                    if len(text) > 0:
                        print(f"{text}", end="")
                else:
                    os.system(f"echo -e \"{self.colour_pallet[colour]}{processed_attributes}{text}\"")

    def load_for_windows(self) -> None:
        """ Prepare the Windows colour pallet """
        for i in "0123456789ABCDEFr":
            for b in "0123456789ABCDEFr":
                if (i == 'r'):
                    if (b == 'r'):
                        self.colour_pallet[f"{i}{b}"] = "color 0A"
                    else:
                        self.colour_pallet[f"{i}{b}"] = f"color 0{b}"
                elif (b == 'r'):
                    self.colour_pallet[f"{i}{b}"] = f"color {i}A"
                else:
                    self.colour_pallet[f"{i}{b}"] = f"color {i}{b}"

    def load_for_non_windows(self) -> None:
        """ Prepare the non Windows colour pallet """
        color_list = ["0 = 30","1 = 34","2 = 32","3 = 36","4 = 31","5 = 35","6 = 33","7 = 37","8 = 90","9 = 94","a = 92","b = 96","c = 91","d = 95","e = 93","f = 97","0"]
        color_list = ["30","34","32","36","31","35","33","37","90","94","92","96","91","95","93","97","0"]
        g=h=0
        for foregound in "0123456789ABCDEFr":
            h=0
            for background in "0123456789ABCDEFr":
                self.colour_pallet[f"{background}{foregound}"]=f"\\e[{int(color_list[h])+10}m\\e[{color_list[g]}m"
                self.unix_colour_pallet[f"{background}{foregound}"]=f"\033[{int(color_list[h])+10}m\033[{color_list[g]}m"
                h+=1
            g+=1

    def init_pallet(self) -> None:
        """ Prepare and load an intersystem pallet based on the Windows colour format """
        COC.reinit()
        self.load_for_non_windows()
        if (self.wich_system == "Windows") :
            self.load_for_windows()

    def unload_ressources(self) -> None:
        """ Free the ressources that can be freed """
        COC.deinit()

    def test_colours(self) -> None:
        """ Display all the available colours and their code """
        print("Displaying all available colours:")
        for i in self.unix_colour_pallet:
            self.display("rr", (), "\n")
            self.display(i, (), f"Current colour: '{i}'")
        self.display("rr", (), f"{len(self.unix_colour_pallet)} Colours displayed.\n")

if __name__ == '__main__':
    CI = ColouriseOutput()
    CI.init_pallet()
    CI.test_colours()
    CI.unload_ressources()
    print(f"Created by {CI.author}")
