"""
3.1
"""

ma_liste = [0, 1, 2, 3, 4, 2, 1, -2, 3, 2, 0, 1, -1, 2, 4]
valeur = 0

nb_occurence = 0
for i in ma_liste:
    if i == valeur:
        nb_occurence += 1

# print(f"{valeur} apparait {nb_occurence} fois dans ma liste")


"""
3.2
"""

maximum = max(ma_liste)

i = 0
while i < len(ma_liste) and ma_liste[i] != maximum:
    i += 1

# print(f"Le maximum {maximum} se trouve à la position {i + 1}")


"""
3.3
"""

phrase = "aujourd'hui, il pleut"
caractere = "u"

i = 0
while i < len(phrase) and phrase[i] != caractere:
    i += 1

# print(f"La lettre {caractere} apparait la première fois à la position {i + 1}")


"""
3.4
"""

chaine1 = "radar"
chaine2 = "anna"
chaine3 = "python"
chaine4 = "ilaunrocsibiscornuali"


def palin(chaine):
    return chaine == chaine[::-1]


# print(f"La chaîne '{chaine1}' est un palindrome ? {palin(chaine1)}")
# print(f"La chaîne '{chaine2}' est un palindrome ? {palin(chaine2)}")
# print(f"La chaîne '{chaine3}' est un palindrome ? {palin(chaine3)}")
# print(f"La chaîne '{chaine4}' est un palindrome ? {palin(chaine4)}")
