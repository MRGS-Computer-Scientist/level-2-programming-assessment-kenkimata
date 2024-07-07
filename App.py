from tkinter import *
import pyperclip
import random
from tkinter import messagebox
import os


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("VisionPass Version 1.01")
        self.geometry("800x300")
        self.configure(bg="black")

        # Initialize variables
        self.passwrd = StringVar()  # String variable to hold the generated password
        self.passlen = IntVar()  # Integer variable to hold the desired password length
        self.passlen.set(0)  # Default password length set to 0

        # Create the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Create the menu frame on the left side
        menubar_frame = Frame(self, bg="gray", width=200, height=300)
        menubar_frame.pack(side=LEFT, fill=Y)

        # Add button to open the password manager
        Button(
            menubar_frame,
            text="Password Manager",
            bg="gray",
            fg="white",
            width=15,
            height=2,
            command=self.open_password_manager,
        ).pack(padx=10, pady=10)

        # Create the content frame on the right side
        content_frame = Frame(self, bg="black")
        content_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Add labels, input fields, and buttons for password generation
        Label(
            content_frame,
            text="Password Generator",
            font="Courier 30 bold",
            bg="black",
            fg="white",
        ).pack()
        Label(
            content_frame,
            text="VisionPass Version 1.01",
            font="Courier 20 italic",
            bg="black",
            fg="white",
        ).pack()
        Label(content_frame, text="Password Length", bg="black", fg="white").pack(
            pady=3
        )
        Entry(content_frame, textvariable=self.passlen).pack(pady=3)
        Button(
            content_frame,
            text="Generate",
            command=self.generate_password,
            bg="gray",
            fg="white",
        ).pack(pady=7)
        Entry(content_frame, textvariable=self.passwrd).pack(pady=3)
        Button(
            content_frame,
            text="Copy Clipboard",
            command=self.copy_to_clipboard,
            bg="gray",
            fg="white",
        ).pack(pady=7)

    # Generates a random password based on the specified length
    def generate_password(self):
        try:
            length = self.passlen.get()
            if (
                length < 1 or length > 100
            ):  # Check if the password length is out of bounds
                raise ValueError
        except TclError:  # Handle non-integer input
            messagebox.showerror(
                "Error", "Please enter a valid integer for the password length"
            )
            return
        except ValueError:  # Handle invalid length
            messagebox.showerror("Error", "Password length must be 1-100 characters")
            return

        pass1 = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            " ",
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "(",
            ")",
            "-",
            "=",
            "`",
            "~",
            "{",
            "}",
            "[",
            "]",
        ]

        password = ""
        for _ in range(length):
            password += random.choice(pass1)  # Append random character to the password

        self.passwrd.set(password)  # Set the generated password

    # Copies the generated password to the clipboard
    def copy_to_clipboard(self):
        random_password = self.passwrd.get()
        pyperclip.copy(random_password)

    # Opens the password manager
    def open_password_manager(self):
        self.destroy()
        os.system("python password_manager.py")


if __name__ == "__main__":
    app = App()
    app.mainloop()
