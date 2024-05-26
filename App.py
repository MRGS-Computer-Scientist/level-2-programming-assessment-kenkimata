from tkinter import *
from app_settings import *
from os import *


class App:

    def __init__(self):
        self.window = Tk()
        self.window.geometry = (str(w_width) + "x" + str(w_height))
        self.window.title = ("VisionPass")

        self.main_frame = Frame(background="black", width=w_width, height=w_height)
        self.main_frame.pack()

        self.hello_label = Label(text="Home")
        self.hello_label.place(x=10, y=10)

        self.hello_label = Label(text="Passwords")
        self.hello_label.place(x=60, y=10)

        self.hello_label = Label(text="Generator")
        self.hello_label.place(x=130, y=10)

        self.window.mainloop()

    def exit(self):
            self.window.destroy()
