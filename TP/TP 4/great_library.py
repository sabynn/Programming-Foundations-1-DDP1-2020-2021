class Book:
    # Constructor class Book
    def __init__(self, nama, tahun, pengarang, penerbit):
        self.__nama = nama
        self.__tahun = tahun
        self.__pengarang = pengarang
        self.__penerbit = penerbit

    # fungsi mengembalikan nama buku
    def get_nama(self):
        return self.__nama

    # fungsi mengembalikan detail tahun buku
    def get_tahun(self):
        return self.__tahun

    # fungsi mengembalikan detail pengarang buku
    def get_pengarang(self):
        return self.__pengarang

    # fungsi mengembalikan detail penerbit buku
    def get_penerbit(self):
        return self.__penerbit

    # fungsi mengembalikan detail deskripsi buku
    def get_book_description(self):
        return f"Nama Buku: {self.get_nama()}\n" \
                f"Tahun: {self.get_tahun()}\n" \
                f"Pengarang: {self.get_pengarang()}\n" \
                f"Penerbit: {self.get_penerbit()}"

    # overload comparasion operators
    def __lt__(self, other):
        return self.get_nama() < other.get_nama()

    def __eq__(self, other):
        return self.get_nama() == other

class Fiction(Book):
    # constructor subclass Fiction (inheritance dari Book)
    def __init__(self, nama, tahun, pengarang, penerbit, genre):
        super().__init__(nama, tahun, pengarang, penerbit)
        self.__genre = genre

    # fungsi mengembalikan detail genre buku
    def get_genre(self):
        return self.__genre

    # override fungsi yang mengembalikan detail deskripsi buku
    def get_book_description(self):
        return f"\nBuku Fiksi\n{super().get_book_description()}\nGenre: {self.get_genre()}"

class Reference(Book):
    # constructor subclass Reference (inheritance dari Book)
    def __init__(self, nama, tahun, pengarang, penerbit, kota_terbit):
        super().__init__(nama, tahun, pengarang, penerbit)
        self.__kota_terbit = kota_terbit

    # fungsi mengembalikan detail kota terbit buku
    def get_kota_terbit(self):
        return self.__kota_terbit

    # override fungsi yang mengembalikan detail deskripsi buku
    def get_book_description(self):
        return f"\nBuku Referensi\n{super().get_book_description()}\nKota Terbit: {self.get_kota_terbit()}"

class Encyclopedia(Book):
    # constructor subclass Encyclopedia(inheritance dari Book)
    def __init__(self, nama, tahun, pengarang, penerbit, revisi_num):
        super().__init__(nama, tahun, pengarang, penerbit)
        self.__revisi_num = revisi_num

    # fungsi mengembalikan detail nomor revisi buku
    def get_revisi_num(self):
        return self.__revisi_num

    # override fungsi yang mengembalikan detail deskripsi buku
    def get_book_description(self):
        return f"\nBuku Ensiklopedia\n{super().get_book_description()}\nNomor Revisi: {self.get_revisi_num()}"

class Shelf:
    # constructor class Shelf
    def __init__(self, nama, kumpulan_buku):
        self.__nama = nama
        self.__kumpulan_buku = kumpulan_buku

    # fungsi mengembalikan nama rak
    def get_nama(self):
        return self.__nama

    # fungsi mengembalikan kumpulan buku
    def get_kumpulan_buku(self):
        return self.__kumpulan_buku

    # fungsi menambahkan buku ke kumpulan buku
    def set_kumpulan_buku(self, the_class):
        self.__kumpulan_buku.append(the_class)

    # fungsi mencari buku dari kumpulan buku dan mengembalikan deskripsi buku
    def search_buku(self, nama_buku, rack):
        for i in rack.get_kumpulan_buku():
            if i == nama_buku:
                return i.get_book_description()

    # fungsi mencetak nama rak dan buku yg ada di dalam rak, buku terurut sesuai alphanumerik dari kecil ke besar.
    def list_buku(self):
        b = []
        for i in sorted(self.__kumpulan_buku):
            b.append(f"     -{i.get_nama()}")
        return "\n".join(b)
class Knowledge(Shelf):
    # constructor subclass Knowledge(inheritance dari Shelf)
    def __init__(self, nama, kumpulan_buku):
        super().__init__(nama, kumpulan_buku)

    # fungsi menambahkan buku ke kumpulan buku sesuai jenis buku
    def add_buku(self, detail):
        rak, nama, tahun, pengarang, penerbit, jenis_buku, atribut = detail
        if jenis_buku not in ["Referensi", "Ensiklopedia"]:
            return "Buku gagal ditambahkan :("
        elif jenis_buku == "Referensi":
            class_buku = Reference(nama, tahun, pengarang, penerbit, atribut)
        elif jenis_buku == "Ensiklopedia":
            class_buku = Encyclopedia(nama, tahun, pengarang, penerbit, atribut)
        self.set_kumpulan_buku(class_buku)
        return f"Buku baru berhasil ditambahkan pada rak {rak} \n{class_buku.get_book_description()}"

class World(Shelf):
    # constructor subclass World(inheritance dari Shelf)
    def __init__(self, nama, kumpulan_buku):
        super().__init__(nama, kumpulan_buku)

    # fungsi menambahkan buku ke kumpulan buku sesuai jenis buku
    def add_buku(self, detail):
        rak, nama, tahun, pengarang, penerbit, jenis_buku, atribut = detail
        if jenis_buku not in ["Fiksi", "Ensiklopedia"]:
            return "Buku gagal ditambahkan :("
        elif jenis_buku == "Fiksi":
            class_buku = Fiction(nama, tahun, pengarang, penerbit, atribut)
        elif jenis_buku == "Ensiklopedia":
            class_buku = Encyclopedia(nama, tahun, pengarang, penerbit, atribut)
        self.set_kumpulan_buku(class_buku)
        return f"Buku baru berhasil ditambahkan pada rak {rak} \n{class_buku.get_book_description()}"

class Mystery(Shelf):
    # constructor subclass Mystery(inheritance dari Shelf)
    def __init__(self, nama, kumpulan_buku):
        super().__init__(nama, kumpulan_buku)

    # fungsi menambahkan buku ke kumpulan buku sesuai jenis buku
    def add_buku(self, detail):
        rak, nama, tahun, pengarang, penerbit, jenis_buku, atribut = detail
        if jenis_buku not in ["Fiksi", "Referensi"]:
            return "Buku gagal ditambahkan :("
        elif jenis_buku == "Fiksi":
            class_buku = Fiction(nama, tahun, pengarang, penerbit, atribut)
        elif jenis_buku == "Referensi":
            class_buku = Reference(nama, tahun, pengarang, penerbit, atribut)
        self.set_kumpulan_buku(class_buku)
        return f"Buku baru berhasil ditambahkan pada rak {rak} \n{class_buku.get_book_description()}"

class Compendium(Shelf):
    # constructor subclass Compendium(inheritance dari Shelf)
    def __init__(self, nama, kumpulan_buku):
        super().__init__(nama, kumpulan_buku)

    # fungsi menambahkan buku ke kumpulan buku sesuai jenis buku
    def add_buku(self, detail):
        rak, nama, tahun, pengarang, penerbit, jenis_buku, atribut = detail
        if jenis_buku == "Fiksi":
            class_buku = Fiction(nama, tahun, pengarang, penerbit, atribut)
        elif jenis_buku == "Ensiklopedia":
            class_buku = Encyclopedia(nama, tahun, pengarang, penerbit, atribut)
        elif jenis_buku == "Referensi":
            class_buku = Reference(nama, tahun, pengarang, penerbit, atribut)
        self.set_kumpulan_buku(class_buku)
        return f"Buku baru berhasil ditambahkan pada rak {rak} \n{class_buku.get_book_description()}"

class Library:
    # constructor class Library
    def __init__(self, kumpulan_rak):
        self.__kumpulan_rak = kumpulan_rak

    # fungsi mengembalikan kumpulan rak
    def get_kumpulan_rak(self):
        return self.__kumpulan_rak

    # fungsi menambahkan rak ke kumpulan rak sesuai jenis rak
    def add_rak(self, nama_rak, jenis_rak):
        if jenis_rak == "Pengetahuan":
            class_rak = Knowledge(nama_rak, [])
        elif jenis_rak == "Dunia":
            class_rak = World(nama_rak, [])
        elif jenis_rak == "Misteri":
            class_rak = Mystery(nama_rak, [])
        elif jenis_rak == "Compendium":
            class_rak = Compendium(nama_rak, [])
        self.__kumpulan_rak[nama_rak] = class_rak

    # fungsi meneruskan detail buku yg ingin ditambahkan ke rak yang sesuai
    def add_buku(self, detail):
        return self.get_kumpulan_rak()[detail[0]].add_buku(detail)

    # fungsi meneruskan pencarian buku sesuai dengan rak tempat buku disimpan
    def search_buku(self, nama_buku):
        for rak in self.get_kumpulan_rak():
            r = self.get_kumpulan_rak()[rak]
            if r.search_buku(nama_buku, r):
                return r.search_buku(nama_buku, r)

# tuple berisi string perintah valid
tup_perintah = ("ADD BUKU", "ADD RAK")

# mengassign variabel li menjadi objek dari Library
li = Library({})
# menambahkan rak rak default(sudah ada sebelum program utama berjalan)
li.add_rak("Pengetahuan01", "Pengetahuan")
li.add_rak("Dunia01", "Dunia")
li.add_rak("Misteri01", "Misteri")
li.add_rak("Compendium01", "Compendium")

# Fungsi yang menjalankan program utama great library
def main():
    print("Selamat datang di The Great Library\nSilakan masukkan perintah!")

    # Meminta input perintah dan membuat kata pada input menjadi elemen dalam list
    perintah = input("Perintah anda: ")
    lst_perintah = perintah.split()

    # Membuat list berisi kumpulan buku
    book = [li.get_kumpulan_rak()[rak].get_kumpulan_buku() for rak in li.get_kumpulan_rak()]
    book = [cl_buku for lst_buku in book for cl_buku in lst_buku]

    # Branching pencetakan output dengan pemanggilan fungsi sesuai input perintah
    if len(lst_perintah) >= 2 and ((" ".join([lst_perintah[0], lst_perintah[1]])) in tup_perintah):
        if lst_perintah[0] == "ADD" and lst_perintah[1] == "RAK" and len(lst_perintah) == 4:
            # mengecek apabila rak sudah ada di kumpulan rak
            if lst_perintah[2] in li.get_kumpulan_rak():
                print(f"Rak dengan nama {lst_perintah[2]} sudah ada di dalam sistem")
            # mengecek apakah jenis rak yang diinput valid
            elif lst_perintah[3] in ["Pengetahuan", "Dunia", "Misteri", "Compendium"]:
                li.add_rak(lst_perintah[2], lst_perintah[3])
                print("Rak buku berhasil ditambahkan\n")
                print(f"Nama: {lst_perintah[2]}\nJenis: {lst_perintah[3]}")
            else:
                print(f"Tidak dapat menambahkan Rak dengan jenis {lst_perintah[3]}")

        elif lst_perintah[0] == "ADD" and lst_perintah[1] == "BUKU" and len(lst_perintah) == 9:
            # mengecek apabila rak belum ada di kumpulan rak
            if (lst_perintah[2] not in li.get_kumpulan_rak()):
                print("Buku gagal ditambahkan :(")
            # mengecek apabila buku sudah berada di dalam kumpulan buku
            elif lst_perintah[3] in book:
                print(f"Buku dengan nama {lst_perintah[3]} sudah ada di dalam sistem")
            # mengecek apakah jenis rak yang diinput valid
            elif lst_perintah[7] in ["Fiksi", "Referensi", "Ensiklopedia"]:
                print(li.add_buku(lst_perintah[2:]))
            else:
                print("Buku gagal ditambahkan :(")
        else:
            print("Perintah tidak valid")

    elif len(lst_perintah) >= 1 and lst_perintah[0] == "SEARCH":
        if len(lst_perintah) != 2:
            print("Perintah tidak valid")
        # mengecek apabila buku ada di kumpulan buku
        elif lst_perintah[1] in book:
            print("Buku ditemukan")
            print(li.search_buku(lst_perintah[1]))
        else:
            print(f"Buku dengan nama {lst_perintah[1]} tidak ditemukan")

    elif perintah == "LIST":
        # mengecek apabila belum ada buku di rak
        if not book:
            print(f"Belum ada buku di dalam sistem :(")
        else:
            # memanggil fungsi list_buku untuk setiap rak yang ada di kumpulan rak
            for rak in li.get_kumpulan_rak():
                print(rak)
                if li.get_kumpulan_rak()[rak].list_buku():
                    print(li.get_kumpulan_rak()[rak].list_buku())

    elif perintah == "EXIT":
        return print("Selesai, Sistem dimatikan")
    else:
        print("Perintah tidak dikenali")
    print()
    main()

if __name__ == "__main__":
    main()
