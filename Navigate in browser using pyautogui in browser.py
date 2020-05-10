import webbrowser
import pyautogui as py
import time


# This will open a browser

webbrowser.open("https://www.google.com")

time.sleep(3)

# This sleep will make the computer to wait 3 seconds

py.write('Nikhil Tech', interval=0.1)

# This py.write will enter that text into google search box

py.keyDown('return')

# This will press the enter

py.moveTo(0, 500)

# This will move your move to a mentioned position

time.sleep(1)

# It makes the computer to wait 1 second

py.click()

# Mouse button will be pressed

py.keyDown('tab')

# Tab button will be pressed

py.keyDown('return')

# Enter button will be pressed
