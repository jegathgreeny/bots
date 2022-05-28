import sys
import time

import pyautogui

# Apps that are running as administrator can't be closed.

# To get all the running window objects.
windows = pyautogui.getAllWindows()

# These are the default background apps that shouldn't be disturbed.
defaultWindows = ["", r"C:\Windows\system32\cmd.exe", "Windows Input Experience"]

# Print a message, that the system is about to close all apps.
print("Closing all apps ", end="")
pyautogui.countdown(3)

# Kill all the apps except the default ones.
for window in windows:
    if window.title in defaultWindows:
        continue
    # print(window.title)
    window.close()


# This is to restart windows, if more than one argument exists.
if len(sys.argv) > 1:
    time.sleep(0.5)
    pyautogui.press("right")
