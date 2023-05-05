from tkinter import *
window = Tk()
window.title("Area")
area = Canvas(window, width=600, height=600)
area.pack()
area.create_rectangle(50, 50, 200, 200, fill="green")
window.mainloop()
