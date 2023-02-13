##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## content.py
##

class Content:
    """ Write the content of the processed data to a file """
    def __init__(self) -> None:
        self.data_content = "ee"

    def test_content(self) -> str:
        """ Test the class WriteContent """
        return "test class write content"

    def write_content(self, content:list[list], file_name:str) -> None:
        """ Write the content of the processed data to a file """
        with open(file_name, "w", encoding="utf-8", newline="\n") as file:
            for i in content:
                for j in i:
                    file.write(j)
                file.write("\n")
        file.close()
