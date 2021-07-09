from tkinter import *
from tkinter import messagebox

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
                return "Buku ditemukan\n" + i.get_book_description() + "\n"

    # fungsi mencetak nama rak dan buku yg ada di dalam rak, buku terurut sesuai alphanumerik dari kecil ke besar.
    def list_buku(self):
        b = []
        # cek apakah ada buku di dalam rak
        if self.get_kumpulan_buku():
            for i in sorted(self.get_kumpulan_buku()):
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
        if nama_rak in self.get_kumpulan_rak():
            return f"Rak dengan nama {nama_rak} sudah ada di dalam sistem"
        elif jenis_rak == "Pengetahuan":
            class_rak = Knowledge(nama_rak, [])
        elif jenis_rak == "Dunia":
            class_rak = World(nama_rak, [])
        elif jenis_rak == "Misteri":
            class_rak = Mystery(nama_rak, [])
        elif jenis_rak == "Compendium":
            class_rak = Compendium(nama_rak, [])
        else:
            return f"Tidak dapat menambahkan Rak dengan jenis {jenis_rak}"
        self.__kumpulan_rak[nama_rak] = class_rak
        return "Rak buku berhasil ditambahkan\n" + f"\nNama: {nama_rak}\nJenis: {jenis_rak}"

    # fungsi meneruskan detail buku yg ingin ditambahkan ke rak yang sesuai
    def add_buku(self, detail):
        if detail[0] not in self.get_kumpulan_rak():
            return f"Buku gagal ditambahkan :("
        return self.get_kumpulan_rak()[detail[0]].add_buku(detail)

    # fungsi meneruskan pencarian buku sesuai dengan rak tempat buku disimpan
    def search_buku(self, nama_buku):
        for rak in self.get_kumpulan_rak():
            r = self.get_kumpulan_rak()[rak]
            if r.search_buku(nama_buku, r):
                return r.search_buku(nama_buku, r)
        return f"Buku dengan nama {nama_buku} tidak ditemukan"

# mengassign variabel li menjadi objek dari Library
li = Library({})
# menambahkan rak rak default(sudah ada sebelum program utama berjalan)
li.add_rak("Pengetahuan01", "Pengetahuan")
li.add_rak("Dunia01", "Dunia")
li.add_rak("Misteri01", "Misteri")
li.add_rak("Compendium01", "Compendium")

class GreatLibrary():
    # constructor GreatLibrary
    def __init__(self, master):
        self.master = master
        self.initUI()
        self.menu()
        self.master.mainloop()

    # fungsi mengembalikan list berisi nama nama buku yg ada pada sistem
    def bookshelf(self):
        book = [li.get_kumpulan_rak()[rak].get_kumpulan_buku() for rak in li.get_kumpulan_rak()]
        book = [cl_buku for lst_buku in book for cl_buku in lst_buku]
        return book

    # fungsi mengatur tampilan windows untuk GUI Menu
    def initUI(self):
        # Mengatur judul dan ukuran dari main window, membuat Frame sebagai anchor dari seluruh button
        self.master.title("The Great Library")
        self.master.geometry("400x200")
        self.master['background'] = '#a2d2ff'
        self.frame = Frame(self.master, bg="#a2d2ff")
        # Mengatur frame agar berada di bagian atas
        self.frame.pack(anchor=CENTER, expand=YES)

    # fungsi mengatur teks dan button untuk GUI Menu
    def menu(self):
        self.label = Label(self.frame, text="Selamat Datang di The Great Library. Silahkan pilih menu yang tersedia",
                           bg="#a2d2ff")
        self.label.grid()
        # Implementasi button yang dibutuhkan
        self.m_buku = Button(self.frame, text="ADD BUKU", command=self.form_buku, height=1, width=15,
                             bg="#bde0fe")
        self.m_buku.grid(row=1, column=0, pady=5)
        self.m_rak = Button(self.frame, text="ADD RAK", command=self.form_rak, height=1, width=15,
                            bg="#bde0fe")
        self.m_rak.grid(row=2, column=0, pady=5)
        self.m_search = Button(self.frame, text="SEARCH", command=self.form_search, height=1, width=15,
                               bg="#bde0fe")
        self.m_search.grid(row=3, column=0, pady=5)
        self.m_list = Button(self.frame, text="LIST", command=self.list, height=1, width=15,
                             bg="#bde0fe")
        self.m_list.grid(row=4, column=0, pady=5)

    # fungsi mengatur penambahan buku sesuai input pada form add buku
    def add_buku(self):
        # mengecek kevalidan input
        if self.b_rak.get().strip() and self.b_nama.get().strip() and self.b_tahun.get().strip() \
                and self.b_penulis.get().strip() and self.b_penerbit.get().strip() \
                and self.b_jenis.get().strip() and self.b_extra.get().strip():
            self.tambah_buku = [self.b_rak.get(), self.b_nama.get(), self.b_tahun.get(),
                                self.b_penulis.get(), self.b_penerbit.get(), self.b_jenis.get(), self.b_extra.get()]
            if self.b_nama.get() in self.bookshelf():
                messagebox.showinfo("", f"Buku dengan nama {self.b_nama.get()} sudah ada di dalam sistem")
            else:
                messagebox.showinfo("", li.add_buku(self.tambah_buku))
        else:
            messagebox.showerror("Invalid Input", "Input tidak valid")

    # fungsi mengatur penambahan rak sesuai input pada form add rak
    def add_rak(self):
        # mengecek kevalidan input
        if len(self.r_nama.get().strip()) and len(self.r_jenis.get().strip()):
            r_hasil = li.add_rak(self.r_nama.get(), self.r_jenis.get())
            messagebox.showinfo("", r_hasil)
        else:
            messagebox.showerror("Invalid Input", "Input tidak valid")

    # fungsi mengatur fitur search sesuai input pada form search
    def cari(self):
        # mengecek kevalidan input
        if self.s_nama.get().strip():
            messagebox.showinfo("", li.search_buku(self.s_nama.get()))
        else:
            messagebox.showerror("Invalid Input", "Input tidak valid")

    # fungsi mengatur kemunculan list nama rak dan nama buku pada GUI
    def list(self):
        # mengecek apakah sudah ada buku di dalam sistem
        if self.bookshelf():
            lst_detail = []
            for rak in li.get_kumpulan_rak():
                lst_detail.append(rak + "\n")
                if li.get_kumpulan_rak()[rak].list_buku():
                    lst_detail.append(li.get_kumpulan_rak()[rak].list_buku() + "\n")
            messagebox.showinfo("", "".join(lst_detail))
        else:
            messagebox.showinfo("", f"Belum ada buku di dalam sistem :(")

    # fungsi mengatur GUI Form add buku
    def form_buku(self):
        self.buku= Tk()
        self.buku.geometry("300x300")
        self.buku.title("Form Buku")
        self.buku["background"] = "#a2d2ff"
        self.f_buku = Frame(self.buku, bg="#a2d2ff")

        self.f_buku.pack(anchor=CENTER, expand=YES)
        Label(self.f_buku, text="Form Tambah Buku", bg="#a2d2ff").grid(row=0, column=1)

        Label(self.f_buku, text="Jenis", bg="#a2d2ff").grid(row=1, padx=5)
        self.b_jenis = Entry(self.f_buku)
        self.b_jenis.grid(row=1, column=1)

        Label(self.f_buku, text="Rak", bg="#a2d2ff").grid(row=2, padx=5)
        self.b_rak = Entry(self.f_buku)
        self.b_rak.grid(row=2, column=1)

        Label(self.f_buku, text="Nama", bg="#a2d2ff").grid(row=3)
        self.b_nama = Entry(self.f_buku)
        self.b_nama.grid(row=3, column=1)

        Label(self.f_buku, text="Tahun", bg="#a2d2ff").grid(row=4)
        self.b_tahun = Entry(self.f_buku)
        self.b_tahun.grid(row=4, column=1)

        Label(self.f_buku, text="Penulis", bg="#a2d2ff").grid(row=5)
        self.b_penulis = Entry(self.f_buku)
        self.b_penulis.grid(row=5, column=1)

        Label(self.f_buku, text="Penerbit", bg="#a2d2ff").grid(row=6)
        self.b_penerbit = Entry(self.f_buku)
        self.b_penerbit.grid(row=6, column=1)

        Label(self.f_buku, text="Extra", bg="#a2d2ff").grid(row=7)
        self.b_extra = Entry(self.f_buku)
        self.b_extra.grid(row=7, column=1)

        Button(self.f_buku, text="SUBMIT", bg="#bde0fe", command=self.add_buku).grid(row=8, column=1)

    # fungsi mengatur GUI Form add rak
    def form_rak(self):
        self.rak= Tk()
        self.rak.geometry("300x300")
        self.rak.title("Form Rak")
        self.rak["background"] = "#a2d2ff"
        self.f_rak = Frame(self.rak, bg="#a2d2ff")

        self.f_rak.pack(anchor=CENTER, expand=YES)
        Label(self.f_rak, text="Form Tambah Rak", bg="#a2d2ff").grid(row=0, column=1)

        Label(self.f_rak, text="Nama", bg="#a2d2ff").grid(row=1, padx=5)
        self.r_nama = Entry(self.f_rak)
        self.r_nama.grid(row=1, column=1)

        Label(self.f_rak, text="Jenis", bg="#a2d2ff").grid(row=2, padx=5)
        self.r_jenis = Entry(self.f_rak)
        self.r_jenis.grid(row=2, column=1)

        Button(self.f_rak, text="SUBMIT", bg="#bde0fe", command=self.add_rak).grid(row=8, column=1)

    # fungsi mengatur GUI Form search
    def form_search(self):
        self.search= Tk()
        self.search.geometry("400x200")
        self.search.title("Form Rak")
        self.search["background"] = "#a2d2ff"
        self.f_search = Frame(self.search, bg="#a2d2ff")

        self.f_search .pack(anchor=CENTER, expand=YES)
        Label(self.f_search, text="Form Cari Buku. Ketikkan Nama Buku pada kolom di bawah ini",
              bg="#a2d2ff").grid(row=0, column=1)

        self.s_nama = Entry(self.f_search)
        self.s_nama.grid(row=1, column=1)

        Button(self.f_search, text="SUBMIT", bg="#bde0fe", command=self.cari).grid(row=8, column=1)

if __name__ == "__main__":
    # membuat windows utama program great library
    windows = Tk()
    GreatLibrary(windows)
