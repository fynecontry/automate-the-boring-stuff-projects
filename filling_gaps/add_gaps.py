#!/usr/bin/env python3
# add_gaps.py - A program which finds all files with a given prefix and
#               add gaps in the numbering of the files

import os, re, shutil

prefix_regex = re.compile(r'(^.*?)([1-9]+)(\..*$)')

# Get absolute path of cwd
folder = os.path.abspath('.')
first_occurence = True

# Traverse the list of file in cwd
for filename in sorted(os.listdir(folder), reverse=True):
    mo = prefix_regex.search(filename)
    # capture no. for first ocurrence & skip eval.
    if mo and first_occurence:
        current = int(mo.group(2)) + 2
        # construct full paths for file renaming
        current_file_path = os.path.join(folder, filename)
        file_rename = mo.group(1) + str(current) + mo.group(3)
        file_renamed_path = os.path.join(folder, file_rename)
        print(f'{current_file_path} ---> {file_renamed_path}')
        shutil.move(current_file_path, file_renamed_path)
        prev = current
        first_occurence = False

    elif mo:
        print(f'{filename}')
        current = prev - 2
        # construct full paths for file renaming
        current_file_path = os.path.join(folder, filename)
        file_rename = mo.group(1) + str(current) + mo.group(3)
        file_renamed_path = os.path.join(folder, file_rename)
        print(f'{current_file_path} ---> {file_renamed_path}')
        # rename file
        shutil.move(current_file_path, file_renamed_path)

        # update increment eval.
        prev = current
