#!/usr/bin/env python3
import re

def date_filter(text):
    '''Filters date from a given text'''
    
    date_regex = re.compile(r'''(
            ([0-2][1-9]|3[0-1])         # DD 01-29 or 30-31
            /
            (0[1-9]|1[0-2])             # MM 01-09 or 10-12
            /
            (1\d\d\d|2\d\d\d)              # YYYY 1000 - 2999
            )''', re.VERBOSE)

    filtered_dates = []
    for dates in date_regex.findall(text):
        filtered_dates.append(dates[0])

    return filtered_dates



# TODO: implement check for valid dates

text = 'for leap years; it will accept nonexistent dates like 01/11/1999 31/02/2020 or 31/04/2021.'

print(date_filter(text))
