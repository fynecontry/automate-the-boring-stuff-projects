#!/usr/bin/env python3

def comma_code(list_values):
    '''
    Returns a string from list items with trailing , and space
    '''
    # check for empty list and throw error
    if not list_values:
        raise RuntimeError("List passed is empty, try passing a list with values")

    converted = ''
    # Iterate of list items and append ', '
    for index, val in enumerate(list_values, start=1):
        #last item in list should end in 'and {val}'
        if index == len(list_values):
            converted += 'and ' + val
        else:
            converted += val + ', '

    return converted


# Main program

#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = []
print(comma_code(spam))
