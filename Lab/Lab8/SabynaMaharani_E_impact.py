class Anemo:
    def __init__(self, name, hp, atk, em):
        ## TODO
        # constructor name, hp, atk, em
        self.name = name
        self.atk = atk
        self.hp = hp
        self.em = em

    def attack(self, other):
        ## TODO
        # Implementasi attack ( mengurangi hp karakter yang diserang sesuai besar atk penyerang)
        other.hp -= self.atk
        pass

    def elemental_skill(self, other):
        ## TODO
        # Implementasi reaksi elemen (reaksi elemental Swirl saat Anemo menyerang Pyro/Hydro)
        if self.em > other.em:
            if isinstance(other, Pyro) or isinstance(other, Hydro):
                other.hp -= (self.em + other.em)
        pass

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        ## TODO
        # Implementasi cetak nama dan hp sesuai format
        return f"{self.name:20} | {self.hp:4}"


class Pyro:
    def __init__(self, name, hp, atk, em):
        ## TODO
        # constructor name, hp, atk, em
        self.name = name
        self.atk = atk
        self.hp = hp
        self.em = em

    def attack(self, other):
        ## TODO
        # Implementasi attack ( mengurangi hp karakter yang diserang sesuai besar atk penyerang)
        other.hp -= self.atk
        pass

    def elemental_skill(self, other):
        ## TODO
        # Implementasi reaksi elemen
        if self.em > other.em:
            # untuk reaksi elemental Swirl (jika Pyro menyerang Anemo)
            if isinstance(other, Anemo):
                other.hp -= (self.em + other.em)
            # untuk reaksi elemental Vaporize (jika Pyro menyerang Hydro)
            elif isinstance(other, Hydro):
                other.hp -= int(1.5 * self.em)
        pass

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        ## TODO
        # Implementasi cetak nama dan hp sesuai format
        return f"{self.name:20} | {self.hp:4}"


class Hydro:
    def __init__(self, name, hp, atk, em):
        ## TODO
        # constructor name, hp, atk, em
        self.name = name
        self.atk = atk
        self.hp = hp
        self.em = em

    def attack(self, other):
        ## TODO
        # Implementasi attack(mengurangi hp karakter yang diserang sesuai besar atk penyerang)
        other.hp -= self.atk
        pass

    def elemental_skill(self, other):
        ## TODO
        # Implementasi reaksi elemen
        if self.em > other.em:
            # untuk reaksi elemental Swirl (jika Hydro menyerang Anemo)
            if isinstance(other, Anemo):
                other.hp -= (self.em + other.em)
            # untuk reaksi elemental Vaporize (jika Hydro menyerang Pyro)
            elif isinstance(other, Pyro):
                other.hp -= (2 * self.em)
        pass
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        ## TODO
        # Implementasi cetak nama dan hp sesuai format
        return f"{self.name:20} | {self.hp:4}"


def main():
    ## TODO
    # Membuat dictionary untuk karakter
    characters = {}

    # Meminta input detail karakter
    input_chara = input("Masukkan karakter: ")
    while input_chara:
        # Assign input ke name, vision, hp, atk, dan em
        name, vision, hp, atk, em = input_chara.split()
        hp, atk, em = int(hp), int(atk), int(em)

        # Menambahkan karakter ke class sesuai vision karakter dan ditambahkan ke dict
        if vision == 'Anemo':
            characters[name] = Anemo(name, hp, atk, em)
        elif vision == 'Pyro':
            characters[name] = Pyro(name, hp, atk, em)
        elif vision == 'Hydro':
            characters[name] = Hydro(name, hp, atk, em)
        else:
            print(f"[ERROR] {vision}: Vision tidak valid")
        input_chara = input("Masukkan karakter: ")

    # Mencetak interaksi yang dilakukan
    inp = input("\nKarakter yang berinteraksi: ")
    while inp != "":
        name1, name2 = inp.split()
        char1 = characters.get(name1)
        char2 = characters.get(name2)

        if char1.is_alive() and char2.is_alive():
            char1.attack(char2)
            print(f"{char1.name} menyerang {char2.name} sebesar {char1.atk}")
        else:
            if not char1.is_alive():
                print(f"{char1.name} sudah mati.")
            elif not char2.is_alive():
                print(f"{char2.name} sudah mati.")
            inp = input("\nKarakter yang berinteraksi: ")
            continue

        if char1.is_alive() and char2.is_alive():
            char2.attack(char1)
            print(f"{char2.name} menyerang {char1.name} sebesar {char2.atk}")
        else:
            if not char1.is_alive():
                print(f"{char1.name} sudah mati.")
            elif not char2.is_alive():
                print(f"{char2.name} sudah mati.")
            inp = input("\nKarakter yang berinteraksi: ")
            continue

        if char1.is_alive() and char2.is_alive():
            char1.elemental_skill(char2)
            char2.elemental_skill(char1)

            if type(char1) == type(char2):
                print("Tidak terjadi reaksi elemen")
            else:
                if isinstance(char1, Anemo) or isinstance(char2, Anemo):
                    print("Terjadi reaksi elemen Swirl!")
                    if char1.em > char2.em:
                        damager = char1.name
                        damaged = char2.name
                    elif char2.em > char1.em:
                        damager = char2.name
                        damaged = char1.name

                    if char1.em != char2.em:
                        print(f"{damager} melukai {damaged} sebesar {char1.em + char2.em}!")
                    else:
                        print("Tidak ada yang terluka")
                else:
                    print("Terjadi reaksi elemen Vaporize!")
                    if char1.em > char2.em:
                        damager = char1.name
                        damaged = char2.name
                    elif char2.em > char1.em:
                        damager = char2.name
                        damaged = char1.name

                    if char1.em != char2.em:
                        if isinstance(characters[damager], Pyro):
                            damage = int(1.5 * characters[damager].em)
                        else:
                            damage = 2 * characters[damager].em
                        print(f"{damager} melukai {damaged} sebesar {damage}!")

                    else:
                        print("Tidak ada yang terluka")
        else:
            if not char1.is_alive():
                print(f"{char1.name} sudah mati.")
            elif not char2.is_alive():
                print(f"{char2.name} sudah mati.")

        inp = input("\nKarakter yang berinteraksi: ")

    print("\nKarakter yang masih hidup:")
    print("-" * 27)
    print("Nama                 | HP")
    print("-" * 27)
    ## TODO
    # Cetak semua karakter yang masih hidup
    for char in characters:
        if characters[char].is_alive():
            print(characters[char])

if __name__ == '__main__':
    main()
