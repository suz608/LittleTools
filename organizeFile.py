# This is a python program that removes all files end with .tmp in the target directory
# File organizing with python tutorial: https://www.python-engineer.com/posts/file-organization/#how-to-delete-files-and-folders-in-python

import os
# Print current working directory
# print(os.getcwd())

# Go to target directory
os.chdir("photos/Douban")

temp = (".tmp")

# Return files end with .tmp
def is_temp(file):
    return os.path.splitext(file)[1] in temp

# Remove files end with .tmp
for file in os.listdir():
    if is_temp(file):
        os.remove(file)