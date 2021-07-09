# menerima input banyak perintah
banyak_perintah = input("Banyak Perintah: ")

# nilai awal sumbu x dan y
sumbu_x = 0
sumbu_y = 0

# menerima input perintah sesuai banyak perintah dan menggerakkan meong bross sesuai input perintah
for perintah in range(int(banyak_perintah)):
    x = input("Masukkan perintah: ")
    if x == "HOME":
        break
    elif x == "U":
        sumbu_y += 1
    elif x == "S":
        sumbu_y -= 1
    elif x == "T":
        sumbu_x += 1
    elif x == "B":
        sumbu_x -= 1

# mencetak koordinat akhir meong bross
print("Karakter Meong Bross berada di koordinat ({},{})".format(sumbu_x, sumbu_y))
