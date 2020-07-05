from tkinter import *
# Displays the key events


# Shows on the screen
def key_pressed(event):
    show.insert(END, str(event) + "\n")
    show.yview(END)   # Auto Scroll


root = Tk()
root.bind("<Key>", key_pressed)

lbl = Label(root, text="Key Events")
lbl.pack()

show = Text(root,  font="21")
show.pack()

root.mainloop()
