from tkinter import *
import tkinter.messagebox as tm

def text():
    print("Working!!!")
    
def Aboutus():
    tm.showinfo("About Us", "This is Notes++ App")
    
def ask():
    asks = tm.askquestion("Exit", "Do You Want To Exit")
    
    if asks == "yes":
        root.destroy()
    else:
        pass

root = Tk()
root.title("Notes++")
root.iconbitmap(r"notes.ico")

# Menu

m = Menu(root)
root.config(menu = m)

cm = Menu(m, tearoff = 0)
m.add_cascade(label = "Click", menu = cm)
cm.add_command(label = "Save", command = text)
cm.add_command(label = "Edit", command = text)
cm.add_separator()
cm.add_command(label = "Exit", command = ask)

am = Menu(m, tearoff = 0)
m.add_cascade(label = "About", menu = am)
am.add_command(label = "About Us", command = Aboutus)
am.add_separator()
am.add_command(label = "Help", command = text)

# Toolbar

tl = Label(root, bg = "gray")

b1 = Button(tl, text = "Image", command = text)
b1.pack(side = LEFT, padx = 2, pady = 2)
b2 = Button(tl, text = "Pack", command = text)
b2.pack(side = LEFT, padx = 2, pady = 2)
b3 = Button(tl, text = "Print", command = text)
b3.pack(side = LEFT, padx = 2, pady = 2)

tl.pack(side = TOP, fill = X)

# Statusbar

sb = Label(root, text = "Hello World", bd = 1, relief = SUNKEN, anchor = W)
sb.pack(side = BOTTOM, fill= X)

# Entry

et = Entry(root)
et.pack()

# Photo

pic = PhotoImage(file = "hello.png")
l1 = Label(root, image = pic)
l1.pack()

root.mainloop()
