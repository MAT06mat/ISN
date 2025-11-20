chaine = """Dans la suite, on suppose que les variables chaine et motif contiennent des chaînes de caractères
(String). On dira que chaine possède une occurence de motif à la position i si les lettres de
chaine à partir de la position i coïncident avec celles de motif. Par exemple, aaabaac possède
trois occurences du motif aa, en position 0, 1 et 4.
On dira que motif est une sous-chaîne de chaine si celle-ci possède au moins une occurence de
motif"""

motif = "motif"


print(chaine.count(motif))


count = 0
for i in range(len(chaine)):
    lettre_correct = 0
    for j in range(len(motif)):
        if i + j < len(chaine) and chaine[i + j] == motif[j]:
            lettre_correct += 1
    if lettre_correct == len(motif):
        count += 1

print(count)
