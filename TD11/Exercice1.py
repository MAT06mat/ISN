def calcul_impot(revenu, nb_parts):
    """La fonction calcul_impot permet de calculer un impôt d'un certain nombre de foyers.

    :param int revenu: Le revenu total du foyer
    :param float nb_parts: Le nombre de part du foyer

    :return: L'impôt calculé
    :rtype: float"""

    ratio = revenu / nb_parts
    if ratio < 20000:
        impot = revenu * 0.125 - 50 * nb_parts
    elif ratio < 30000:
        impot = revenu * 0.25 - 100 * nb_parts
    else:
        impot = revenu * 0.5 - 200 * nb_parts
    return impot


def afficher_foyer(revenu, nb_parts):
    """La fonction afficher_foyer permet d'afficher et de calculer l'impot d'un foyer en fonction de son revenu et de ses parts.

    :param int revenu: Le revenu total du foyer
    :param float nb_parts: Le nombre de part du foyer
    """

    impot = calcul_impot(revenu, nb_parts)
    print(
        f"Avec un revenu de {revenu:6}€ et {nb_parts} parts, un foyer paiera {impot}€"
    )


def saisir_un_foyer():
    try:
        revenu = abs(int(input("Revenu du foyer : ")))
        nb_parts = abs(float(input("Nombre de part(s) du foyer : ")))
        print(f"-> Un foyer avec {revenu=}€ et {nb_parts=} à bien été créé")
    except:
        revenu = -1
        nb_parts = 0
        print("-> Fin de la saisie des foyers")
    return revenu, nb_parts


les_revenus = [25000, 80000, 130000, 75000, 500, 30000]
les_parts = [2, 3, 4, 3, 1, 5]


rev, parts = saisir_un_foyer()
while rev != -1:
    les_revenus.append(rev)
    les_parts.append(parts)
    rev, parts = saisir_un_foyer()

for i in range(len(les_revenus)):
    afficher_foyer(les_revenus[i], les_parts[i])
