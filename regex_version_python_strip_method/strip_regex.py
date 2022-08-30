#!/usr/bin/env python3

# Program - which implement regex version of strip()

import re, sys

def strip_regex(text, char=''):
    '''Strip whitespaces from string passed, and strip optional character'''

    non_white_space = re.compile(r'[^\s]')
    
    # if 2nd character argument passed strip it
    if char:
        char_regex = re.compile(char)
        new_text = ''.join(non_white_space.findall(text))
        new_text = char_regex.sub('', new_text)
        return new_text
    else:
        return ''.join(non_white_space.findall(text))


def main():
    '''Main program'''

    print('Please input the text: ', end='')
    users_string = input()
    print('Character to strip: ', end='')
    strip_char = input()
    print(strip_regex(users_string, strip_char))


if __name__ == "__main__":
    main()
    
    
