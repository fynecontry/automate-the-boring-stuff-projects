#!/usr/bin/env python3
# map_it.py - Launches a map in the browser using an address
# from the command line or clipboard

import webbrowser, sys, logging, pyperclip
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if len(sys.argv) > 1:
    # Get address from the command line
    address = ' '.join(sys.argv[1:])
    logging.debug(f'address - {address}')
else:
    # Get address from clipboard
    address = pyperclip.paste()
    logging.debug(f'address extracted from clipboard: {address}')

webbrowser.open('https://www.google.com/maps/place/' + address)
logging.info('Address map opened sucessfully')
