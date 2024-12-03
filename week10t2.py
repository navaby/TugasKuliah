import tkinter as tk
from tkinter import ttk

def save_action():
    print("Data saved.")

def update_action():
    print("Data updated.")

def delete_action():
    print("Data deleted.")

root = tk.Tk()
root.title("Form Kategori")
root.geometry("400x250")
root.configure(bg="lightgrey")

frame = tk.Frame(root, bg="white", padx=10, pady=10)
frame.pack(fill="both", expand=True, padx=10, pady=10)

label_kode = tk.Label(frame, text="KODE KATEGORI", bg="white")
label_kode.grid(row=0, column=0, sticky="w", pady=5)
entry_kode = tk.Entry(frame, width=30)
entry_kode.grid(row=0, column=1, pady=5)

label_nama = tk.Label(frame, text="NAMA", bg="white")
label_nama.grid(row=1, column=0, sticky="w", pady=5)
entry_nama = tk.Entry(frame, width=30)
entry_nama.grid(row=1, column=1, pady=5)

label_jenis = tk.Label(frame, text="JENIS", bg="white")
label_jenis.grid(row=2, column=0, sticky="w", pady=5)
combo_jenis = ttk.Combobox(frame, width=28, state="readonly")
combo_jenis['values'] = ("Option 1", "Option 2", "Option 3")  
combo_jenis.grid(row=2, column=1, pady=5)

button_save = tk.Button(frame, text="SAVE", command=save_action, width=10, bg="lightgrey")
button_save.grid(row=3, column=0, pady=10)

button_update = tk.Button(frame, text="UPDATE", command=update_action, width=10, bg="lightgrey")
button_update.grid(row=3, column=1, pady=10, sticky="w")

button_delete = tk.Button(frame, text="DELETE", command=delete_action, width=10, bg="lightgrey")
button_delete.grid(row=3, column=1, pady=10, sticky="e")

text_output = tk.Text(frame, width=40, height=5)
text_output.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
