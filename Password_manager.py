import os
import json
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet

PASSWORDS_FILE = "passwords.json"
KEY_FILE = "secret.key"

# Creates a new encryption key if it doesn't already exist, or loads the existing key from a file. Returns the encryption key.
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return key

# Encrypts the password using the provided key and returns the encrypted password.
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password.decode()

# Decrypts the encrypted password using the provided key and returns the decrypted password.
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password.encode())
    return decrypted_password.decode()

class PasswordManager(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry("800x400")
        self.configure(bg='black')

        self.key = load_key()  # Load the encryption key
        self.passwords = self.load_passwords()  # Load existing passwords
        self.create_widgets()  # Create the GUI components

    def create_widgets(self):
        # Create the menu frame on the left side
        menubar_frame = Frame(self, bg='gray', width=200, height=400)
        menubar_frame.pack(side=LEFT, fill=Y)

        # Add button to open the password generator
        Button(menubar_frame, text="Password Generator", bg='gray', fg='white', width=15, height=2, command=self.open_password_generator).pack(padx=10, pady=10)

        # Create the content frame on the right side
        content_frame = Frame(self, bg='black')
        content_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Add labels and input fields for managing passwords
        Label(content_frame, text="Password Manager", font="Courier 30 bold", bg='black', fg='white').pack(pady=10)
        Label(content_frame, text="Manage your passwords here", font="Courier 20 italic", bg='black', fg='white').pack(pady=10)

        manage_frame = Frame(content_frame, bg='black')
        manage_frame.pack(pady=20)

        Label(manage_frame, text="Site", bg='black', fg='white').grid(row=0, column=0, padx=5)
        Label(manage_frame, text="Username", bg='black', fg='white').grid(row=0, column=1, padx=5)
        Label(manage_frame, text="Password", bg='black', fg='white').grid(row=0, column=2, padx=5)

        self.site_entry = Entry(manage_frame)
        self.site_entry.grid(row=1, column=0, padx=5)
        self.username_entry = Entry(manage_frame)
        self.username_entry.grid(row=1, column=1, padx=5)
        self.password_entry = Entry(manage_frame)
        self.password_entry.grid(row=1, column=2, padx=5)

        Button(manage_frame, text="Add", command=self.add_password, bg='gray', fg='white').grid(row=1, column=3, padx=5)
        Button(manage_frame, text="View", command=self.view_passwords, bg='gray', fg='white').grid(row=2, column=0, columnspan=4, pady=5)

        # Create a canvas and scrollbar for viewing passwords
        self.canvas = Canvas(content_frame, bg='black')
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = Scrollbar(content_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.scrollable_frame = Frame(self.canvas, bg='black')
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

    # Adds a new password to the list and encrypts it before saving
    def add_password(self):
        site = self.site_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if site and username and password:
            encrypted_password = encrypt_password(password, self.key)
            self.passwords.append({"site": site, "username": username, "password": encrypted_password})
            self.save_passwords()
            self.site_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.view_passwords()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    # Displays all saved passwords in a scrollable frame
    def view_passwords(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for idx, entry in enumerate(self.passwords):
            try:
                decrypted_password = decrypt_password(entry['password'], self.key)
                Label(self.scrollable_frame, text=f"{idx+1}. {entry['site']} - {entry['username']} - {decrypted_password}", bg='black', fg='white').pack(anchor='w')
            except Exception as e:
                print(f"Failed to decrypt password for '{entry['site']}': {e}")

    # Loads passwords from a file if it exists
    def load_passwords(self):
        if os.path.exists(PASSWORDS_FILE):
            with open(PASSWORDS_FILE, "r") as file:
                return json.load(file)
        return []

    # Saves passwords to a file
    def save_passwords(self):
        with open(PASSWORDS_FILE, "w") as file:
            json.dump(self.passwords, file)

    # Opens the password generator
    def open_password_generator(self):
        self.destroy()
        os.system('python app.py')

if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.mainloop()
