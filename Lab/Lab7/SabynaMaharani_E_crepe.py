# Meminta input user dan mengembalikan type hasil input menjadi tuple
crepe = eval(input("Masukkan input Crepe CTAARRR!!!: "))

# Fungsi mengembalikan semua isi yang ada dalam Crêpe CTAARRR!!!
def crepe_ctar(c):
    # Base case (menghandle saat tuple kosong)
    if len(c) == 0:
        return ""
    # case apabila isi tuple adalah tuple
    elif isinstance(c[0], tuple):
        return crepe_ctar(c[0]) + crepe_ctar(c[1:])
    # case apabila isi tuple adalah string
    elif isinstance(c[0], str):
        return c[0] + " " + crepe_ctar(c[1:])

# Program mencetak "kosong" jika tidak ada isi dalam tuple
if crepe_ctar(crepe) == "":
    print("kosong")
# Program memanggil dan mencetak return fungsi crepe_ctar()
else:
    print(crepe_ctar(crepe))
