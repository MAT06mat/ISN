"""
5.1
"""

ma_chaine = "Bonjour, je suis une belle phrase !"
voyelles = "aeiouy"

nb_voyelle = 0
for lettre in ma_chaine.lower():
    if lettre in voyelles:
        nb_voyelle += 1

print("Nb voyelle =", nb_voyelle)


"""
5.2
"""

print(f"La phrase '{ma_chaine}' contient les voyelles suivantes :")
for i in range(len(ma_chaine)):
    if ma_chaine[i].lower() in voyelles:
        print(f"-> {ma_chaine[i]} à la position {i + 1}")
