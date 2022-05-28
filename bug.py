import webbrowser
import sys, pyperclip


# Get error from command line.
if len(sys.argv) > 1:
    error = "+".join(sys.argv[1:])
# Get error from clipboard.
else:
    error = pyperclip.paste()

webbrowser.open(f"https://duckduckgo.com/?q={error}+python")
