from tkinter import *

root = Tk()
root.geometry("250x300")
with open("logics.py", "r") as p:
    a = p.read()

k = Text(root)  # height and width can be used
k.insert(END, a)
k.pack(expand=TRUE, fill=BOTH)


root.mainloop()




































