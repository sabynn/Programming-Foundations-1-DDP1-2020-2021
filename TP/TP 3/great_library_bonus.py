# Assign variabel awal
rak = {}
buku = {}
tambahan = 0
tup_perintah = ("ADD RAK", "ADD BUKU", "MOVE BUKU", "SEARCH BUKU", "EXIT", "REMOVE RAK")

# Fungsi untuk penambahan rak
def add_rak(ar):
    # mengecek kevalidan nama rak
    if ar == "null":
        print("Nama rak tidak valid")
    # menambahkan rak ke dict rak jika rak belum terdapat dalam dict rak
    elif ar not in rak:
        rak[ar] = []
        print(f"Rak dengan nama {ar} berhasil ditambahkan")
    else:
        print(f"Rak dengan nama {ar} sudah ada di dalam sistem")

# Fungsi untuk penambahan buku
def add_buku(ab):
    # mengecek kevalidan nama buku
    if ab[1] == "null":
        print("Nama buku tidak valid")
    # mengecek apakah buku sudah ada di rak
    elif ab[1] not in buku:
        # membuat rak jika rak belum ada dalam dict rak
        if ab[0] not in rak:
            add_rak(ab[0])
        # memanggil fungsi kapasitas() untuk mengecek kapasitas rak
        ab[0] = kapasitas(ab[0])
        # menambahkan buku sebagai value dari key rak yang diinput dalam dict rak
        rak[ab[0]].append(ab[1])
        # menambahkan nama buku sebagai key, dan menambahkan detail buku sebagai value ke dict buku
        buku[ab[1]] = ab[2:]

        detail_buku = [ab[1]] + ab[3:]
        detail_buku = ", ".join(detail_buku)
        print(f"Buku ditambahkan pada {ab[0]}")
        print(f"Buku dengan nama {detail_buku} berhasil ditambahkan")
    else:
        print(f"Buku dengan nama {ab[1]} sudah ada di dalam sistem")

# Fungsi untuk memindahkan buku
def move_buku(m):
    # mengecek apakah buku sudah ada dalam rak
    if m[0] in buku:
        # membuat rak jika rak belum ada dalam dict rak
        if m[1] not in rak:
            add_rak(m[1])

        # menghapus buku dari rak lama
        rak_lama = "".join([k for k, v in rak.items() if m[0] in v])
        rak[rak_lama].remove(m[0])

        m[1] = kapasitas(m[1])

        # menambahkan buku ke rak yang diinput
        rak[m[1]].append(m[0])
        print(f"Buku ditambahkan pada {m[1]}")

        if rak_lama == m[1]:
            print(f"Buku dengan nama {m[0]} tidak jadi dipindahkan dari rak dengan nama {rak_lama}")
        else:
            print(f"Buku dengan nama {m[0]} dipindahkan dari rak dengan nama {rak_lama} ke rak dengan nama {m[1]}")
    else:
        print(f"Buku dengan nama {m[0]} tidak ditemukan")


# Fungsi untuk mencari buku dan mencetak detail buku menggunakan rekursi
def search_buku(s, b=0, r=0):
    lst_buku = list(buku.keys())
    lst_rak = list(rak.keys())
    if b < len(lst_buku):
        # mengecek apakah sudah ditemukan buku yang sesuai dengan nama buku yg diinput
        if s == lst_buku[b]:
            book = buku[s]
            # mengecek keberadaan buku pada rak untuk menentukan nama rak tempat buku disimpan
            if s in rak[lst_rak[r]]:
                rak_buku = lst_rak[r]
                info_buku = f"Posisi {rak_buku}\nNama Buku: {s}\nPengarang: {book[0]}" \
                            f"\nPenerbit Buku: {book[2]}\nTahun terbit: {book[1]}\nGenre Buku: {book[3]}"
                return f"Buku ditemukan\n{info_buku}"
            else:
                return search_buku(s, b, r + 1)
        else:
            return search_buku(s, b + 1)
    else:
        return f"Buku tidak ditemukan"


# Fungsi pengecekan kapasitas rak
def kapasitas(c):
    lst_rak = list(rak.keys())
    the_index = lst_rak.index(c)

    # mengecek apakah jumlah buku pada rak sudah mencapai batas maksimal kapasitas rak
    if len(rak[c]) < 3:
        return c
    elif len(rak[c]) == 3:
        print(f"Rak dengan nama {c} sudah penuh")

    # menambahkan rak tambahan dengan memanggil fungsi, jika semua rak yang tersedia sudah penuh
    if the_index == len(rak) - 1:
        return rak_tambahan()
    return kapasitas(lst_rak[the_index + 1])


# Fungsi untuk penambahan RakTambahan
def rak_tambahan():
    global tambahan
    tambahan += 1
    add_rak(f"RakTambahan{tambahan}")
    return f"RakTambahan{tambahan}"


# Fungsi untuk menghapus rak
def remove_rak(r):
    if r not in rak:
        print(f"Rak dengan nama {r} tidak ditemukan di dalam sistem")
    else:
        lst_rak = list(rak.keys())
        the_index = lst_rak.index(r)
        # menyimpan data nama buku yang ada di rak yang akan dihapus
        b = rak[r][::1]
        if the_index == len(rak) - 1:
            rak_tambahan()
        # memindahkan buku dari rak yang akan dihapus ke rak lain
        for book in b:
            lst_rak = list(rak.keys())
            the_index = lst_rak.index(r)
            move_buku([book, kapasitas(lst_rak[the_index + 1])])
        del rak[r]
        print(f"Rak dengan nama {r} berhasil dihapus")


# Fungsi yang menjalankan program utama great library
def great_library():
    print("Selamat datang di The Great Library\nSilakan masukkan perintah!")
    # Meminta input perintah dan membuat kata pada input menjadi elemen dalam list
    perintah = input("Perintah anda: ")
    lst_perintah = perintah.split()

    # Branching pencetakan output dengan pemanggilan fungsi sesuai input perintah
    if len(lst_perintah) >= 2 and " ".join([lst_perintah[0], lst_perintah[1]]) in tup_perintah:
        if lst_perintah[0] == "ADD" and lst_perintah[1] == "RAK" and len(lst_perintah) == 3:
            add_rak(lst_perintah[2])
        elif lst_perintah[0] == "ADD" and lst_perintah[1] == "BUKU" and len(lst_perintah) == 8:
            add_buku(lst_perintah[2:])
        elif lst_perintah[0] == "MOVE" and lst_perintah[1] == "BUKU" and len(lst_perintah) == 4:
            move_buku(lst_perintah[2:])
        elif lst_perintah[0] == "SEARCH" and lst_perintah[1] == "BUKU" and len(lst_perintah) == 3:
            print(search_buku(lst_perintah[2]))
        elif lst_perintah[0] == "REMOVE" and lst_perintah[1] == "RAK" and len(lst_perintah) == 3:
            remove_rak(lst_perintah[2])
        else:
            print("Perintah tidak valid")
    elif perintah == "EXIT":
        return print("Selesai, Sistem dimatikan")
    else:
        print("Perintah tidak dikenali")
    print()
    great_library()

# Pemanggilan fungsi great_library untuk memulai keseluruhan program
great_library()
