from tkinter import *

root = Tk()
root.title("Button Checker")

def left(event):
    print("Left")

def middle(event):
    print("Middle")
    
def right(event):
    print("Right")
    
l = Label(text = "Button Checker App")
l.pack()
    
space = Frame(root, width = 400, height = 400)
space.bind("<Button-1>", left)
space.bind("<Button-2>", middle)
space.bind("<Button-3>", right)

space.pack()

root.mainloop()