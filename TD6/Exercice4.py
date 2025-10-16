"""
4.1
"""

ma_liste = [0, 0, 2, 9, 8, 0, 1, 4, 4]

compte = []
for i in range(10):
    compte.append(ma_liste.count(i))

print(f"{compte=}")

"""
4.2
"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(range(10), compte)
fig.savefig("TD6/Exercice4.pdf")
