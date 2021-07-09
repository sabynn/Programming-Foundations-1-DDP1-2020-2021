print("### REQUEST TACTICAL DOLL ###")
# menerima input nama tactical doll dalam bentuk str
tactical_doll_name = input("Masukkan nama Tactical Doll: ")

# menerima input atribut tactical doll dan mengubah input ke bentuk int
firepower = int(input("Masukkan Firepower: "))
rate_of_fire = int(input("Masukkan Rate of Fire: "))
accuracy = int(input("Masukkan Accuracy: "))
evasion = int(input("Masukkan Evasion: "))

# menghitung damage per second dan membulatkan nilainya menjadi dua angka di belakang koma
damage_per_second = firepower * rate_of_fire / 60
damage_per_second = round(damage_per_second, 2)

# menghitung combat effectiveness Tactical Doll
combat_effectiveness = 30 * firepower + 40 * rate_of_fire ** 2//120 + 15 * (accuracy + evasion)

# mencetak nama, atribut, damage per second, dan combat effectiveness Tactical Doll
print("### SUCCESS ###")
print("Nama Tactical Doll:", tactical_doll_name)
print("Firepower:", firepower)
print("Rate of Fire:", rate_of_fire)
print("Accuracy:", accuracy)
print("Evasion:", evasion)
print("Damage per Second", damage_per_second)
print("Combat Effectiveness:", combat_effectiveness)

