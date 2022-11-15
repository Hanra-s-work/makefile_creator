##
## EPITECH PROJECT, 2021
## makefile_creator - get_data.py
## File description:
## jitter jitter
##

class get_file_data:
    """ get the data from the files"""
    def __init__(self, c_path, csfml_path):
        """ local globals """
        self.c_path = c_path
        self.csfml_path = csfml_path

    def remove_empty_slots(self, my_list):
        """ Remove empty slots from the list """
        temp = []
        for i in range(len(my_list)):
            if my_list[i] == '' or my_list[i] == ' ':
                continue
            else:
                temp.append(my_list[i])
        return temp

    def load_declarations(self, filepath):
        """ Return the content of the file in a list form"""
        file=open(filepath, "r", encoding="utf-8")
        content = file.read().split('\n')
        file.close()
        p_content = get_file_data.remove_empty_slots(self, content)
        return p_content

    def sub_main(self):
        """ The function controlling the class """
        csfml_declarations = get_file_data.load_declarations(self, self.csfml_path)
        c_declarations = get_file_data.load_declarations(self, self.c_path)
        return csfml_declarations, c_declarations
