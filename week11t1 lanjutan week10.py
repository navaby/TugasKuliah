import tkinter as tk
from tkinter import ttk

def save_action(event=None):
    email = entry_email.get()   
    nama = entry_nama.get()
    jenis = combo_jenis.get()
    action_text.config(state='normal')
    action_text.insert(tk.END, f"Data has been saved:\n- Email: {email}\n- Nama: {nama}\n- Jenis: {jenis}\n\n")
    action_text.config(state='disabled')

def update_action():
    action_text.config(state='normal')
    action_text.insert(tk.END, "Data has been updated.\n\n")
    action_text.config(state='disabled')

def delete_action():
    action_text.config(state='normal')
    lines = action_text.get("1.0", tk.END).splitlines()
    last_data_start = len(lines) - 1
    
    while last_data_start >= 0 and not lines[last_data_start].startswith("Data has been saved:"):
        last_data_start -= 1
    
    if last_data_start >= 0:
        action_text.delete(f"{last_data_start + 1}.0", tk.END)
        action_text.insert(tk.END, "Data has been deleted.\n\n")
    else:
        action_text.insert(tk.END, "No data to delete.\n\n")
    
    action_text.config(state='disabled')

root = tk.Tk()
root.title("Data Entry Form")
root.geometry("450x600")
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

label_jenis = tk.Label(frame, text="Jenis", bg="#282C34", fg="#98C379", font=("Helvetica", 10, "bold"))
label_jenis.grid(row=3, column=0, sticky="w", pady=5)
combo_jenis = ttk.Combobox(frame, width=28, state="readonly", font=("Helvetica", 10))
combo_jenis['values'] = ("Option 1", "Option 2", "Option 3")
combo_jenis.grid(row=3, column=1, pady=5)
combo_jenis.bind("<Return>", save_action)

button_frame = tk.Frame(frame, bg="#282C34")
button_frame.grid(row=4, column=0, columnspan=2, pady=20)

button_style = {"width": 10, "font": ("Helvetica", 10, "bold"), "fg": "white"}
button_save = tk.Button(button_frame, text="SAVE", command=save_action, bg="#6C757D", **button_style)
button_save.grid(row=0, column=0, padx=5)

button_update = tk.Button(button_frame, text="UPDATE", command=update_action, bg="#6C757D", **button_style)
button_update.grid(row=0, column=1, padx=5)

button_delete = tk.Button(button_frame, text="DELETE", command=delete_action, bg="#6C757D", **button_style)
button_delete.grid(row=0, column=2, padx=5)

action_text = tk.Text(frame, width=45, height=10, bg="black", fg="white", font=("Helvetica", 10), relief="flat")
action_text.grid(row=5, column=0, columnspan=2, pady=(20, 0))
action_text.insert(tk.END, "Tindakan akan muncul di sini...\n")
action_text.config(state='disabled', wrap="word")

button_subscribe = tk.Button(root, text="Subscribe", bg="#6C757D", fg="white", font=("Helvetica", 10, "bold"), width=20)
button_subscribe.pack(pady=20)

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground="#3C4048", background="#282C34", foreground="white")

root.mainloop()
