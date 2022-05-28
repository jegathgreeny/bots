import os
import time
import webbrowser

import pyautogui
import pyscreeze
from selenium import webdriver

alphabets = {
    "a": "a.png",
    "b": "b.png",
    "c": "c.png",
    "d": "d.png",
    "e": "e.png",
    "f": "f.png",
    "g": "g.png",
    "h": "h.png",
    "i": "i.png",
    "j": "j.png",
    "k": "k.png",
    "l": "l.png",
    "m": "m.png",
    "n": "n.png",
    "o": "o.png",
    "p": "p.png",
    "q": "q.png",
    "r": "r.png",
    "s": "s.png",
    "t": "t.png",
    "u": "u.png",
    "v": "v.png",
    "w": "w.png",
    "x": "x.png",
    "y": "y.png",
    "z": "z.png",
}

# screenshot of the image
# change the left, top, width, height
# question = pyscreeze.screenshot("image.png", region=(0, 40, 300, 500))


# open google images
browser = webdriver.Firefox()
browser.get("https://images.google.co.uk/imghp?sbi=1")
# upload the image
image_link = browser.find_element_by_link_text("Upload an image")
image_link.click()

# drv.find_element_by_id("IdOfInputTypeFile").send_keys(os.getcwd()+"/image.png")

# upload the image
# pyautogui.click()
# pyautogui.click()
# pyautogui.write(['\t'])
# pyautogui.write('')
# pyautogui.press('enter')
# pyautogui.write(['\t'])



# for i in range(len(answer)):
#     if answer[i] in alphabets.keys():
#         current_alphabet_filename = alphabets[answer[i]]
#         location = pyscreeze.locateOnScreen(current_alphabet)
#         time.sleep(0.4)
#         pyautogui.click(location)
