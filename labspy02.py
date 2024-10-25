# Program untuk menentukan bilangan terbesar dari tiga bilangan
# Meminta input tiga bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

# Menggunakan if untuk mencari bilangan terbesar
if a > b and a > c:
    terbesar = a
elif b > a and b > c:
    terbesar = b
else:
    terbesar = c

# Menampilkan bilangan terbesar
print("Bilangan terbesar adalah:", terbesar)
