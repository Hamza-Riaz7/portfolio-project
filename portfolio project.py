import tkinter as tk
from tkinter import messagebox
from functools import partial
from cryptography.fernet import Fernet


def store_password():
    appname = appname_entry.get()
    username = username_entry.get()
    old_password = old_password_entry.get()
    new_password = new_password_entry.get()

    if not appname or not username or not old_password or not new_password:
        messagebox.showerror("Error", "Please fill all the fields")
        return

    # Save passwords into a text file
    with open("Passwords.txt", "a") as file:
        file.write(f"app_name: {appname}\n")
        file.write(f"username: {username}\n")
        file.write(f"old_password: {old_password}\n")
        file.write(f"new_password: {new_password}\n\n")

    appname_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    old_password_entry.delete(0, tk.END)
    new_password_entry.delete(0, tk.END)

    messagebox.showinfo("Password Saved", "Password has been saved successfully.")

def second_window():
    second_window = tk.Toplevel(screen)
    second_window.title("password Manager")
    second_window.geometry("250x150")

    # Buttons
    app_name_button = tk.Button(second_window, text="App Name")
    app_name_button.pack(padx=2, pady=2)

    username_button = tk.Button(second_window, text="Username")
    username_button.pack(padx=2, pady=2)

    password_button = tk.Button(second_window, text="Password")
    password_button.pack(padx=2, pady=2)

    generate_pass_button = tk.Button(second_window, text="Generate Password")
    generate_pass_button.pack()

    back_button = tk.Button(second_window, text="Back")
    back_button.pack(padx=2, pady=2)

    save_button = tk.Button(second_window, text="Save")
    save_button.pack(padx=2, pady=2)

    label = tk.Label(second_window)
    label.pack()

def update_password():
    app_name = appname_entry.get()
    username = username_entry.get()
    new_password = new_password_entry.get()

    if not app_name or not username or not new_password:
        messagebox.showerror("Error", "Please fill all the fields")
        return

    updated_password = False
    updated_entries = []

    with open("passwords.txt", "r") as file:
        lines = file.readlines()

    with open("passwords.txt", "w") as file:
        for i in range(0, len(lines), 4):
            app = lines[i].strip().split(":")[1].strip()
            user = lines[i + 1].strip().split(":")[1].strip()
            pwd = lines[i + 2].strip().split(":")[1].strip()
            if app == app_name and user == username:
                updated_entries.extend([f"App Name: {app_name}\n", f"Username: {username}\n", f"Password: {new_password}\n\n"])
                updated_password = True
            else:
                updated_entries.extend([f"App Name: {app}\n", f"Username: {user}\n", f"Password: {pwd}\n\n"])

        file.writelines(updated_entries)

    if updated_password:
        messagebox.showinfo("Success", "Password updated successfully.")
    else:
        messagebox.showerror("Error", "App and username combination not found.")
    
    
    
    

   

def retrieve_password():
    passwords = ""
    try:
        with open("passwords.txt", "r") as file:
            passwords = file.read()
    except FileNotFoundError:
        passwords = "Password file not found."

    # Display the passwords in a message box
    messagebox.showinfo("Stored Passwords", passwords)
    # retrieve_password = tk.Toplevel(screen)
    retrieve_password.title("Retrieve Password")
    retrieve_password.geometry("200x200")

    label = tk.Label(screen)
    label.pack()

# Create the main window
screen = tk.Tk()
screen.title("password Manager")
screen.geometry("200x200")

# Labelling part
appname_label = tk.Label(screen, text="App")
appname_label.pack(padx=5, pady=5)
appname_entry = tk.Entry(screen)
appname_entry.pack(padx=5, pady=5)

username_label = tk.Label(screen, text="Username")
username_label.pack(padx=5, pady=5)
username_entry = tk.Entry(screen)
username_entry.pack(padx=5, pady=5)

old_password_label = tk.Label(screen, text="Old Password:")
old_password_label.pack(padx=5, pady=5)
old_password_entry = tk.Entry(screen, show="*")
old_password_entry.pack(padx=5, pady=5)

new_password_label = tk.Label(screen, text="New Password")
new_password_label.pack(padx=5, pady=5)
new_password_entry = tk.Entry(screen, show="*")
new_password_entry.pack(padx=5, pady=5)

# Making buttons
save_button = tk.Button(screen, text="Save Password", command=store_password)
save_button.pack()

retrieve_button = tk.Button(screen, text="Retrieve Password", command=retrieve_password)
retrieve_button.pack()

update_button = tk.Button(screen, text="Update Password", command=update_password)
update_button.pack()

exit_button = tk.Button(screen, text="Exit", command=exit)
exit_button.pack()

screen.mainloop()