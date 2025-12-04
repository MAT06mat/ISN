from time import time


def time_it(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        print(f"{func} time :", t2 - t1)
        return res

    return wrapper


chaine = (
    """Dans la suite, on suppose que les variables chaine et motif contiennent des chaînes de caractères
(String). On dira que chaine possède une occurence de motif à la position i si les lettres de
chaine à partir de la position i coïncident avec celles de motif. Par exemple, aaabaac possède
trois occurences du motif aa, en position 0, 1 et 4.
On dira que motif est une sous-chaîne de chaine si celle-ci possède au moins une occurence de
motif"""
    * 1000
)


motif = (
    """On dira que chaine possède une occurence de motif à la position i si les lettres de
chaine à partir de la position i coïncident avec celles de motif. Par exemple, aaabaac possède
trois occurences du motif aa, en position 0, 1 et 4.
On dira que motif est une sous-chaîne de chaine si celle-ci possède au moins une occurence de
motif"""
    * 200
)


@time_it
def default_count(chaine, motif):
    return chaine.count(motif)


@time_it
def count1(chaine, motif):
    count = 0
    for i in range(len(chaine)):
        lettre_correct = 0
        for j in range(len(motif)):
            if i + j < len(chaine) and chaine[i + j] == motif[j]:
                lettre_correct += 1
        if lettre_correct == len(motif):
            count += 1
    return count


@time_it
def count2(chaine, motif):
    count = 0
    for i in range(len(chaine) - len(motif) + 1):
        lettre_correct = True
        j = 0
        while j < len(motif) and lettre_correct:
            if chaine[i + j] == motif[j]:
                j += 1
            else:
                lettre_correct = False
        if lettre_correct:
            count += 1
    return count


@time_it
def count3(chaine, motif):
    count = 0
    for i in range(len(chaine) - len(motif) + 1):
        if chaine[i : i + len(motif)] == motif:
            count += 1
    return count


print(default_count(chaine, motif))
# print(count1(chaine, motif))
print(count2(chaine, motif))
print(count3(chaine, motif))
