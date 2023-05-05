from tkinter import *
from tkinter import messagebox


def info():
    messagebox.showinfo(message="The result is" + b1["text"]*10)


window = Tk()
window.title("Click!")
b1 = Button(window, text="1", command=info)
b2 = Button(window, text="2", command=info)
b3 = Button(window, text="3", command=quit)
b1.place(x=40, y=80)
b2.place(x=90, y=80)
b3.place(x=140, y=80)
window.mainloop()
