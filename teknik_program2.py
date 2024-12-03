import math

# Input jari-jari lingkaran
r = float(input("Masukkan jari-jari lingkaran (r): "))

# Hitung luas lingkaran
luas = math.pi * r**2

# Hitung keliling lingkaran
keliling = 2 * math.pi * r

# Output luas dan keliling
print("Luas lingkaran:", luas)
print("Keliling lingkaran:", keliling)