##
## EPITECH PROJECT, 2021
## skin_changer
## File description:
## env.py
##

import os
import platform
from .constants import Const as CONST
from .root import Root

class Environment:
    """ Class in charge of processing the .env file """
    def __init__(self, error:int=CONST().ERROR, success:int=CONST().SUCCESS, env_file:str=CONST().ENV_FILE):
        """ The global variables """
        self.author = f"{chr(169)} Henry Letellier"
        self.error = error
        self.success = success
        self.env_file = env_file
        self.env = os.environ
        self.env = self.append_missing_envs()
        self.dos_var_open_symb = "%"
        self.dos_var_closed_symb = self.dos_var_open_symb
        self.env_var_open_symb = "{"
        self.env_var_closed_symb = "}"
        self.ri = Root(self.error, self.success)

    def append_missing_envs(self) -> dict:
        """ Append missing environement variables depending
        on the system on wich the script is run """
        if platform.system() == "Windows":
            self.env["pwd"] = os.getcwd()
            self.env["home"] = self.env["userprofile"]
            self.env["user"] = self.env["username"]

        elif platform.system() != "Windows":
            self.env["userprofile"] = self.env["home"]
            self.env["username"] = self.env["user"]
        return self.env

    def process_vars(self, string:str, open_symb:str, closed_symb:str) -> list[dict,dict]:
        """ Isolate the variables from the string """
        var_name = ""
        string_buffer = ""
        begining_found = False
        ending_found = False
        split_content = list()
        for i, element in enumerate(string):
            if string[i] == closed_symb and begining_found == True:
                ending_found = True
            if begining_found == True and ending_found == False:
                var_name += element
            if string[i] == open_symb:
                begining_found = True
                split_content.append({"type":"string", "name":"","content":string_buffer})
                string_buffer = ""
            if begining_found == False:
                string_buffer += element
            if begining_found == True and ending_found == True:
                split_content.append({"type":"var", "name":var_name,"content":""})
                begining_found = False
                ending_found = False
                var_name = ""
        split_content.append({"type":"string", "name":"","content":string_buffer})

        return split_content

    def compile_vars_to_string(self, string:list[dict, dict]) -> str:
        """ Convert the processed list back into a string """
        final_string = ""
        for element in enumerate(string):
            final_string+=element[1]["content"]
        return final_string

    def get_dos_var_content(self, string:str) -> str:
        """ Get the corresponding content to a dos var """
        if string in self.env:
            return self.env[string]
        return string

    def process_dos_var(self, string:str) -> str:
        """ Replaced called dos vars by their content """
        researched_keyword = "var"
        content_keyword = "content"
        var_name_keyword = "name"

        cut_string = self.process_vars(string, self.dos_var_open_symb, self.dos_var_closed_symb)
        for i in enumerate(cut_string):
            if cut_string[i[0]]["type"] == researched_keyword:
                cut_string[i[0]][content_keyword] = self.get_dos_var_content(cut_string[i[0]][var_name_keyword])

        return self.compile_vars_to_string(cut_string)

    def get_env_var_content(self, var:str, reference:list[dict, dict]) -> str:
        """ Fetch the content of a var """
        if var in reference and ("{"+f"{var}"+"}") not in reference[var]:
            return reference[var]
        return var

    def env_var_filler(self, string:list[dict, dict], environement_vars:list[dict, dict]) -> list[dict, dict]:
        """ Get the content of the variables based on the environement file """
        researched_keyword = "var"
        content_keyword = "content"
        var_name_keyword = "name"
        for i, content in enumerate(string):
            if content["type"] == researched_keyword:
                string[i][content_keyword] = self.get_env_var_content(string[i][var_name_keyword], environement_vars)
        return string

    def process_env_var(self, string:str, env_vars:dict) -> str:
        """ Replace called env vars by their content """
        cut_string = self.process_vars(string, self.env_var_open_symb, self.env_var_closed_symb)
        processed_string = self.env_var_filler(cut_string, env_vars)
        compiled_string = ""
        for i in enumerate(processed_string):
            compiled_string+=processed_string[i[0]]["content"]
        return compiled_string

    def remove_commented_vars(self, env_content:dict) -> dict:
        """ Remove entries who start with a # """
        to_be_removed = list()
        for i in env_content:
            if i[0] == "#":
                to_be_removed.append(i)
        for i in to_be_removed:
            env_content.pop(i)
        return env_content

    def translate(self, env_content:dict) -> dict:
        """ Replace the 'env variables' by their respective content """
        result = {"status": self.success, "content": ""}
        env_content = self.remove_commented_vars(env_content)
        for content in env_content:
            if self.dos_var_open_symb in env_content[content] or self.dos_var_closed_symb in env_content[content]:
                env_content[content] = self.process_dos_var(env_content[content])

        for content in env_content:
            if self.env_var_open_symb in env_content[content] or self.env_var_closed_symb in env_content[content]:
                env_content[content] = self.process_env_var(env_content[content], env_content)

        result["content"] = env_content
        return result


    def get_local_env(self, env_file:str="") -> dict[int, dict]:
        """ Get a local .env file """
        env_content = dict()
        if self.ri.is_string_empty(env_file) == True or self.ri.is_string_only_blanks(env_file) == True:
            if self.ri.is_string_empty(self.env_file) == False and self.ri.is_string_only_blanks(self.env_file) == False:
                env_file = self.env_file
            elif self.ri.is_string_empty(CONST().ENV_FILE) == False and self.ri.is_string_only_blanks(CONST().ENV_FILE) == False:
                env_file = CONST().ENV_FILE
            else:
                env_content["status"] = self.error
                env_content["content"] = "The env filepath is empty"
                return env_content
        env_content = self.ri.get_file_content(env_file)
        if self.ri.answer_successefull(env_content) == True:
            temp = self.ri.env_to_dict(env_content["content"])
            if self.ri.answer_successefull(temp) == True:
                env_content["content"] = temp["content"]
            else:
                env_content["content"] = f"env_to_dict: {env_content['content']}"
        else:
            env_content = {"status": CONST().ERROR, "content": "File not found"}
        return env_content
