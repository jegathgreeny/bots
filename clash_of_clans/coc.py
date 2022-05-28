import time

from pyautogui import *

directory = r'C:\Users\jegat\Desktop\py_work\work\bots\clash_of_clans'

# Begin usb debuging.
hotkey('win', 'r')
time.sleep(1)
write('scrcpy', 0.02)
time.sleep(1)
press('enter')
time.sleep(5)
hotkey('alt', '\t')
time.sleep(2)
scrcpy_prompt = getActiveWindow()
click(scrcpy_prompt.right - 155, scrcpy_prompt.top + 15)
time.sleep(1.5)

# open clash of clans
mobile = getActiveWindow()
click(mobile.center)
drag(-200, 0, 0.4)
time.sleep(1.5)
clash_icon = locateOnScreen(f'{directory}\clash.png', confidence=0.8)
doubleClick(clash_icon, interval=0.5)
time.sleep(25)
# open in fullscreen
click(mobile.right - 94, mobile.top + 15)

# drag to make resources visible
click(195, 402);dragTo(293, 749, 0.5)
time.sleep(1)

# collect the resources.
gold = locateOnScreen(f'{directory}\gold.png', confidence=0.8)
doubleClick(gold)
elixir = locateOnScreen(f'{directory}\elixir.png', confidence=0.8)
doubleClick(elixir)
dark_elixir = locateOnScreen(f'{directory}\dark_elixir.png', confidence=0.8)
doubleClick(dark_elixir)
