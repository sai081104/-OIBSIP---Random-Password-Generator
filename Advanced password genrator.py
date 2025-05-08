import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    """Generate a random password based on user-selected criteria."""
    length = length_var.get()

    if length <= 0:
        messagebox.showerror("Error", "Password length must be positive.")
        return

    characters = ""
    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "No character set selected!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    """Copy the generated password to clipboard."""
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
app = tk.Tk()
app.title("Random Password Generator")
app.geometry("400x300")

# Variables
length_var = tk.IntVar()
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

# Widgets
tk.Label(app, text="Password Length:").pack(pady=5)
tk.Entry(app, textvariable=length_var).pack(pady=5)

tk.Checkbutton(app, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(app, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(app, text="Include Symbols", variable=symbols_var).pack()

tk.Button(app, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(app, font=("Arial", 14), width=30)
password_entry.pack(pady=5)

tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

app.mainloop()

