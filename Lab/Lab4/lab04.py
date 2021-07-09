# Menerima input nama file txt dari user
in_filename = input("Masukkan nama file input: ")

# Error handling jika file tidak ditemukan
try:
    # Menghitung karakter pada file dan menuliskan hasil di file yang sama
    char_list = []
    with open(in_filename, 'r+') as file:
        lines = file.readlines()

        # Membedakan hal yg dituliskan jika tidak ada teks pada file
        if not lines:
            file.write("NULL")
        else:
            for line in lines:
                char = len(line) - 1
                char_list.append(char)
            file.write("########### \n")
            file.write("Min: " + str(min(char_list)) + " karakter \n")
            file.write("Max: " + str(max(char_list)) + " karakter \n")
            file.write("Range: " + str(max(char_list) - min(char_list)) + " karakter \n")

except FileNotFoundError:
    print("File tidak ditemukan :(")

else:
    print("Output berhasil ditulis pada", in_filename)

# Meminta input enter untuk menyelesaikan program
input("Program selesai. Tekan enter untuk keluar...")
