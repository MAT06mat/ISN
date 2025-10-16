"""
6.1
"""

liste = [42, 37, 12, 39, 24]


def cherche_min(liste, pos_debut):
    i_min = pos_debut
    for i in range(len(liste)):
        if i > pos_debut and liste[i_min] > liste[i]:
            i_min = i
    return i_min


"""
6.2
"""

a, b = 1, 2
a, b = b, a
# print(a, b)


"""
6.3
"""


def trier(liste):
    for i in range(len(liste)):
        i_min = cherche_min(liste, i)
        liste[i], liste[i_min] = liste[i_min], liste[i]
    return liste


# print(trier(liste))
