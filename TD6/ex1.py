"""
1.1

Le programme affiche une erreur (car liste[6 + 1] n'existe pas)
"""

"""
1.2

Affiche le nombre d'élements de la liste qui sont égaux à b + ou - 1
"""

"""
1.3

3
2
"""

liste1 = [1, 2, 3, 4, 5, 6]
liste2 = [4, 5, -1, 2, 8]
valeur = 5


def ma_fonction(liste, b):
    compteur = 0
    for i in range(len(liste)):
        if liste[i] >= b - 1 and liste[i] <= b + 1:
            compteur += 1
    return compteur


res1 = ma_fonction(liste1, valeur)
print(res1)
print(ma_fonction(liste2, valeur))
