#!/usr/bin/env python3
# mcb.pyw - Saves and loads piece of text to the clipboard.
# Usage: python3 mcb.pyw save <keyword> - Saves clipboard to keyword.
#   python3 mcb.pyw <keyword> - Loads keyword data to clipboard.
#   python3 mcb.pyw list - Loads all keywords to clipboard.
#   python3 mcb.pyw delete <keyword> - delete keyword data
#   python3 mcb.pyw delete - delete all keywords

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb.db')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
