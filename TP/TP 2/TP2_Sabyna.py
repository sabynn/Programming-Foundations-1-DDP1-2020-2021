import os
import random

# Fungsi mencakup keseluruhan permainan
def taman_melodi():
    print(r"""
  _
 | |__   ___ _ __ _ __   __ _  ___ _   _
 | '_ \ / _ \ '__| '_ \ / _` |/ __| | | |
 | |_) |  __/ |  | |_) | (_| | (__| |_| |
 |_.__/ \___|_|  | .__/ \__,_|\___|\__,_|
                 |_|                DALAM
  ██╗      ██╗ ██████╗  ██╗ ██╗  ██╗
  ██║      ██║ ██╔══██╗ ██║ ██║ ██╔╝
  ██║      ██║ ██████╔╝ ██║ █████╔╝
  ██║      ██║ ██╔══██╗ ██║ ██╔═██╗
  ███████╗ ██║ ██║  ██║ ██║ ██║  ██╗
  ╚══════╝ ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝
  """)
    print("~"*50)
    pemain = input("masukkan username    : ")
    mode = ""
    the_round = 0
    score = 0
    lagu = os.listdir("lagu")

    # Memastikan input uname dan mode sesuai yang diinginkan
    while pemain == "null" or pemain == "":
        pemain = input("harap gunakan nama yang valid.\nmasukkan username     : ")
    while mode.lower() not in ["normal", "expert"]:
        mode = input("mode (normal/expert) : ")

    # Mengatur nilai variabel hp sesuai mode yang dipilih user
    if mode.lower() == "normal":
        hp = 3
        line = 0
    else:
        hp = 1
        line = 1

    print("~"*50)
    print("Good Luck & Have Fun :)\n")

    # Selama var hp != 0, permainan terus berlanjut
    while hp != 0:
        the_round += 1
        print("Round", the_round)
        print("HP :", hp)
        print("Score :", score)
        print("~" * 50)

        # pemilihan lagu random dan memastikan lagu yang sudah terpilih, tidak akan terpilih lagi dalam satu permainan
        file = random.choice(lagu)
        lagu.remove(file)

        # memanggil dan mengassign fungsi generate_lagu ke variabel lyric
        lyric = generate_lagu(file)
        print("Judul lagu:", file.replace(".txt", ""))

        # memanggil dan mengassign fungsi pilih_lirik ke variabel lirik_random, kemudian meminta input tebakan
        lirik_random = pilih_lirik(lyric)
        tebakan = input("Silakan menebak: \n")

        # mengatur output jika tebakan benar ataupun salah
        if tebakan.lower() == lirik_random.lower():
            score += len(tebakan)
            print("Jawaban BENAR\n")
        else:
            hp -= 1
            print("Jawaban SALAH")
            print("Jawaban :", lirik_random, "\n")

        # mengatur output jika pemain berhasil menyelesaikan ronde lima, tanpa kehabisan HP
        if the_round == 5 and hp != 0:
            print("SELAMAT!\nAnda berhasil menyelesaikan permainan\nHasil akhir:\nScore:", score)
            break
    else:
        print("GAME OVER\nSayang sekali " + pemain + ", anda terhenti disini")
        print("Hasil akhir:\nScore:", score)

    create_highscore()
    # menulis perolehan highscore baru jika didapat score yg lebih tinggi daripada yg terdata di highscore.txt
    with open("highscore.txt", 'r+') as txt:
        text = txt.readlines()
        num = ""
        for word in text[line]:
            if word.isdigit():
                num += word
        if score > int(num):
            print("\nNEW HIGHSCORE!!!\nusername:", pemain, "\nscore:", score)
            print("Berhasil meraih highscore di mode", mode.lower())
            text[line] = str(mode).capitalize() + " " + pemain + " " + str(score) + "\n"
        print("\n~~~~~~~~~~~~~~~~ Thanks for playing ~~~~~~~~~~~~~~~~")
        txt.seek(0)
        txt.writelines(text)

# Fungsi membuka file dan mengembalikan list isi file sesuai nama file lagu yang terpilih dalam folder lagu
def generate_lagu(nama_file):
    with open(f"lagu/{nama_file}", 'r') as lagu_terpilih:
        isi_file = lagu_terpilih.readlines()
        # adapted from codespeedy.com
        lirik = [x.replace("\n", "") for x in isi_file]
    return lirik

# Fungsi mengembalikan lirik yang dipilih secara random  dan mencetak 4 baris lirik sebelum lirik terpilih
def pilih_lirik(ly):
    ly_choice = random.choice(ly)
    while ly_choice in ly[0:4]:
        ly_choice = random.choice(ly)
    else:
        the_index = ly.index(ly_choice)
        print("\n".join(ly[(the_index - 4): the_index]))
    return ly_choice

# Fungsi membuat file highscore.txt jika terdeteksi belum ada file di directory
def create_highscore():
    hs = os.listdir()
    highscore = None
    # check if doesn't exist, then create default
    if "highscore.txt" not in hs:
        highscore = open("highscore.txt", 'w')
        a = ["Normal null 0\n", "Expert null 0\n"]
        highscore.writelines(a)
    return highscore

# Memanggil fungsi taman_melodi untuk memulai keseluruhan permainan
taman_melodi()
