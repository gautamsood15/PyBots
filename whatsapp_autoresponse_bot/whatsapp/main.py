import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("smily_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

# Gets message
