from random import randint


def jeu_vide(n, val):
    """
    Créer une grille de taille n x n, chaque case contenant la valeur val
    Paramètres:
        - n (int): la taille d'un coté de la grille
        - val (int): la valeur à mettre dans chaque case
    Retour:
        - jeu: la grille
    """
    jeu = []
    for i in range(n):
        jeu.append([])
        for j in range(n):
            jeu[i].append(val)
    return jeu


def initialisation_grille_cachee(n, nb_mines):
    """
    Créer une grille de jeu cachée avec un nombre de mines
    donné placées aléatoirement
    Paramètres:
        - n (int): la taille d'un côté de la grille
        - nb_mines (int): le nombre de mines à placer
    Retour:
        - la grille de jeu cachée (grille)
    """
    jeu = jeu_vide(n, 0)
    mines = 0
    while mines < nb_mines:
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        if jeu[x][y] != -1:
            jeu[x][y] = -1
            mines += 1

    calcul_mines_voisines(jeu)
    return jeu


def initialisation_grille_affichee(n):
    """
    Créer une grille de jeu qui sera affichée au joueur
    donné placées aléatoirement
    Paramètres:
        - n (int): la taille d'un côté de la grille
    Retour:
        - la grille de jeu à afficher (grille)
    """
    return jeu_vide(n, -1)


def calcul_mines_voisines(jeu):
    """
    Calcule le nombre de mines adjacentes à chaque case du jeu et
    met à jour l
    Paramètres:
        - jeu (grille): la grille de jeu contenant les mines
    Retour:
        - Rien.
    """
    for i in range(len(jeu)):
        for j in range(len(jeu)):
            if jeu[i][j] == -1:
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if k != 0 or l != 0:
                            if (
                                i + k >= 0
                                and i + k < len(jeu)
                                and j + l >= 0
                                and j + l < len(jeu)
                                and jeu[i + k][j + l] != -1
                            ):
                                jeu[i + k][j + l] += 1


def choix_coordonnees(jeu):
    """
    Demander au joueur la case qu'il veut dévoiler
    Paramètres:
        - jeu (grille): le jeu
    Retour:
        - x (int): le numéro de la ligne de la case
        - y (int): le numéro de la colonne de la case
    """
    i = -1
    j = -1
    while i < 0 or i >= len(jeu) or j < 0 or j >= len(jeu):
        try:
            print(f"Les coordonnées doivent être comprises entre {0} et {len(jeu)-1}")
            i = input("Choix de l'indice de ligne ? ")
            if i == "":
                raise SystemExit()
            j = input("Choix de l'indice de colonne ? ")
            i, j = int(i), int(j)
        except (KeyboardInterrupt, SystemExit):
            exit()
        except:
            i = -1
            j = -1
            print("Format non accepté")
    return i, j


def mise_a_jour_jeu_visible(jeu, jeu_visible, i_init, j_init):
    """
    Met à jour le jeu visible en fonction de la case sélectionnée par le joueur
    Paramètres:
        - jeu (grille): le jeu
        - jeu_visible (grille): le jeu visible par le joueur
        - x (int): numéro de ligne de la case choisie par le joueur
        - y (int): numéro de colonne de la case choisie par le joueur
    Retour:
        Rien.
    """
    cases_a_decouvrir = [[i_init, j_init]]
    while len(cases_a_decouvrir) > 0:
        i, j = cases_a_decouvrir.pop()
        if jeu[i][j] != 0:
            jeu_visible[i][j] = jeu[i][j]  # Afficher la case
        else:
            jeu_visible[i][j] = 0  # Afficher la case
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (
                        i + k >= 0
                        and i + k < len(jeu)
                        and j + l >= 0
                        and j + l < len(jeu)
                    ):
                        if jeu_visible[i + k][j + l] == -1:  # Case non visitée
                            cases_a_decouvrir.append([i + k, j + l])


def affichage_jeu(jeu):
    """
    Afficher la grille du jeu cachée contenant la position de toutes les mines
    Paramètres:
        - jeu (grille): le jeu caché
    """
    for i in range(len(jeu)):
        ligne = ""
        for j in range(len(jeu)):
            if jeu[i][j] == -1:
                ligne += "* "
            else:
                ligne += str(jeu[i][j]) + " "
        print(ligne)
    print()


def affichage_jeu_visible(jeu):
    """
    Afficher la grille du jeu visible (les -1 sont masqués et
    les autres valeurs sont affichées)
    Paramètres:
        - jeu_visible (grille): le jeu visible par le joueur
    """
    for i in range(len(jeu)):
        ligne = ""
        for j in range(len(jeu)):
            if jeu[i][j] == -1:
                ligne += "_ "
            else:
                ligne += str(jeu[i][j]) + " "
        print(ligne)
    print()


def jeu_gagne(jeu_visible, nb_mines):
    """
    Détermine si le jeu est gagné ou non
    Paramètres:
        - jeu_visible (grille): le jeu visible
        - nb_mines (int): le nombre de mines totales dans le jeu
    Retour:
        - True si le jeu est gagné, False sinon
    """
    taille_jeu = len(jeu_visible)
    compteur = taille_jeu**2
    for i in range(taille_jeu):
        for j in range(taille_jeu):
            if jeu_visible[i][j] == -1:
                compteur -= 1
    return compteur == taille_jeu**2 - nb_mines


def jeu_perdu(jeu, i, j):
    """
    Détermine si le jeu est perdu ou non suite au choix d'une nouvelle case par le joueur
    Paramètres:
        - jeu (grille): le jeu caché
        - x (int): numéro de ligne de la case choisie par le joueur
        - y (int): numéro de colonne de la case choisie par le joueur
    Retour:
        - True si le jeu est perdu, False sinon
    """
    return jeu[i][j] == -1
