from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()
        self.create_buttons()
        self.create_editor()

    def initUI(self):
        # Mengatur judul dan ukuran dari main window, membuat Frame sebagai anchor dari seluruh button
        self.master.title("Pacil Editor")
        self.master.geometry("500x400")
        self.frame = Frame(self.master)
        # Mengatur frame agar berada di bagian atas
        self.frame.pack(side=TOP, anchor=NW)

    def create_buttons(self):
        # Implementasi button yang dibutuhkan
        self.open = Button(self.frame, text="Open File", command=self.load_file)
        self.open.grid(row=0, column=0, padx=5)
        self.save = Button(self.frame, text="Save File", command=self.save_file)
        self.save.grid(row=0, column=1, padx=5)
        self.quit = Button(self.frame, text="Quit Program", command=self.master.destroy)
        self.quit.grid(row=0, column=2, padx=5)

        # Implementasi event binding (bonus)
        self.master.bind("<Control-o>", self.load_file_event)
        self.master.bind("<Control-s>", self.save_file_event)


    def create_editor(self):
        # Implementasi textbox
        self.textbox = Text(self.master)
        self.textbox.pack(fill="both", expand=YES)

    def load_file_event(self, event):
        self.load_file()

    def load_file(self):
        file_name = askopenfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return
        text_file = open(file_name, 'r', encoding="utf-8")
        result = text_file.read()
        # menampilkan result di textbox
        self.set_text(result)
        text_file.close()

    def save_file_event(self, event):
        self.save_file()

    def save_file(self):
        file_name = asksaveasfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return
        # ambil isi dari textbox lalu simpan dalam file dengan nama file_name
        result = self.get_text()
        text_file = open(file_name, "w", encoding="utf-8")
        text_file.write(result)
        text_file.close()

    def set_text(self, text=''):
        # menuliskan isi file ke textbox
        self.textbox.delete('1.0', END)
        self.textbox.insert('1.0', text)
        self.textbox.mark_set(INSERT, '1.0')
        self.textbox.focus()

    def get_text(self):
        # ambil teks dari textbox
        return self.textbox.get('1.0', END+'-1c')

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
