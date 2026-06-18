import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------- GENERATE PASSWORD ---------------- #

def generate_password():

    length = password_length.get()

    if length < 4:
        messagebox.showerror(
            "Error",
            "Password length must be at least 4"
        )
        return

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check_strength()


# ---------------- CHECK PASSWORD STRENGTH ---------------- #

def check_strength(event=None):

    password = password_entry.get()

    strength = 0

    # LENGTH CHECK
    if len(password) >= 8:
        strength += 1

    # UPPERCASE CHECK
    if any(char.isupper() for char in password):
        strength += 1

    # LOWERCASE CHECK
    if any(char.islower() for char in password):
        strength += 1

    # NUMBER CHECK
    if any(char.isdigit() for char in password):
        strength += 1

    # SPECIAL CHARACTER CHECK
    if any(char in string.punctuation for char in password):
        strength += 1

    # RESULT
    if strength <= 2:
        strength_label.config(
            text="Weak Password",
            fg="red"
        )

    elif strength <= 4:
        strength_label.config(
            text="Medium Password",
            fg="orange"
        )

    else:
        strength_label.config(
            text="Strong Password",
            fg="green"
        )


# ---------------- COPY PASSWORD ---------------- #

def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "No password available"
        )

    else:
        pyperclip.copy(password)

        messagebox.showinfo(
            "Copied",
            "Password copied successfully!"
        )


# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()

root.title("Password Generator & Strength Checker")

root.geometry("500x500")

root.config(bg="#0f172a")


# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 22, "bold"),
    bg="#0f172a",
    fg="white"
)

title.pack(pady=20)


# ---------------- LENGTH LABEL ---------------- #

length_label = tk.Label(
    root,
    text="Enter Password Length",
    font=("Arial", 14),
    bg="#0f172a",
    fg="white"
)

length_label.pack(pady=5)


# ---------------- LENGTH ENTRY ---------------- #

password_length = tk.IntVar(value=12)

length_entry = tk.Entry(
    root,
    textvariable=password_length,
    font=("Arial", 14),
    width=10,
    justify="center"
)

length_entry.pack(pady=10)


# ---------------- PASSWORD ENTRY ---------------- #

password_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=30,
    justify="center"
)

password_entry.pack(pady=20)

# ENTER KEY EVENT
password_entry.bind("<Return>", check_strength)


# ---------------- GENERATE BUTTON ---------------- #

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 14, "bold"),
    bg="#22c55e",
    fg="white",
    padx=10,
    pady=5,
    command=generate_password
)

generate_btn.pack(pady=10)


# ---------------- CHECK BUTTON ---------------- #

check_btn = tk.Button(
    root,
    text="Check Strength",
    font=("Arial", 14, "bold"),
    bg="#f59e0b",
    fg="white",
    padx=10,
    pady=5,
    command=check_strength
)

check_btn.pack(pady=10)


# ---------------- COPY BUTTON ---------------- #

copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 14, "bold"),
    bg="#3b82f6",
    fg="white",
    padx=10,
    pady=5,
    command=copy_password
)

copy_btn.pack(pady=10)


# ---------------- STRENGTH LABEL ---------------- #

strength_label = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold"),
    bg="#0f172a"
)

strength_label.pack(pady=20)


# ---------------- RUN APP ---------------- #

root.mainloop()
