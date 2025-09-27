import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_characters = letters + digits + symbols

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    if length > 3:
        password += random.choices(all_characters, k=length-3)

    random.shuffle(password)
    result_label.config(text=''.join(password))

def clear_password():
    result_label.config(text="")

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Enter Password Length:").pack(pady=10)
entry_length = tk.Entry(root)
entry_length.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)
tk.Button(root, text="Clear Password", command=clear_password).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue")
result_label.pack(pady=10)

root.mainloop()
