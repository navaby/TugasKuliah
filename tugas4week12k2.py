import tkinter as tk
from tkinter import messagebox

karyawan = ["budi", "bunga", "alex", "mawar", "dani", "sultan"]

def cek_status_karyawan(event=None):
    nama = entry_nama.get().strip().lower()
    if nama in karyawan:
        result_label.config(text=f"{nama.capitalize()} adalah Karyawan.", fg="green")
    else:
        result_label.config(text=f"{nama.capitalize()} Bukan Karyawan.", fg="red")

root = tk.Tk()
root.title("Status Karyawan")
root.geometry("400x300")
root.configure(bg="#f0f8ff")  

header_label = tk.Label(root, text="Cek Status Karyawan", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#2c3e50")
header_label.pack(pady=20)

input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

entry_label = tk.Label(input_frame, text="Masukkan Nama:", font=("Arial", 12), bg="#f0f8ff", fg="#34495e")
entry_label.grid(row=0, column=0, padx=5)

entry_nama = tk.Entry(input_frame, font=("Arial", 12), width=20)
entry_nama.grid(row=0, column=1, padx=5)
entry_nama.bind("<Return>", cek_status_karyawan)

btn_cek = tk.Button(root, text="Cek Status", font=("Arial", 12), bg="#2980b9", fg="white", command=cek_status_karyawan)
btn_cek.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff", fg="#2c3e50")
result_label.pack(pady=20)

entry_nama.focus()
root.mainloop()
