# input atribut tactical doll milik saya
print("### MY TACTICAL DOLL ###")
my_doll_name = input("Masukkan nama Tactical Doll: ")
my_firepower = int(input("Masukkan Firepower: "))
my_rate_of_fire = int(input("Masukkan Rate of Fire: "))
my_accuracy = int(input("Masukkan Accuracy: "))
my_evasion = int(input("Masukkan Evasion: "))
my_dps = my_firepower * my_rate_of_fire / 60
my_dps = round(my_dps, 2)
my_combat_effectiveness = 30 * my_firepower + 40 * my_rate_of_fire ** 2//120 + 15 * (my_accuracy + my_evasion)

# input atribut tactical doll milik saya
print("### ENEMY TACTICAL DOLL ###")
enemyTacticalDollName = input("Masukkan nama Tactical Doll: ")
enemyFirepower = int(input("Masukkan Firepower: "))
enemyRateOfFire = int(input("Masukkan Rate of Fire: "))
enemyAccuracy = int(input("Masukkan Accuracy: "))
enemyEvasion = int(input("Masukkan Evasion: "))
enemy_dps = enemyFirepower * enemyRateOfFire / 60
enemy_dps = round(enemy_dps, 2)
enemyCombatEffectiveness = 30 * enemyFirepower + 40 * enemyRateOfFire ** 2//120 + 15 * (enemyAccuracy + enemyEvasion)

# cetak damage per second dan combat effectiveness Tactical Doll
print("### RESULT ###")
print(my_doll_name)
print("Damage per Second", my_dps)
print("Combat Effectiveness:", my_combat_effectiveness)
print(enemyTacticalDollName)
print("Damage per Second", enemy_dps)
print("Combat Effectiveness:", enemyCombatEffectiveness)

# membandingkan damage per second dan combat effectiveness dengan milik musuh dan menentukan tindakan
if my_dps > enemy_dps and my_combat_effectiveness > enemyCombatEffectiveness:
    print("Gass lawan")
else:
    print("Kaburrr")