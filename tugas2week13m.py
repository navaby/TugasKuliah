import tkinter as tk
from tkinter import ttk, messagebox

customer_data = []

def tambah_data():
    kode = kode_entry.get()
    nama = nama_entry.get()
    jenis_kelamin = gender_var.get()
    alamat = alamat_combo.get()

    if not (kode and nama and jenis_kelamin and alamat):
        messagebox.showwarning("Warning", "All fields must be filled!")
        return

    customer_data.append((kode, nama, jenis_kelamin, alamat))
    update_tabel()
    bersihkan_form()

def hapus_data():
    selected_item = tabel.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select data to delete!")
        return

    for item in selected_item:
        index = tabel.index(item)
        customer_data.pop(index)
    update_tabel()

def bersihkan_form():
    kode_entry.delete(0, tk.END)
    nama_entry.delete(0, tk.END)
    gender_var.set("")
    alamat_combo.set("")

def update_tabel():
    tabel.delete(*tabel.get_children())
    for item in customer_data:
        tabel.insert("", tk.END, values=item)

root = tk.Tk()
root.title("Customer Management System")
root.geometry("600x400")
root.configure(bg="#1a237e")  

input_frame = tk.Frame(root, bg="#1a237e")
input_frame.pack(pady=10)

label_font = ("Arial", 10, "bold")
entry_font = ("Arial", 10)

label_fg = "#e3f2fd"  
tk.Label(input_frame, text="Customer Code:", fg=label_fg, bg="#1a237e", font=label_font).grid(row=0, column=0, sticky="w", padx=5, pady=5)
kode_entry = tk.Entry(input_frame, font=entry_font, bg="#283593", fg="white", insertbackground="white")
kode_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Customer Name:", fg=label_fg, bg="#1a237e", font=label_font).grid(row=1, column=0, sticky="w", padx=5, pady=5)
nama_entry = tk.Entry(input_frame, font=entry_font, bg="#283593", fg="white", insertbackground="white")
nama_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Gender:", fg=label_fg, bg="#1a237e", font=label_font).grid(row=2, column=0, sticky="w", padx=5, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(input_frame, text="Male", variable=gender_var, value="Male", fg=label_fg, bg="#1a237e", font=entry_font, selectcolor="#283593").grid(row=2, column=1, sticky="w")
tk.Radiobutton(input_frame, text="Female", variable=gender_var, value="Female", fg=label_fg, bg="#1a237e", font=entry_font, selectcolor="#283593").grid(row=2, column=2, sticky="w")

tk.Label(input_frame, text="Address:", fg=label_fg, bg="#1a237e", font=label_font).grid(row=3, column=0, sticky="w", padx=5, pady=5)
alamat_combo = ttk.Combobox(input_frame, values=["Batam", "Karimun", "Tj Pinang", "Bintan", "Lingga", "Bekasi"], state="readonly", font=entry_font)
alamat_combo.grid(row=3, column=1, padx=5, pady=5)

button_frame = tk.Frame(root, bg="#1a237e")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", command=tambah_data, bg="#283593", fg="white", font=label_font).pack(side="left", padx=5)
tk.Button(button_frame, text="Delete", command=hapus_data, bg="#283593", fg="white", font=label_font).pack(side="left", padx=5)
tk.Button(button_frame, text="Clear", command=bersihkan_form, bg="#283593", fg="white", font=label_font).pack(side="left", padx=5)

tabel_frame = tk.Frame(root, bg="#1a237e")
tabel_frame.pack(fill="both", expand=True, padx=10, pady=10)

style = ttk.Style()
style.configure("Treeview", 
                background="#bdbdbd",  
                foreground="black",   
                rowheight=25,
                fieldbackground="#bdbdbd",  
                font=("Arial", 10))
style.configure("Treeview.Heading", 
                background="#616161",  
                foreground="black", 
                font=("Arial", 10, "bold"))
style.map("Treeview", background=[("selected", "#757575")])  

tabel = ttk.Treeview(tabel_frame, columns=("Code", "Name", "Gender", "Address"), show="headings")
tabel.heading("Code", text="Customer Code")
tabel.heading("Name", text="Customer Name")
tabel.heading("Gender", text="Gender")
tabel.heading("Address", text="Address")

tabel.column("Code", width=120, anchor="center")
tabel.column("Name", width=150, anchor="center")
tabel.column("Gender", width=100, anchor="center")
tabel.column("Address", width=150, anchor="center")

scrollbar = ttk.Scrollbar(tabel_frame, orient="vertical", command=tabel.yview)
tabel.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

tabel.pack(fill="both", expand=True)

root.mainloop()
