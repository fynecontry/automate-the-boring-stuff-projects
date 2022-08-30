#!/usr/bin/env python3

# fill_gaps.py - A program which finds all files with a given prefix and 
#               fills any gaps in the numbering of the files

import os, re, shutil

prefix_regex = re.compile(r'(^.*?)([1-9]+)(\..*$)')     # matches and captures numbers in a files

# Get absolute path of cwd
folder = os.path.abspath('.')
first_occurence = True

# traverse the list of file in cwd
for filename in sorted(os.listdir(folder)):
    mo = prefix_regex.search(filename)
    # Capture num for first occurence & skip eval.
    if mo and first_occurence:
        first_occurence = False
        prev = int(mo.group(2))
        continue

    elif mo:
        print(f'{filename}')
        current = int(mo.group(2))
        # Evaluate if filename increases by 1
        if (current - prev) > 1:
            current = prev + 1

            # construct full paths for file renaming
            current_file_path = os.path.join(folder, filename)
            file_rename = mo.group(1) + str(current) + mo.group(3)
            file_renamed_path = os.path.join(folder, file_rename)
            print(f'{current_file_path} ---> {file_renamed_path}')
            # rename file
            shutil.move(current_file_path, file_renamed_path)

            # update increment eval.
            prev = current
