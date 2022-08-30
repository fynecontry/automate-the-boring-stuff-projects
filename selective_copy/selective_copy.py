#!/usr/bin/env python3
# selective_copy.py - Program which searches for files in a folder
#                   with specific extension and move to new folder

import os, shutil
from pathlib import Path

# Select current working directory to traverse
folder = str(Path.cwd())

# new folder where files should be stored
new_location = folder + '/recent_copies'
try:
    os.mkdir(new_location)
except FileExistsError:
    print(f'{new_location} already exists, trying copy operations now...')

# walk folder and copy of .py files
for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith('.py') and not os.path.exists(new_location +'/'+ filename):
            file_path = os.path.join(foldername,filename)
            shutil.copy(file_path, new_location)
            print(f'Copied {file_path} --> {new_location}')

print('Done!')


