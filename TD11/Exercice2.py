"""
(2.1)
Pour chaque nombre n dans l'intervalle [a, b]:
    Calculer la liste des diviseurs stricts de n
    Faire la somme des diviseurs de n
    Si la sommme est égale à n:
        n est un nombre parfait

"""

from nombres_parfaits import est_parfait, compteur

interval = [2, 10000]
print("Début :", compteur)
for n in range(interval[0], interval[1] + 1):
    if est_parfait(n):
        print(f"{n} est parfait")

from nombres_parfaits import compteur

print("Fin :", compteur)
