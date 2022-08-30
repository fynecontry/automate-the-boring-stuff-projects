#!/usr/bin/env python3
# Regex search - file ...

import re
from pathlib import Path


def main():
    '''Main function which call other functions for program exe'''

    user_input = input('Please enter pattern to search for :')
    user_regex = re.compile(f'{user_input}')

    folder = Path.cwd()
    files_content_dict = {}

    for filename in folder.glob('*.txt'):
        file_object = open(str(filename))
        file_content = file_object.readlines()
        for line in file_content:
            if user_regex.findall(line):
                files_content_dict[filename.name] = line

    for key, value in files_content_dict.items():
        print(f'From file {key} - {value}')

if __name__ =="__main__":
    main()

