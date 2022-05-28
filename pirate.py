import sys
import webbrowser

import pyperclip

if len(sys.argv) > 1:
    # Get the search word from command line.
    search_for = " ".join(sys.argv[1:])
else:
    # Get the search word from clipboard.
    search_for = pyperclip.copy()

# The pirate bay url.
urls = [
    f"https://thepiratebay.org/search.php?q={search_for}&all=on&search=Pirate+Search&page=0&orderby=",
    f"https://www.1337xx.to/search/{search_for}/1/",
]

[webbrowser.open(url) for url in urls] 
