from tkinter import *

root = Tk()
root.title("Option Menu")
root.geometry("400x400")

# Option Menu In Tkinter

# It will look better

# When you use ttk

# Select any theme or change it to look more like a real option menu


def show():
    lbl = Label(root, text=var.get())
    lbl.pack()


options = ["Select An Item",
           "Hello",
           "World",
           "Welcome"
           ]

var = StringVar()
var.set(options[0])


opt_menu = OptionMenu(root, var, *options)
opt_menu.pack()


btn = Button(root, text="Click", command=show)
btn.pack()


root.mainloop()
