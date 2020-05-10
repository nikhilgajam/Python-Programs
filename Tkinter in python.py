from tkinter import *

var = Tk()
var.title("Hello World")
var.iconbitmap(r"hello.ico")
lab = Label(var, text = "Hello World")
lab.pack()
var.mainloop()