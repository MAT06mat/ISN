import matplotlib.pyplot as plt

size = 21
nb_iterations = size // 2 - 1
numero_jeu_regles = 1

# Initialisation de l'automate
# A completer

# INIT AFFICHAGE
g = []  #
g.append(grid)  # Ajout de l'etat t=0 de l'automate

for j in range(nb_iterations):
    # Evolution automate
    # A compléter

    g.append(grid)  # Ajout de la mise à jour de l'automate

# AFFICHAGE
plt.imshow(g)
plt.axis("off")
plt.show()
