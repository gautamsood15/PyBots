import pyautogui as pt
from time import sleep

# red heart colour = (237, 73, 86)

class GuiCommands:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def navigate_to_heart(self, speed):
        position = pt.locateOnScreen()
        
