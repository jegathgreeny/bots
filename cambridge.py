import sys
import webbrowser

import pyperclip

# The official link to cambridge dictionary.
link = "https://dictionary.cambridge.org/dictionary/english/"

# This runs if words to be searched are in the command prompt.
if len(sys.argv) > 1:
    for word in sys.argv[1:]:
        webbrowser.open(f"{link}{word}")
# This runs if words are in the clipboard.
else:
    words = pyperclip.paste().split(" ")
    # Removes empty strings.
    words.remove("")
    for word in words:
        webbrowser.open(f"{link}{word}")
