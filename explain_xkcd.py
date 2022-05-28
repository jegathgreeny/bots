import webbrowser, sys


# Opens explainxkcd with the current comic number.
webbrowser.open(f'https://www.explainxkcd.com/{sys.argv[1]}')