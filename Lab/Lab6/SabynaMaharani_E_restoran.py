# Fungsi mencetak informasi donat yang terjual,menambah nama donat ke list dan mengembalikan int harga donat yg terjual
def beli_nama(n):
    print(f"{n} terjual dengan harga {(dct_data[n])[0]}")
    lst_beli.append(n)
    return int((dct_data[n])[0])

# Fungsi mencetak informasi donat yang terjual,menambah nama donat ke list dan mengembalikan int harga donat yg terjual
def beli_rasa(r):
    lst_nama = [k for k, v in dct_data.items() if r in v]
    lst_harga = [int(v[0]) for k, v in dct_data.items() if r in v]
    maks_harga = max(lst_harga)
    nama = lst_nama[lst_harga.index(maks_harga)]
    lst_beli.append(nama)
    print(f"{nama} terjual dengan harga {maks_harga}")
    return int((dct_data[nama])[0])

# Meminta input jumlah donat
jumlah_donat = int(input("Masukkan Jumlah Donat DUAARRR!!!: "))

# Membuat variabel awal
dct_data = {}
lst_beli = []
pendapatan = 0

# Meminta input data donat 
for i in range(jumlah_donat):
    data = input(f"Data {i + 1}: ")
    lst_data = data.split()
    dct_data[lst_data[0]] = [lst_data[1], lst_data[2]]

# Meminta input data jumlah pembeli dan data pembelian
jumlah_pembeli = int(input("\nMasukkan Jumlah Pembeli: "))
for i in range(jumlah_pembeli):
    pembeli = input(f"Pembeli {i + 1}: ")
    beli = pembeli.split()

    # Mengatur output jika pembelian BELI_NAMA, dengan memanggil fungsi beli_nama()
    if beli[0] == "BELI_NAMA":
        if beli[1] in dct_data:
            b = beli_nama(beli[1])
            pendapatan += b
        else:
            print(f"Tidak ada Donat DUAARRR!!! dengan nama {beli[1]} :(")

    # Mengatur output jika pembelian BELI_RASA, dengan memanggil fungsi beli_rasa()
    elif beli[0] == "BELI_RASA":
        if beli[1] in [i[1] for i in dct_data.values()]:
            b = beli_rasa(beli[1])
            pendapatan += b
        else:
            print(f"Tidak ada Donat DUAARRR!!! dengan rasa {beli[1]} :(")

# Mengubah list menjadi set agar tidak ada duplikasi elemen
st_beli = set(lst_beli)

# Mencetak donat yang berhasil terjual dan total penghasilan 
print("\nDonat terjual: " + ",".join(st_beli))
print(f"Total pendapatan: {pendapatan}")
