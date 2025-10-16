from math import sqrt


def moyenne(l):
    return sum(l) / len(l)


def ecart_type(l):
    moy = moyenne(l)
    l2 = [(i - moy) ** 2 for i in l]
    return sqrt(sum(l2) / len(l))


print(ecart_type([5]))
print(ecart_type([0, -2, 8, 1]))
print(ecart_type(range(1_000_000)))
