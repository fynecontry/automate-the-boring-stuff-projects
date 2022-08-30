#!/usr/bin/env python3
# delete_unneeded.py - a program which traverses a folder and
#                   deletes files greater than MAX_SIZE

import os, shutil

# traverse current working directory
folder = os.path.abspath('.')

MAX_SIZE = 100000000     # allowed max size in bytes (100MB)

# Walk directory and delete(unlink) files > MAX_SIZE
for folder, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        file_path = os.path.join(folder, filename)
        if os.path.getsize(file_path) > MAX_SIZE:
            #os.unlink(file_path)
            print(f'Deleted {file_path}')

print('Done')
