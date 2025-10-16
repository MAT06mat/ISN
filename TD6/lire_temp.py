f = open("TD6/temp.txt", "r", encoding="utf-8")
temp = f.read()
f.close()

# print(temp)


"""
3.5

Le code lit le fichier temps.txt et affiche son contenu
temp est une chaine de caractère
"""

"""
3.6
"""
from Exercice3 import moyenne, ecart_type

liste_temp = []
for t in temp.split(","):
    liste_temp.append(int(t))

print(liste_temp)
print(f"Moyenne : {moyenne(liste_temp)}")
print(f"Ecart type : {ecart_type(liste_temp)}")


"""
3.7
"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title("Températures relevées du 12 Février 2025 à Lyon")
ax.plot(range(1, 25), liste_temp)
ax.set_xlabel("Heure de la journée (en h)")
ax.set_ylabel("Températures (en °C)")

fig.savefig("TD6/Exercice6.pdf")
