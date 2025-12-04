compteur = 0


def est_divisible(n, p):
    """
    Renvoie vrai si et seulement si n est divisible par p.

    Parametres
    ----------
    n, p : deux entiers

    Retour
    -------
    True ou False
    """
    global compteur
    compteur += 1
    return n % p == 0


def get_diviseurs_stricts(n):
    """
    Renvoie la liste des diviseurs stricts de n.
    Parametres
    ----------
    n : un entier

    Retour
    -------
    liste des diviseurs stricts de n (liste d'entiers).
    """
    diviseurs = []
    for p in range(1, n):
        if est_divisible(n, p):
            diviseurs.append(p)
    return diviseurs


def est_parfait(n):
    """Renvoie vrai si et seulement si n est un nombre parfait.
    Parametres
    ----------
    n : un entier

    Retour
    -------
    Vrai ou Faux
    """
    diviseurs = get_diviseurs_stricts(n)
    somme_diviseurs = sum(diviseurs)
    return n == somme_diviseurs


### Programme principal

if __name__ == "__main__":
    print("Début des tests...")
    print("-> Tests de est_divisible")
    assert not est_divisible(24, 10)
    assert est_divisible(15, 5)
    assert est_divisible(941, 941)
    assert est_divisible(45, 1)
    assert not est_divisible(48, 13)

    print("-> Tests de get_diviseurs_stricts")
    assert get_diviseurs_stricts(18) == [1, 2, 3, 6, 9]
    assert get_diviseurs_stricts(14) == [1, 2, 7]
    assert get_diviseurs_stricts(60) == [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30]

    print("-> Tests de est_parfait")
    assert est_parfait(6)
    assert est_parfait(28)
    assert est_parfait(496)
    assert not est_parfait(2)
    assert not est_parfait(29)

    print("Tous les tests se sont bien passés")
