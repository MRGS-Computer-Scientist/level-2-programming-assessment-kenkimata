from tkinter import *
from app_settings import *

class App():

    def __init__(self):
        window = Tk()
        window.geometry(str(w_width) + "x" + str(w_height))
        window.title("VisionPass")

        main_frame = Frame(background="black", width=w_width, height=w_height)
        main_frame.pack()

        hello_label = Label(text="Home")
        hello_label.place(x=10, y=10)

        hello_label = Label(text="Passwords")
        hello_label.place(x=60, y=10)

        hello_label = Label(text="Generator")
        hello_label.place(x=130, y=10)

        window.mainloop()