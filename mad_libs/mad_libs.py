#!/usr/bin/env python3
# Mad Libs - A program that replaces ADJECTIVE, NOUN, ADVERB, or VERB keyword
#           for user prompted words

# Read and store file contents
import sys
from pathlib import Path
def main():
    '''Executes program and make calls to other functions'''
    KEYWORDS = ('ADJECTIVE', 'NOUN', 'ADVERB', 'VERB')     # Const keywords to search for


    while True:
        filename = input('Enter the name of the file: ')
        if Path.is_file(Path.cwd() / filename):
            break
        else:
            try:
                print('File does not exist in this directory, please retry' +
                'or press Ctrl-C to exit and change directories!')
            except KeyboardInterrupt:
                print('Bye!!')
    file_object = open(filename)
    phrase_content = file_object.read()
    file_object.close()
    phrase_content_list = phrase_content.split()

    for index, word in enumerate(phrase_content_list):
        if word.startswith(KEYWORDS):
            # Call user prompt function for string replacement
            phrase_content_list[index] = user_prompt(word)

    phrase_content = ' '.join(phrase_content_list)

    file_object = open('phrase_modified.txt', 'w')
    file_object.write(phrase_content + '\n')
    file_object.close()

    


# Implement user prompt function
def user_prompt(word):
    if word.lower().startswith('a'):
        user_choice = input(f'Enter an {word}: ')
    else:
        user_choice = input(f'Enter a {word}: ')

    return user_choice


if __name__ == "__main__":
    main()
