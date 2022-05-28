# blue.py -- Executes bluetooth tethering.

import os
import time

import pyautogui

pyautogui.PAUSE = 0.6

# opens control panel
os.system('control.exe ')
time.sleep(2)

# Navigate to view devices and printers. 
pyautogui.press('\t', presses=10)
pyautogui.press('\n')
time.sleep(1)

# navigate on 'connect using'
pyautogui.press('right', presses=3)
time.sleep(1)
pyautogui.hotkey('shift', 'f10')

# connect via access point
pyautogui.typewrite(['down', 'right', 'down', '\n'], 1)

# close control panel
pyautogui.hotkey('alt', 'f4')
