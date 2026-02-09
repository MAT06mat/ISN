from funcs import *
from random import choice
from wordlistignore import words

TAILLE = 10
NB_MINES = 100

grille_bombes = initialisation_grille_cachee(TAILLE, NB_MINES)
grille_affiche = initialisation_grille_affichee(TAILLE)

partie_termine = False
victoire = False

while not partie_termine:
    affichage_jeu_visible(grille_affiche)

    x, y = choix_coordonnees(grille_bombes)
    mise_a_jour_jeu_visible(grille_bombes, grille_affiche, x, y)

    if jeu_perdu(grille_bombes, x, y):
        partie_termine = True
    elif jeu_gagne(grille_affiche, NB_MINES):
        victoire = True
        partie_termine = True

if victoire:
    affichage_jeu_visible(grille_affiche)
    print("Bien joué, tu as trouvé toutes les bombes")
else:
    affichage_jeu(grille_bombes)
    print("Perdu... Les mines ont eu raison de toi...")
    print(choice(words))
