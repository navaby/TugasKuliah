import tkinter as tk
from tkinter import ttk

saved_data = []

def save_action(event=None):
    email = entry_email.get()
    nama = entry_nama.get()
    jenis = combo_jenis.get()
    
    saved_data.append((email, nama, jenis))
    
    update_treeview()
    
    action_text.config(state='normal')
    action_text.insert(tk.END, f"Data has been saved:\n- Email: {email}\n- Nama: {nama}\n- Jenis: {jenis}\n\n")
    action_text.config(state='disabled')

def update_action():
    selected_item = treeview.focus()
    if selected_item:
        email, nama, jenis = saved_data[treeview.index(selected_item)]
        
        new_email = entry_email.get() if entry_email.get() else email
        new_nama = entry_nama.get() if entry_nama.get() else nama
        new_jenis = combo_jenis.get() if combo_jenis.get() else jenis
        
        saved_data[treeview.index(selected_item)] = (new_email, new_nama, new_jenis)
        update_treeview()
        
        action_text.config(state='normal')
        action_text.insert(tk.END, f"Data has been updated to:\n- Email: {new_email}\n- Nama: {new_nama}\n- Jenis: {new_jenis}\n\n")
        action_text.config(state='disabled')
    else:
        action_text.config(state='normal')
        action_text.insert(tk.END, "Please select a row to update.\n\n")
        action_text.config(state='disabled')

def delete_action():
    selected_item = treeview.focus()
    if selected_item:
        index = treeview.index(selected_item)
        deleted_data = saved_data.pop(index)
        
        update_treeview()
        
        action_text.config(state='normal')
        action_text.insert(tk.END, f"Data has been deleted:\n- Email: {deleted_data[0]}\n- Nama: {deleted_data[1]}\n- Jenis: {deleted_data[2]}\n\n")
        action_text.config(state='disabled')
    else:
        action_text.config(state='normal')
        action_text.insert(tk.END, "Please select a row to delete.\n\n")
        action_text.config(state='disabled')

def update_treeview():
    for row in treeview.get_children():
        treeview.delete(row)
    for entry in saved_data:
        treeview.insert('', 'end', values=entry)

root = tk.Tk()
root.title("Data Entry Form")
root.geometry("600x600")
root.configure(bg="#282C34")

frame = tk.Frame(root, bg="#282C34", padx=20, pady=20)
frame.pack(pady=20, padx=20)

title_label = tk.Label(
    frame, text="Data Entry Form", font=("Helvetica", 18, "bold"),
    bg="#282C34", fg="#61AFEF"
)
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

label_email = tk.Label(frame, text="Email", bg="#282C34", fg="#98C379", font=("Helvetica", 10, "bold"))
label_email.grid(row=1, column=0, sticky="w", pady=5)
entry_email = tk.Entry(frame, width=30, bg="#3C4048", fg="white", font=("Helvetica", 10), relief="flat")
entry_email.grid(row=1, column=1, pady=5)
entry_email.bind("<Return>", save_action)

label_nama = tk.Label(frame, text="Nama", bg="#282C34", fg="#98C379", font=("Helvetica", 10, "bold"))
label_nama.grid(row=2, column=0, sticky="w", pady=5)
entry_nama = tk.Entry(frame, width=30, bg="#3C4048", fg="white", font=("Helvetica", 10), relief="flat")
entry_nama.grid(row=2, column=1, pady=5)
entry_nama.bind("<Return>", save_action)

label_jenis = tk.Label(frame, text="Jenis", bg="#282C34")