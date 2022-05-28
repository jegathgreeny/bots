import pyautogui, time
import os


# Pause for half a second before each pyautogui call.
pyautogui.PAUSE = 0.5

# Switch to book window.
pyautogui.hotkey('win', '\t')
pyautogui.click(791, 911)

# Open books.
pyautogui.hotkey('win', '2')
time.sleep(3)
pyautogui.hotkey('ctrl', 'b')
pyautogui.typewrite(['\t', 'down'])
with pyautogui.hold('ctrl'):
	pyautogui.press(['down', 'space', 'down', 'space'])
pyautogui.rightClick(119, 272)
pyautogui.typewrite(['down', 'enter'])
pyautogui.click(258, 26)
time.sleep(1)

# Switch back to work window,
pyautogui.hotkey('win', '\t')
pyautogui.click(467, 915)
time.sleep(1)

# Open command prompt on learning log directory.
os.system('start cmd')
time.sleep(2)
pyautogui.write(r"cd C:\Users\jegat\Desktop\py_work\for_pull\learning_log", 0.02)
pyautogui.press('enter')

# Activating virtual environment.
pyautogui.write("ll_env\\Scripts\\activate", 0.02)
pyautogui.press("enter")
time.sleep(2)


# Run development server.
pyautogui.write("python manage.py runserver", 0.02)
pyautogui.press('enter')
time.sleep(4)

# Launch site.
os.system('start firefox')
time.sleep(3)
pyautogui.write('http://127.0.0.1:8000', 0.02)
pyautogui.press('enter')
