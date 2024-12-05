import tkinter as tk
from tkinter import messagebox

def login(event=None):
    email = email_entry.get()
    password = password_entry.get()
    if email == "test@example.com" and password == "password123":
        messagebox.showinfo("Login Successful", f"Welcome, {email}!")
    else:
        messagebox.showerror("Login Failed", "Invalid email or password. Please try again.")

root = tk.Tk()
root.title("Login")
root.geometry("300x200")
root.configure(bg="#d3d3d3")  

email_label = tk.Label(root, text="Email address:", bg="#d3d3d3")
email_label.pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:", bg="#d3d3d3")
password_label.pack(pady=5)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Login", command=login, bg="#007bff", fg="white", width=20)
login_button.pack(pady=20)

root.bind('<Return>', login)

root.mainloop()
