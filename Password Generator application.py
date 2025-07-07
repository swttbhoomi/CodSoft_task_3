import tkinter as tk
from tkinter import messagebox
import random
import string
import re

FONT = ("Arial", 14)

def update_mode():
    if mode_var.get() == "generate":
        entry_password.config(state="readonly")
        btn_generate.config(state="normal")
        password_var.set("")
        reenter_var.set("")
    else:
        entry_password.config(state="normal")
        btn_generate.config(state="disabled")
        password_var.set("")
        reenter_var.set("")

def generate_password():
    try:
        length = int(length_var.get())
        if length < 6:
            messagebox.showerror("Error", "Password length should be at least 6.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    chars = ""
    if var_lower.get():
        chars += string.ascii_lowercase
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_digits.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Select at least one character set.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def is_valid_password(pw):
    if len(pw) < 8:
        return False
    if not re.search(r'[a-z]', pw):
        return False
    if not re.search(r'[A-Z]', pw):
        return False
    if not re.search(r'\d', pw):
        return False
    if not re.search(r'[^A-Za-z0-9]', pw):
        return False
    return True

def verify_password():
    if mode_var.get() == "manual":
        pw = password_var.get()
        if not is_valid_password(pw):
            messagebox.showerror(
                "Invalid password",
                "Password must be at least 8 characters and include a lowercase letter, uppercase letter, digit, and special character."
            )
            return
    if password_var.get() == reenter_var.get():
        messagebox.showinfo("Success", "Password verified successfully!")
    else:
        messagebox.showerror("Error", "Passwords do not match.")

root = tk.Tk()
root.title("Password Generator")

mode_var = tk.StringVar(value="generate")

tk.Label(root, text="Choose mode:", font=FONT).grid(row=0, column=0, sticky="w")
tk.Radiobutton(root, text="Generate password for me", variable=mode_var, value="generate", command=update_mode, font=FONT).grid(row=0, column=1, sticky="w")
tk.Radiobutton(root, text="Let me enter my own password", variable=mode_var, value="manual", command=update_mode, font=FONT).grid(row=0, column=2, sticky="w")

tk.Label(root, text="Password Length:", font=FONT).grid(row=1, column=0, sticky="e")
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var, width=5, font=FONT).grid(row=1, column=1, sticky="w")

var_lower = tk.BooleanVar(value=True)
var_upper = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Lowercase", variable=var_lower, font=FONT).grid(row=2, column=0, sticky="w")
tk.Checkbutton(root, text="Uppercase", variable=var_upper, font=FONT).grid(row=2, column=1, sticky="w")
tk.Checkbutton(root, text="Digits", variable=var_digits, font=FONT).grid(row=3, column=0, sticky="w")
tk.Checkbutton(root, text="Symbols", variable=var_symbols, font=FONT).grid(row=3, column=1, sticky="w")

btn_generate = tk.Button(root, text="Generate Password", command=generate_password, font=FONT)
btn_generate.grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(root, text="Password:", font=FONT).grid(row=5, column=0, sticky="e")
password_var = tk.StringVar()
entry_password = tk.Entry(root, textvariable=password_var, width=30, state="readonly", font=FONT)
entry_password.grid(row=5, column=1, sticky="w")

tk.Label(root, text="Re-enter Password:", font=FONT).grid(row=6, column=0, sticky="e")
reenter_var = tk.StringVar()
tk.Entry(root, textvariable=reenter_var, width=30, show="*", font=FONT).grid(row=6, column=1, sticky="w")

tk.Button(root, text="Verify Password", command=verify_password, font=FONT).grid(row=7, column=0, columnspan=2, pady=5)

update_mode()  # Set initial state

root.mainloop()
