import webbrowser
import csv, json
import pyautogui, time


selected_list = []
directory = r"C:\Users\jegat\Desktop\py_work\work\bots\link_generator"
# Change the category to switch.
category = "action.csv"


# So absolute paths are not needed.
# This is a relative path.
with open(f"{directory}/imdb_data/{category}") as movieFile:
    movieReader = csv.reader(movieFile)
    movieData = list(movieReader)

# Loads the last stored row number.
with open(f"{directory}/imdb_data/current.json", "r") as current:
    start = json.load(current)

# The end point of the loop.
stop = start + 50
for i in range(start, stop):
    title = movieData[i][0]
    year = movieData[i][1]
    webbrowser.open(
        f"https://google.com/search?channel=nrow5&client=firefox-b-d&q={title}, {year}"
    )
    the_alert = pyautogui.confirm(
        f'Add "{title}"', "Selected List", buttons=["yes", "no"]
    )
    if the_alert == "yes":
        selected_list.append(f"{title} {year}\n")


# Stores the last row number.
with open(f"{directory}/imdb_data/current.json", "w") as current:
    json.dump(i + 1, current)

# Closes the browser.
browser = pyautogui.getActiveWindow()
browser.close()

# Stores the selected movie titles.
with open(f"{directory}/selected.txt", "w") as selected_file:
    for movie in selected_list:
        selected_file.write(movie.lower().replace(" ", "-"))

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("yts")
time.sleep(1)
