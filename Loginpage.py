import tkinter as tk
from tkinter import *
from tkinter import messagebox

def ok():
    username = e1.get()
    password = e2.get()
    if username == "" and password == "":
        messagebox.showinfo("", "Blank not allowed")
    elif username == "Admin" and password == "1234":
        messagebox.showinfo("", "Login Successful")
        root.destroy()
    else:
        messagebox.showinfo("", "Invalid credentials")

root = tk.Tk()
root.title("Login page")
root.geometry("500x500")

e1 = tk.StringVar()
e2 = tk.StringVar()

tk.Label(root, text="Username").place(x=10, y=10)
tk.Label(root, text="Password").place(x=10, y=40)
tk.Entry(root, textvariable=e1).place(x=80, y=10)
tk.Entry(root, textvariable=e2, show="*").place(x=80, y=40)

tk.Button(root, text="Login", height=2, width=8,command=ok).place(x=10, y=100)

root.mainloop()
