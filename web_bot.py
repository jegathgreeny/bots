import time, sys, os
import pyautogui


name = sys.argv[1]
print(f"Project Title: ----{name}<<<<")

# Default pause for all pyautogui calls.
pyautogui.PAUSE = 0.6

# Clear the screen.
pyautogui.hotkey("winleft", "d")

# Project directory.
working_directory = rf"C:\Users\jegat\Desktop\py_work\{name}"

# Create a new directory in py_work and switch to it.
os.makedirs(working_directory)
os.chdir(working_directory)
with open(".gitignore", "w") as ignoreFile:
    ignoreFile.write("__pycache__/")

# Git integration.

# Open git and change directory.
pyautogui.hotkey("shift", "f10")
pyautogui.press("down", presses=8)
pyautogui.press("enter")
time.sleep(3)
pyautogui.write(f"cd C:/Users/jegat/Desktop/py_work/{name}", 0.04)
pyautogui.press("\n")

# Initialize a repository.
pyautogui.write("git init", 0.04)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("git status", 0.04)
pyautogui.press("enter")
time.sleep(1)

# Add files to the repository.
pyautogui.write("git add .", 0.04)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("git status", 0.04)
pyautogui.press("enter")
time.sleep(1)

# Make a commit.
pyautogui.write(f'git commit -m "{name.title()} project started."', 0.04)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("git status", 0.04)
pyautogui.press("enter")
time.sleep(2)

# Open command prompt.
pyautogui.press("win")
pyautogui.write("cmd", 0.04)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write(f"cd {working_directory}", 0.04)
pyautogui.press("enter")
time.sleep(1)
print("command prompt accessed...")

# Initiate the virtual environment.
pyautogui.write(f"python -m venv {name}_env", 0.04)
pyautogui.press("enter")
time.sleep(12)
print("virtual environment created...")

# Activate the virtual environment.
pyautogui.write(f"{name}_env\\Scripts\\activate", 0.04)
pyautogui.press("enter")
time.sleep(2)
print("virtual environment activated...")

# Check if virtual environment is working.
pyautogui.write("pip list")
pyautogui.press("enter")
time.sleep(6)

# Install django.
pyautogui.write("pip install django", 0.04)
pyautogui.press("enter")
time.sleep(25)
print("django installed...")

# Create a new project in django.
pyautogui.write(f"django-admin startproject {name} .", 0.04)
pyautogui.press("enter")
time.sleep(3)
print(f"new django project {name} started...")

# Check all the created directory.
pyautogui.write("dir", 0.04)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write(f"dir {name}", 0.04)
pyautogui.press("enter")
print("directory checked...")

# Create the database.
pyautogui.write("python manage.py migrate", 0.04)
pyautogui.press("enter")
time.sleep(10)
print("database created...")

# Check the database directory.
pyautogui.write("dir", 0.04)
pyautogui.press("enter")
time.sleep(1)
print("database directory checked...")

# Run the development server.
pyautogui.write("python manage.py runserver", 0.04)
pyautogui.press("enter")
time.sleep(4)
print("development server started...")

# View the page.
pyautogui.hotkey("win", "2")
time.sleep(3)
pyautogui.write("http://127.0.0.1:8000/", 0.04)
pyautogui.press("enter")
print("local host running...")

# To minimize firefox and command prompt.
for i in range(3):
    pyautogui.hotkey("win", "down")

# Add the new files into the repository.
pyautogui.write("git add .", 0.04)
pyautogui.press("enter")
time.sleep(25)
pyautogui.write("git status", 0.04)
pyautogui.press("enter")
time.sleep(3)

# Make a commit.
pyautogui.write('git commit -am "Development server started."', 0.04)
pyautogui.press("enter")
time.sleep(22)
pyautogui.write("git status", 0.04)
pyautogui.press("enter")
time.sleep(2)

# Check the log.
pyautogui.write("git log --pretty=oneline", 0.04)
pyautogui.press("enter")
time.sleep(1)

# Bring commad prompt and firefox into display.
pyautogui.hotkey('alt', '\t')
pyautogui.hotkey('win', '2')

# Display that the bot has finished it's work
pyautogui.alert(text="Web bot terminated...", title="Automation", button="ok")
