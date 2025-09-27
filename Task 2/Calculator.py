import tkinter as tk
from tkinter import messagebox

def press(key):
    entry_var.set(entry_var.get() + str(key))

def clear():
    entry_var.set("")

def cancel():
    entry_var.set(entry_var.get()[:-1])

def calculate():
    try:
        ans = str(eval(entry_var.get()))
        entry_var.set(ans)
    except:
        messagebox.showerror("Error","Invalid Input")

def enter(e):
    e.widget['background'] = "#444"

def leave(e):
    e.widget['background'] = e.widget.default_bg

root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.config(bg="#222")
root.resizable(False, False)

entry_var = tk.StringVar()

entry= tk.Entry(root, textvariable=entry_var, font=("Arial",20),
                 bd=5, relief="flat", justify="right",
                 bg="#111", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10, padx=10, sticky="nsew")


buttons = [
    ["7",  "8",  "9",  "/"],
    ["4",  "5",  "6",  "*"],
    ["1",  "2",  "3",  "-"],
    ["0",  ".",  "+",  "="],
    ["Clear"," X "]
]


btn_style = {"font":("Arial",16,"bold"),
             "relief":"flat",
             "fg":"white",
             "activebackground":"#555",
             "activeforeground":"white"}

for r in range(len(buttons)):
    for c in range(len(buttons[r])):
        text = buttons[r][c]
        if text == "=":
            btn = tk.Button(root, text=text, command=calculate, bg="#0066cc", **btn_style)
        elif text == "Clear":
            btn = tk.Button(root, text=text, command=clear, bg="#cc3300", **btn_style)
        elif text == " X ":
            btn = tk.Button(root, text=text, command=cancel , bg="#cc3300", **btn_style)
        else:
            btn = tk.Button(root, text=text, command=lambda t=text: press(t), bg="#333", **btn_style)

        btn.grid(row=r+1, column=c, padx=5, pady=5, sticky="nsew")
        btn.default_bg = btn["bg"]
        btn.bind("<Enter>", enter)
        btn.bind("<Leave>", leave)


for i in range(6):
    root.grid_rowconfigure(i,weight=1)

for j in range(4):
    root.grid_columnconfigure(j,weight=1)

root.mainloop()
