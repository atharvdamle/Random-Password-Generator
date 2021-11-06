from tkinter import *
from password_generator import passgen
root = Tk()


def ButtonCommand():
    x = passgen(int(entry1.get()))
    disp.insert(0, x)

Label(root, text='Enter the number of characters', width = 25, borderwidth = 3).pack()
entry1 = Entry(root, width = 20)
entry1.pack()

Button(root, text='Generate Password', command = ButtonCommand).pack()

disp = Entry(root, width = 25, borderwidth = 3)
disp.pack()


root.mainloop()