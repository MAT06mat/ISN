"""
(1.1)
"""


def affiche_liste_2d(liste: list[list]):
    print()
    for ligne in liste:
        print(*ligne)
    print()


# table_2d = [[0, 2, 0, 1], [0, 0, 3, 0], [0, 4, 1, 5]]
# affiche_liste_2d(table_2d)


"""
(1.2)
"""


def creation_matrice_nulle(n: int, m: int):
    liste = []
    for _ in range(n):
        liste.append(m * [0])
    return liste


matrice_nulle = creation_matrice_nulle(5, 7)

"""
(1.3)
"""

# matrice_nulle[2][3] = 1
# affiche_liste_2d(matrice_nulle)


"""
(1.4)
"""


def affiche_centre(liste: list[list]):
    ligne_centrale = len(liste) // 2
    colone_centrale = len(liste[ligne_centrale]) // 2
    centre = liste[ligne_centrale][colone_centrale]
    print("Le centre est :", centre)


# affiche_centre(matrice_nulle)


"""
(1.5)
"""

from random import randint


def creation_matrice_aleatoire(n: int, m: int):
    liste = []
    for _ in range(n):
        ligne = []
        for _ in range(m):
            ligne.append(randint(0, 9))
        liste.append(ligne)
    return liste


alea = creation_matrice_aleatoire(5, 7)
# affiche_liste_2d(alea)
# affiche_centre(alea)

"""
(1.6)
"""


def compte_elem(liste: list[list[int]], k: int, val: int):
    compteur = 0
    for ligne in liste:
        n_elem = 0
        for elem in ligne:
            if elem >= val:
                n_elem += 1
        if n_elem >= k:
            compteur += 1
    return compteur


# print(compte_elem(alea, 4, 5))


"""
(1.7)
"""

from copy import deepcopy

l1 = creation_matrice_aleatoire(4, 5)
affiche_liste_2d(l1)
l2 = deepcopy(l1)
affiche_liste_2d(l2)


# Sinon:
def copie_matrice(liste: list[list[int]]):
    nouvelle_liste = []
    for i in range(len(liste)):
        ligne = []
        for j in range(len(liste[i])):
            ligne.append(liste[i][j])
        nouvelle_liste.append(ligne)
    return nouvelle_liste


l2 = copie_matrice(l1)
affiche_liste_2d(l2)
