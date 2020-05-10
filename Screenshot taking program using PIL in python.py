from PIL import ImageGrab


def screen_shot():
    img = ImageGrab.grab()
    img.show()          # It just shows not saves
    img.save("screenshot.png")   # saves the pic


screen_shot()
