# List daftar_keranjang untuk menyimpan semua keranjang
daftar_keranjang = []

# Mengatur fungsi sesuai operasi
def beli_keranjang(nama_keranjang, kapasitas_keranjang):
    daftar_keranjang.append([nama_keranjang, kapasitas_keranjang])
    print("Berhasil menambahkan", nama_keranjang, "dengan kapasitas", kapasitas_keranjang)


def jual_keranjang(indeks):
    print("Berhasil menjual", daftar_keranjang[indeks][0], "yang memiliki kapasitas sebesar",
          daftar_keranjang[indeks][1])
    daftar_keranjang.pop(indeks)


def ubah_kapasitas(indeks, kapasitas_baru):
    daftar_keranjang[indeks][1] = kapasitas_baru
    print("Berhasil mengubah kapasitas", daftar_keranjang[indeks][0], "menjadi", kapasitas_baru)


def ubah_nama(indeks, nama_baru):
    nama_lama = daftar_keranjang[indeks][0]
    daftar_keranjang[indeks][0] = nama_baru
    print("Berhasil mengubah nama", nama_lama, "menjadi", nama_baru)


def lihat(indeks):
    print("Keranjang", daftar_keranjang[indeks][0], "memiliki kapasitas sebesar", daftar_keranjang[indeks][1])


def lihat_semua():
    print("---------------------------")
    for keranjang in daftar_keranjang:
        print("{:<20s} {} {}".format(keranjang[0], "|", keranjang[1]))


def total_kapasitas():
    kapasitas = 0
    for n in range(0, len(daftar_keranjang)):
        kapasitas += int(daftar_keranjang[n][1])
    print("Total kapasitas keranjang Dek Depe adalah", kapasitas)
    # return 0


# Mengatur inti program
jumlah_operasi = int(input("Masukkan banyak operasi: "))
for i in range(jumlah_operasi):
    i += 1
    # Meminta input operasi,memecah input menjadi dalam suatu list dan mengassign list ke variabel
    operasi = input("Operasi " + str(i) + ": ")
    list_operasi = operasi.split()

    # Memanggil fungsi sesuai dengan operasi pada input
    if list_operasi[0] == "BELI":
        beli_keranjang(list_operasi[1], list_operasi[2])

    elif list_operasi[0] == "JUAL":
        jual_keranjang(int(list_operasi[1]))

    elif list_operasi[0] == "UBAH_KAPASITAS":
        ubah_kapasitas(int(list_operasi[1]), list_operasi[2])

    elif list_operasi[0] == "UBAH_NAMA":
        ubah_nama(int(list_operasi[1]), list_operasi[2])

    elif list_operasi[0] == "LIHAT":
        lihat(int(list_operasi[1]))

    elif list_operasi[0] == "LIHAT_SEMUA":
        lihat_semua()

    else:
        total_kapasitas()
