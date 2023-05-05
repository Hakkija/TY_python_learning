import tkinter as tk
import hashlib
from tkinter import messagebox

# Define the correct username and hashed password
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = hashlib.sha256(b"password").hexdigest()

# Define the function to hash the password entered by the user


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Define the function to check the login credentials


def check_login(username, password):
    if username == CORRECT_USERNAME and hash_password(password) == CORRECT_PASSWORD:
        return True
    else:
        return False

# Define the function to handle the login button click


def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if check_login(username, password):
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Incorrect username or password")

# Define the function to handle the clear button click


def handle_clear():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x250")  # Set the size of the window
root.configure(bg="#F8F8FF")  # Set the background color

# Create the title label
title_label = tk.Label(root, text="Login Panel", font=(
    "Arial", 20, "bold"), fg="#2F4F4F", bg="#F8F8FF", padx=20, pady=20)
title_label.pack()

# Create the username label and text entry
username_label = tk.Label(root, text="Username", font=(
    "Arial", 12), fg="#2F4F4F", bg="#F8F8FF")
username_label.pack()
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack()

# Create the password label and text entry
password_label = tk.Label(root, text="Password", font=(
    "Arial", 12), fg="#2F4F4F", bg="#F8F8FF")
password_label.pack()
password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack()

# Create the login and clear buttons
button_frame = tk.Frame(root, bg="#F8F8FF")
button_frame.pack(pady=20)
login_button = tk.Button(button_frame, text="Login", font=(
    "Arial", 12), fg="#FFFFFF", bg="#4169E1", command=handle_login)
login_button.pack(side="left", padx=10)
clear_button = tk.Button(button_frame, text="Clear", font=(
    "Arial", 12), fg="#FFFFFF", bg="#A9A9A9", command=handle_clear)
clear_button.pack(side="right", padx=10)

# Start the main event loop
root.mainloop()
