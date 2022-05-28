#! python3
# form.py - Fills in the form.

from time import sleep

import pyautogui

data = [
    {
        "e-mail": "jegathgreeny@gmail.com",
        "mobile.no": "8248489836",
        "reg.no": "312418114053",
        "name": "Jegath Greeny.E.S",
    }
]

pyautogui.PAUSE = 0.5

# Access chrome.
pyautogui.press("win")
pyautogui.write("chrome", 0.02)
pyautogui.press("enter")
sleep(10)

# Access google classroom.
pyautogui.click(793, 464)
pyautogui.confirm("Do you want to continue?")

# Accessing question paper and google form .
pyautogui.rightClick(784, 343)
pyautogui.write(["down", "enter"], 0.02)
sleep(1)
pyautogui.click(351, 345)

# The main loop.
for person in data:

    # Give the user a chance to kill the script.
    print(">>> 15-SECOND PAUSE TO LET USER PRESS CTRL-C <<<")
    sleep(15)

    # Terminal output.
    print(f"Entering {person['name']}'s info...")
    pyautogui.write("\t")
    sleep(1)

    # Enters the email id.
    pyautogui.write(person["e-mail"] + "\t", 0.02)
    sleep(0.5)

    # Enter the mobile number.
    pyautogui.write(person["mobile.no"] + "\t", 0.02)
    sleep(0.5)

    # Fill out the reg.no field.
    pyautogui.write(person["reg.no"] + "\t", 0.02)
    sleep(0.5)

    # Fill out the name field.
    pyautogui.write(person["name"].upper() + "\t", 0.02)
    sleep(0.5)

    # Choose the date.
    pyautogui.write([" ", "\t", "enter"], 0.02)
    pyautogui.write(["\t", "\t", "\t"], 0.02)
    sleep(0.5)

    # Terminal assurance output.
    print("Entered fixed data...")
