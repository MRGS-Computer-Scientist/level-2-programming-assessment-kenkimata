# File: App.py

from tkinter import *
import pyperclip
import random

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("VisionPass Version 1.01")
        self.geometry("800x300")
        self.configure(bg='black')

        self.passwrd = StringVar()
        self.passlen = IntVar()
        self.passlen.set(0)

        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Password Generator", font="Courier 30 bold", bg='black', fg='white').pack()
        Label(self, text="VisionPass Version 1.01", font="Courier 20 italic", bg='black', fg='white').pack()
        Label(self, text="Enter the number to get password", bg='black', fg='white').pack(pady=3)
        Entry(self, textvariable=self.passlen).pack(pady=3)
        Button(self, text="Tap to get", command=self.generate_password, bg='gray', fg='white').pack(pady=7)
        Entry(self, textvariable=self.passwrd).pack(pady=3)
        Button(self, text="Tap to copy clipboard", command=self.copy_to_clipboard, bg='gray', fg='white').pack(side=RIGHT, padx=10)
        Button(self, text="BROOO", bg='gray', fg='white').pack(side=LEFT, padx=1)

    def generate_password(self):
        pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
                 '*', '(', ')', '-', '=', '`', '~', '{', '}', '[',
                 ']', ]
        password = ""
        for x in range(self.passlen.get()):
            password = password + random.choice(pass1)
        self.passwrd.set(password)

    def copy_to_clipboard(self):
        random_password = self.passwrd.get()
        pyperclip.copy(random_password)