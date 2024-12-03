import tkinter as tk
from tkinter import messagebox

karyawan = ["budi", "bunga", "alex", "mawar", "dani", "sultan", "Ganda"]

def cek_status_karyawan(event=None):
    nama = entry_nama.get().strip().lower()
    if nama in karyawan:
        messagebox.showinfo("Hasil", f"{nama.capitalize()} adalah Karyawan.")
    else:
        messagebox.showinfo("Hasil", f"{nama.capitalize()} Bukan Karyawan.")

root = tk.Tk()
root.title("Cek Status Karyawan")

label = tk.Label(root, text="Masukkan Nama:", font=("Arial", 12))
label.pack(pady=10)

entry_nama = tk.Entry(root, font=("Arial", 12))
entry_nama.pack(pady=5)
entry_nama.bind("<Return>", cek_status_karyawan)

btn_cek = tk.Button(root, text="Cek Status", font=("Arial", 12), command=cek_status_karyawan)
btn_cek.pack(pady=10)

entry_nama.focus()
root.mainloop()
