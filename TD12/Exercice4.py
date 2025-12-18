from random import randint


def est_pair(l: list):
    pair = True
    i = 0
    while i < len(l) and pair:
        if l[i] % 2 != 0:
            pair = False
        i += 1
    return pair


def elimine_impair(l: list):
    for i in range(len(l)):
        if l[i] % 2 != 0:
            l[i] = 0


def creer_liste_aleatoire(n: int = 10):
    l = []
    for i in range(n):
        l.append(randint(0, 10))
    return l


def bataille(l: list):
    res = False
    pp = l[0] % 2 == 0
    for i in range(len(l) - 1):
        if pp and l[i + 1] % 2 != 0:
            pp = l[i + 1] % 2 == 0
            l[i + 1] = l[i]
            res = True
        else:
            pp = l[i + 1] % 2 == 0
    return res


def guerre(l: list):
    while bataille(l):
        pass


def guerre_ULTIME(l: list):
    for i in range(len(l) - 1):
        if l[i + 1] % 2 != 0:
            l[i + 1] = l[i]


liste = [2, 4, 1, 6, 5, 7, 9, 2, 3, 1, 2]
print(liste)
guerre_ULTIME(liste)
print(liste)
