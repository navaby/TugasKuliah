def proses_pesanan(nama, barang, harga, diskon=0):
    total_harga = sum(harga)
    
    if diskon > 0:
        total_harga -= total_harga * (diskon / 100)
    
    pajak = total_harga * 0.10
    total_harga += pajak
    
    print("Ringkasan Pesanan")
    print(f"Nama Pelanggan: {nama}")
    print("Daftar Barang yang Dibeli:")
    for i, item in enumerate(barang):
        print(f"- {item}: Rp{harga[i]:,.0f}")
    print(f"Diskon: {diskon}%")
    print(f"Pajak (10%): Rp{pajak:,.0f}")
    print(f"Total Harga: Rp{total_harga:,.0f}")

barang = ["laptop", "mouse", "keyboard"]
harga = [8000000, 30000, 50000]  

proses_pesanan("Syaeful", barang, harga, diskon=10)
