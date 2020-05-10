import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import tkinter.messagebox


root = Tk()
root.iconbitmap(r'images\n.ico')
root.title("Nikhil Music")
# root.geometry("300x300")
mixer.init()


# Commands used

name = TRUE
paused = FALSE
muted = FALSE


def play():
    global paused

    if paused:
        mixer.music.unpause()
        sb['text'] = 'Music Resumed:' + ' ' + os.path.basename(name)
        globals()['paused'] = None
    else:
        try:
            mixer.music.load(name)  # Selecting the music track
            mixer.music.play()   # Playing the selected track
            sb['text'] = 'Playing Music:' + ' ' + os.path.basename(name)
        except NameError:
            tkinter.messagebox.showerror("Song", "Select a song by clicking Player > Open")
            open_file()


def stop():
    mixer.music.stop()  # Music stopping statement
    sb['text'] = "Music Stopped"


def rewind():
    mixer.music.play()
    sb['text'] = 'Music Rewinded' + ' ' + os.path.basename(name)


def pause():
    global paused
    paused = TRUE
    mixer.music.pause()
    sb['text'] = 'Music Paused:' + ' ' + os.path.basename(name)


def mute():
    global muted
    if muted:
        mixer.music.set_volume(0.5)
        b5.configure(image=mutePic)
        scale.set(50)
        muted = FALSE
        sb['text'] = 'Music Unmuted:'
    else:
        mixer.music.set_volume(0)
        scale.set(0)
        b5.configure(image=volPic)
        muted = TRUE
        sb['text'] = 'Music Muted:'


def vol(val):
    volume = int(val)/100   # Volume adjustment
    mixer.music.set_volume(volume)


def about():
    tkinter.messagebox.showinfo("About Us", "Nikhil Music")  # Prompt information


def ask():
    asks = tkinter.messagebox.askquestion("Exit", "Do You Want To Exit")  # Prompt to close

    if asks == "yes":
        root.destroy()  # To quit the window
    else:
        pass


def open_file():
    global name
    name = filedialog.askopenfilename()  # Opening a open window
    play()


# Menu

m = Menu(root)
root.config(menu=m)

cm = Menu(m, tearoff=0)
m.add_cascade(label="Player", menu=cm)
cm.add_command(label="Open", command=open_file)
cm.add_separator()
cm.add_command(label = "Exit", command=ask)

am = Menu(m, tearoff=0)
m.add_cascade(label="About", menu=am)
am.add_command(label="About Us", command=about)

# Label

l1 = Label(root, text="Nikhil Music")
l1.pack()

# Buttons with pictures

middle = Frame(root)
middle.pack(padx=3, pady=3)

playPic = PhotoImage(file=r"images\play.png")
b1 = Button(middle, image=playPic, command=play, bg="white")
b1.grid(row=0, column=0, padx=3, pady=3)

pausePic = PhotoImage(file=r"images\pause.png")
b2 = Button(middle, image=pausePic, command=pause, bg="white")
b2.grid(row=0, column=1, padx=3, pady=3)

stopPic = PhotoImage(file=r"images\stop.png")
b3 = Button(middle, image=stopPic, command=stop, bg="white")
b3.grid(row=0, column=2, padx=3, pady=3)

bottom = Frame(root)
bottom.pack()

rewindPic = PhotoImage(file=r"images\rewind.png")
b4 = Button(bottom, image=rewindPic, command=rewind, bg="white")
b4.grid(row=0, column=0)

mutePic = PhotoImage(file=r"images\mute.png")
volPic = PhotoImage(file=r"images\volume.png")
b5 = Button(bottom, image=mutePic, command=mute, bg="white")
b5.grid(row=0, column=2)

# Volume Slider

scale = Scale(bottom, orient=HORIZONTAL, command=vol)
scale.set(50)
mixer.music.set_volume(0.5)
scale.grid(row=0, column=1 ,padx=3, pady=11)

# Status Bar

sb = Label(root, text="Welcome To Nikhil Music", relief=SUNKEN, bd=1, anchor=W)
sb.pack(side=BOTTOM, fill=X)

root.mainloop()






