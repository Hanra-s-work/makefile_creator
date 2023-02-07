##
## EPITECH PROJECT, 2021
## skin_changer
## File description:
## root.py
##

import os

try:
    from . import CONST
except ImportError:
    import constants as CONST

class Root:
    """ Functions used by everyone """
    def __init__(self, error:int=CONST.ERROR, success:int=CONST.SUCCESS) -> None:
        """ The global variables """
        self.success = success
        self.error = error
        self.status = {"status": self.error, "content":""}

    def get_file_content(self, file:str, encoding:str="utf-8") -> list[int, str]:
        """ Get the content of a file """
        result = dict()
        result["status"] = self.success
        result["content"] = ""
        if os.path.exists(file) == True:
            try:
                file = open(file, 'r', encoding=encoding)
                result["content"] = file.read()
                file.close()
            except Exception as error:
                result['status'] = self.error
                result['content'] = str(error)
        else:
            result['status'] = self.error
            result['content'] = "File not found"
        return result

    def env_to_dict(self, string:str) -> list[int, dict]:
        """ Convert an env file to a dict string """
        result = dict()
        result["status"] = CONST.SUCCESS
        result["content"] = ""
        final_list = dict()
        try:
            string = string.split('\n')
            for i in string:
                if i != "":
                    i = i.split('=')
                    final_list[i[0]] = i[1]
            result["content"] = final_list
        except Exception as error:
            result['status'] = CONST.ERROR
            result['content'] = {"error": str(error)}
        return result

    def answer_successefull(self, result:dict) -> bool:
        """ Check if the result is successefull """
        if result["status"] == self.success:
            return True
        return False

    def is_string_empty(self, string:str) -> bool:
        """ Check if the string is empty """
        if len(string) == 0:
            return True
        return False

    def is_string_only_blanks(self, string:str) -> bool:
        """ Check if the string is only blanks """
        for i in string:
            if i != " " or i != "\t":
                return False
        return True

    def output_error(self, result:dict) -> int:
        """ Output the error message """
        if self.answer_successefull(result) == False:
            print(f"Error:\n'{result['content']}'")
        return result["status"]
