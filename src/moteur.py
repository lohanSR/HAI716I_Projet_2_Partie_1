from random import randint


GAINS = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (2, 2) 
}

def jouer_partie(strat1, strat2, nb_tours):
    """
    """
    hist1, hist2 = [], []
    score1, score2 = 0, 0

    for _ in range(nb_tours):
        coup1 = strat1 # Choix du coup pour la stratégie 1
        coup2 = strat2 # Choix du coup pour la stratégie 2

        gain1, gain2 = GAINS[(coup1, coup2)]
        score1 += gain1
        score2 += gain2

        # Mise à jour mémoire stratégies, donne l'historique des coups
        # strat1
        # strat2

        hist1.append(coup1)
        hist2.append(coup2)

    return (score1, score2), (hist1, hist2)

def jouer_rencontre(strat1, strat2, nb_parties, nb_tours):
    """
    """
    total_score1, total_score2 = 0, 0

    for _ in range(nb_parties):
        (score1, score2), _ = jouer_partie(strat1, strat2, nb_tours)
        total_score1 += score1
        total_score2 += score2

    return total_score1, total_score2

def tournoi(population, nb_parties, nb_tours):
    n = len(population)
    matrice_scores = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            score_i, score_j = jouer_rencontre(population[i], population[j], nb_parties, nb_tours)
            matrice_scores[i][j] = score_i
            matrice_scores[j][i] = score_j

    return matrice_scores

            