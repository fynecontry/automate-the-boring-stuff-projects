# automate-the-boring-stuff projects implementation
My solutions to automation project ideas from [automate the boring stuff with python by Al Sweigart](https://automatetheboringstuff.com)

Install required Python modules for executing programs in this repo by running (use `python3` on macOS and Linux):

    python -m pip install --user automate-linux-requirements.txt
    
This will install the following modules:
* `send2trash==1.5.0`
* `requests==2.21.0`
* `beautifulsoup4==4.7.1`
* `selenium==3.141.0`
* `openpyxl==2.6.1`
* `PyPDF2==1.26.0`
* `python-docx==0.8.10`
* `imapclient==2.1.0`
* `pyzmail36==1.0.4`
* `twilio`
* `pillow==5.4.1`
* `PyInputPlus==0.2.6`
* `ezgmail==0.0.4`
* `ezsheets==0.0.2`
* `python3-xlib==0.15`
* `pyautogui==0.9.42`

### Projects Description

* [command_line_emailer](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/command_line_emailer) - A tool which send emails via the command line using args passed.

* [download_xkcd](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/download_xkcd) - Program scraps XKCD and downloads every comic to XKCD directory

* [search_pypi](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/search_pypi) - Searches PyPi and opens 5 tabs results for specific python packages

* [map_it](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/map_it) - Launches Google map in the browser using an address from the command line or clipboard

* [debugging_coin_toss](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/debugging_coin_toss) - A program which debugs and logs events in coin toss simulation.

* [filling_gaps](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/filling_gaps) - Finds all files with a given prefix, such as spam001.txt, spam002.txt/ etc.. and locates any gaps in the numbering then either fills the gaps by renaming (fill_gaps.py)
or insert gaps by renaming (add_gaps.py)

* [delete_unneeded_files](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/delete_unneeded_files) - A program which traverses a folder and deletes greater than MAX_SIZE where MAX_SIZE = 100MB.

* [selective_copy](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/selective_copy) - Walks through a folder tree and searches for files with a certain file extension (such as .pdf, .txt or .jpg) copy these files into a new folder.

* [backup_to_zip](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/backup_to_zip) - Copies an entire folder and its contents into a ZIP file whose filename increments.

* [rename_dates](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/rename_dates) - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY

* [regex_search](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/regex_search) - Opens all .txt files in a folder and searches for line that matches a user-supplied regular expression.

* [mad_libs](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/mad_libs) - A program that searches a file for  ADJECTIVE, NOUN, ADVERB, or VERB keywords and replaces them for user prompted words in a modified file.

* [multi-clipboard](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/multi-clipboard) - Arguments passed to the command line program with the save, delete and list keywords, will either save clipboard to keyword, load or delete saved clipboard shelfs.

* [random_quiz_generator](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/random_quiz_generator) - Creates random quizzes and stores questions and answers in different files, along with answer keys.

* [phone_and_email_extractor](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/phone_and_email_extractor) - Finds and extracts phone numbers and email addresses on system's clipboard.

* [multiplication_quiz](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/multiplication_quiz) - Program prompts user with 10 random multiplication questions, ranging from 0 x 0 to 9 x 9

* [regex_version_python_strip_method](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/regex_version_python_strip_method) - 
Regex implementation of python's built-in strip function

* [date_detector](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/date_detection) - Using regular expressions, script can detect dates in the DD/MM/YYYY formats.

* [table_printer](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/table_printer) -  Given a list of lists, program displays it in a well-organized table with column right-justified.

* [fantasy_game_inventory](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/fantasy_game_inventory) - Using a dictionary to model player's inventory where keys describe the items in the inventory and values are integer detailing how items a player has.

* [chess_dictionary_validator](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/chess_dictionary_validator) - A chess board simulator using different data structures such as dictionaries

* [the_collatz_sequence](https://github.com/fynecontry/automate-the-boring-stuff-projects/tree/main/the_collatz_sequence) -  Recurvisely reduces passed integer to 1 using Collatz sequence
