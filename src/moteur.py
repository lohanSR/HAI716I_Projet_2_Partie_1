
import random

from src.strategies import Strategie

GAINS = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (2, 2) 
}

GAINS_CERF = {
    ('C', 'C'): (4, 4),
    ('C', 'D'): (0, 3),
    ('D', 'C'): (3, 0),
    ('D', 'D'): (1, 1)
}

def jouer_partie(strat1: Strategie, strat2: Strategie, nb_tours: int, alea: random.Random, gains=GAINS, w=None):
    """
    Joue une partie pour un nombre de tours fixé entre deux stratégies
    """
    strat1.reinitialiser()
    strat2.reinitialiser()

    hist1, hist2 = [], []
    score1, score2 = 0, 0

    tour = 0

    if w is not None and not (0 <= w < 1):
        raise ValueError("w doit être compris entre 0 inclus et 1 exclu")

    while w is not None or tour < nb_tours:
        coup1 = strat1.jouer(hist1, hist2, alea)
        coup2 = strat2.jouer(hist2, hist1, alea)

        gain1, gain2 = gains[(coup1, coup2)]
        score1 += gain1
        score2 += gain2

        hist1.append(coup1)
        hist2.append(coup2)

        tour += 1

        if w is not None and alea.random() >= w:
            break

    return (score1, score2), (hist1, hist2)

def jouer_rencontre(strat1: Strategie, strat2: Strategie, nb_parties: int, nb_tours: int, graine: str, gains=GAINS, w=None):
    """
    Joue une rencontre complète entre deux stratégies sur plusieurs parties
    """
    total_score1, total_score2 = 0, 0

    for k in range(nb_parties):
        alea_partie = random.Random(f"{graine}-{k}")
        (score1, score2), _ = jouer_partie(strat1, strat2, nb_tours, alea_partie, gains, w)
        total_score1 += score1
        total_score2 += score2

    return total_score1, total_score2

def tournoi(population: list[Strategie], nb_parties: int, nb_tours: int, graine=42, gains=GAINS, w=None):
    """
    Organise un tournoi entre les stratégies, chaque stratégie affronte toutes les autres stratégies
    """
    n = len(population)
    matrice_scores = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            graine_rencontre = f"{graine}-{i}-{j}"
            score_i, score_j = jouer_rencontre(population[i], population[j], nb_parties, nb_tours, graine_rencontre, gains, w)
            matrice_scores[i][j] = score_i
            matrice_scores[j][i] = score_j

    return matrice_scores

def classement(population: list[Strategie], matrice_scores: list[list[int]]):
    """
    Calcule le score total de chaque participant et génère le classement final
    """
    scores_totaux = []

    for i in range(len(population)):
        score_total = sum(matrice_scores[i])
        nom_strategie = getattr(population[i], "nom")
        scores_totaux.append((score_total, nom_strategie))

    scores_totaux.sort(reverse=True, key=lambda x: x[0])
    return scores_totaux
