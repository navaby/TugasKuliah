total_belanja = float(input("Masukkan total belanja Anda: Rp "))

if total_belanja > 500000:
    diskon = 0.07  
    bonus = "Mug Cantik"
elif 100000 <= total_belanja <= 499000:
    diskon = 0.05  
    bonus = "Coca Cola"
else:
    diskon = 0.0  
    bonus = "Kupon Potongan Belanja"

jumlah_diskon = total_belanja * diskon
total_setelah_diskon = total_belanja - jumlah_diskon

print(f"\nTotal belanja Anda: Rp {total_belanja:,.0f}")
if diskon > 0:
    print(f"Diskon: {diskon * 100}% (Rp {jumlah_diskon:,.0f})")
else:
    print("Diskon: Tidak ada")

print(f"Total setelah diskon: Rp {total_setelah_diskon:,.0f}")
print(f"Bonus: {bonus}")
