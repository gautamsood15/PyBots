import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)

position1 = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

# Gets message
def get_message():
    global x, y

    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]

    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 70, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message received: " + whatsapp_message)

    return whatsapp_message

# Posts
def post_response(message):
    global x, y

    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    # pt.typewrite("\n", interval=.01)


# Processes Response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions!"

    else:
        if random_no == 0:
            return "That's cool!"
        elif random_no == 1:
            return "Remember to subscribe to Code Palace!"
        else:
            return "I want to eat something."

processed_message = process_response(get_message())
post_response(processed_message)


get_message()

post_response(get_message())





