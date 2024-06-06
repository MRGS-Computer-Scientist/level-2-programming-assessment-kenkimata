from tkinter import *
import os

class PasswordManager(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry("800x300")
        self.configure(bg='black')

        self.passwords = []
        self.create_widgets()

    def create_widgets(self):
        # Create the frame that acts like a menubar
        menubar_frame = Frame(self, bg='gray', width=200, height=300)
        menubar_frame.pack(side=LEFT, fill=Y)

        # Add buttons to the menu frame
        Button(menubar_frame, text="Password Generator", bg='gray', fg='white', width=15, height=2, command=self.open_password_generator).pack(padx=10, pady=10)

        # Main content frame
        content_frame = Frame(self, bg='black')
        content_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        Label(content_frame, text="Password Manager", font="Courier 30 bold", bg='black', fg='white').pack(pady=10)
        Label(content_frame, text="Manage your passwords here", font="Courier 20 italic", bg='black', fg='white').pack(pady=10)

        # Frame for managing passwords
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

        self.password_list_frame = Frame(content_frame, bg='black')
        self.password_list_frame.pack(fill=BOTH, expand=True)

    def add_password(self):
        site = self.site_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if site and username and password:
            self.passwords.append((site, username, password))
            self.site_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def view_passwords(self):
        for widget in self.password_list_frame.winfo_children():
            widget.destroy()

        for idx, (site, username, password) in enumerate(self.passwords):
            Label(self.password_list_frame, text=f"{idx+1}. {site} - {username} - {password}", bg='black', fg='white').pack(anchor='w')

    def open_password_generator(self):
        self.destroy()
        os.system('python app.py')

if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.mainloop()
