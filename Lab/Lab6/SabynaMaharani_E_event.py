# assign variabel awal
lst_k = []
dct = {}
dct_peserta = {}
# meminta input jumlah peserta webinar
for i in range(3):
    jumlah = input(f"Jumlah nama yang akan dicatat untuk Webinar {i+1}: ")
    lst_nama = []

    # meminta input nama peserta webinar
    for j in range(int(jumlah)):
        nama1 = input(f"Masukkan nama {j+1}: ")

        if nama1 == "":
            continue
        else:
            lst_nama.append(nama1)
    # memastikan tidak ada duplikasi nama dalam satu webinar
    s_nama = set(lst_nama)
    dct[i+1] = lst_nama

# membentuk list keseluruhan yg hadir
webinar = dct[1]
webinar.extend(dct[2])
webinar.extend(dct[3])

# menghitung kehadiran peserta
for i in webinar:
    k = webinar.count(i)
    lst_k.append(k)

s_webinar = set(webinar)

# menambahkan key dan value ke dict berupa nama peserta dan jumlah kehadiran
for i in s_webinar:
    dct_peserta[i] = lst_k[webinar.index(i)]


peserta = ", ".join(f"{k}({v})" for k, v in dct_peserta.items() if k)
peserta1 = ", ".join(k for k, v in dct_peserta.items() if v == 3)


# mencetak peserta yang dayang ke webinar
print("Peserta yang datang ke Webinar Donat DUAARRR!!!")
if peserta:
    print(peserta)
else:
    print("Tidak Ada")

# mencetak peserta yang dayang ke seluruh webinar
print("Peserta yang datang ke seluruh Webinar Donat DUAARRR!!!:")
if peserta1:
    print(peserta1)
else:
    print("Tidak Ada")
