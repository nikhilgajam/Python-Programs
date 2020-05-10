from datetime import datetime
from tkinter import *
import threading
import time

root = Tk()
root.title("Time")
stop_threads = None

l0 = Label(root, text="", font="Verdana 16")
l0.pack()
l1 = Label(root, text="", font="Verdana 40")
l1.pack()


def time_thing():
    global stop_threads

    while TRUE:
        c = time.ctime(time.time())
        d = datetime.strptime(c[11:16], "%H:%M")
        d = d.strftime("%I:%M %p")
        d = d[:-3] + c[16:19] + d[5:]

        l1['text'] = d
        l0['text'] = " Day : " + c[:4] + "\n" + "Date : " + c[8:11] + " \t" + " Year : " + c[20:] + "\n" + "Month: " \
                     + c[4:8]

        if stop_threads is True:
            exit(t1)
            break


def ok():
    global stop_threads
    stop_threads = True
    time_thing()
    root.quit()
    exit(t1)


t1 = threading.Thread(target=time_thing)
t1.start()


root.protocol("WM_DELETE_WINDOW", ok)
root.mainloop()
