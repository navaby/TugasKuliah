saldo_rekening = 1000000  
def tampilkan_saldo():
    print(f"Saldo saat ini: Rp{saldo_rekening:,.0f}")

def tambah_saldo(jumlah):
    global saldo_rekening
    saldo_rekening += jumlah
    print(f"Saldo bertambah Rp{jumlah:,.0f}")

def kurangi_saldo(jumlah):
    global saldo_rekening
    if saldo_rekening >= jumlah:
        saldo_rekening -= jumlah
        print(f"Saldo berkurang Rp{jumlah:,.0f}")
    else:
        print("Saldo tidak mencukupi untuk penarikan ini.")


tampilkan_saldo()      
tambah_saldo(500000)   
tampilkan_saldo()      
kurangi_saldo(200000)  
tampilkan_saldo()      
