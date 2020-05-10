from tkinter import *

root = Tk()
root.title("Binding In Tkinter")

def left(event):
    #pylint: disable=unused-argument
    print("Left")

def middle(event):
    #pylint: disable=unused-argument
    print("Middle")
    
def right(event):
    #pylint: disable=unused-argument
    print("Right")
    
l = Label(text = "Button Checker App")
l.pack()
    
space = Frame(root, width = 400, height = 400)
space.bind("<Button-1>", left)
space.bind("<Button-2>", middle)
space.bind("<Button-3>", right)

space.pack()

root.mainloop()