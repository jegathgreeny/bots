import os
import shelve
import sys
import time

import pyperclip

# use this using commands

# mcb save <value> - To save key value in the shelve file.
# mcb delete <key> - To delete a key value pair from the shelve file.
# mcb list - To load all the available keys to the clipboard.
# mcb <key> - To load a specific value to clipboard.


os.chdir(r"C:\Users\jegat\Desktop\py_work\work\bots\clipboard")

mcbShelf = shelve.open("mcb")

if len(sys.argv) == 3:

    # Save clipboard content to that variable like key value pairs.
    if sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print(f"{sys.argv[2]} -- added")

    # To delete a specific key value pair from shelf file.
    elif sys.argv[1].lower() == "delete":
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]
            print(f"removing -- {sys.argv[2]}")

elif len(sys.argv) == 2:

    # Lists keywords and loads content.
    if sys.argv[1].lower() == "list":
        all_keys = str(list(mcbShelf.keys()))
        pyperclip.copy(all_keys)
        print(all_keys)
        time.sleep(2)

    # Loads the keyword equivalent value to the clipboard.
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(f"{sys.argv[1]} -- loaded to clipboard")

    # To clear the shelf.
    elif sys.argv[1].lower() == "clear":
        mcbShelf.clear()
        print("-- shelf cleared")

mcbShelf.close()

# To look at the command prompt for assurance.
time.sleep(1)
