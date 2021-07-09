# menerima input banyak perintah
banyak_perintah = input("Banyak Perintah: ")

sumbu_x = 0
sumbu_y = 0
sumbu = (sumbu_x, sumbu_y)
list_sumbu = [sumbu]

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
    sumbu_baru = (sumbu_x, sumbu_y)
    list_sumbu.append(sumbu_baru)

list_sumbu = ', '.join(map(str, list_sumbu))

print("Jalur yang ditempuh meong bross adalah", list_sumbu)