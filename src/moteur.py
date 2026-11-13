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