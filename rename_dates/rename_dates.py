#!/usr/bin/env python3
# rename_dates.py - renames filenames with American MM-DD-YYYY date 
#                   format to European DD-MM-YYYY.

import shutil, os, re
from pathlib import Path
# Create a regex that matches files with the American date format.
date_pattern = re.compile(r"""^(.*?)        # all text before the date
        ((0|1)?\d)-                         # one or two digits for the month
        ((0|1|2|3)?\d)-                     # one or two digits for the day
        ((19|20)\d\d)                       # four digits for the year
        (.*?)$                              # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
p = Path.cwd()

for amer_filename in os.listdir(p):
    mo = date_pattern.search(amer_filename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

# Form the European-style filename.
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

# Get the full, absolute file paths.
    #abs_working_dir = os.path.abspath(p)
    #amer_filename = os.path.join(abs_working_dir, amer_filename)
    #euro_filename = os.path.join(abs_working_dir, euro_filename)

    amer_filename = p / amer_filename
    euro_filename = p / euro_filename
    
# Rename the files.
    #print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
    shutil.move(amer_filename, euro_filename)


