belanja = float(input("Masukan jumlah diskon: "))

if belanja > 300:
    diskon = 0.15 * belanja 
    total_bayar = belanja - diskon
    print(f"Budi mendapat diskon 15%. Rp {diskon:2f}")
else:
    diskon = 0
    total_bayar = belanja
    print("Budi tidak mendapat diskon.")
print(f"Total yang harus di bayar: Rp {total_bayar:.2f}")