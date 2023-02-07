##
## EPITECH PROJECT, 2022
## makator_v2 (Workspace)
## File description:
## fold_content.py
##

import os

# get the content of a folder
def get_content(path):
    content = os.listdir(path)
    return content

# get all the content of a folder and return it as a list
def get_content_list(path):
    content = get_content(path)
    content_list = []
    for i in content:
        content_list.append(i)
    return content_list
