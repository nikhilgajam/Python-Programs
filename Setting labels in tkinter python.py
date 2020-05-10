from tkinter import *

root = Tk()

l1 = Label(root, text="Hello World", bg="gray", fg = "white")
l1.pack()

l2 = Label(root, text="Header\n", bg="grey", fg = "white")
l2.pack(fill=X)

l3 = Label(root, text="Control", bg="gray", fg = "white")
l3.pack(side=LEFT, fill=Y)

root.mainloop()