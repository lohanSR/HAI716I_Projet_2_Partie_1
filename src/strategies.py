class Strategie:
    """Classe de base de toutes les stratégies.

    Le moteur doit :
    - appeler reinitialiser() au début de chaque partie ;
    - appeler jouer(mon_historique, historique_adverse, alea) à chaque tour, où
      mon_historique et historique_adverse sont des listes de 'C'/'D' (coups
      passés de la partie en cours, vides au premier tour) et alea est un
      random.Random fourni par le moteur ;
    - recevoir 'C' ou 'D' en retour.
    """

    def __init__(self, nom):
        self.nom = nom

    def jouer(self, mon_historique, historique_adverse, alea):
        raise NotImplementedError("Chaque stratégie doit définir jouer()")

    def reinitialiser(self):
        pass


class AllD(Strategie):

    def __init__(self, nom="ALL-D"):
        super().__init__(nom)

    def jouer(self, mon_historique, historique_adverse, alea):
        return 'D'


class TFT(Strategie):

    def __init__(self, nom="TIT-FOR-TAT"):
        super().__init__(nom)

    def jouer(self, mon_historique, historique_adverse, alea):
        if len(historique_adverse) == 0:
            return 'C'

        return historique_adverse[-1]


class Random(Strategie):

    def __init__(self, nom="RANDOM"):
        super().__init__(nom)

    def jouer(self, mon_historique, historique_adverse, alea):
        if (alea.random() < 0.5):
            return 'C'

        return 'D'


class Joss(TFT):

    def __init__(self, nom="JOSS"):
        super().__init__(nom)

    def jouer(self, mon_historique, historique_adverse, alea):
        coup = super().jouer(mon_historique, historique_adverse, alea)

        if coup == 'C' and alea.random() < 0.1:
            return 'D'
        return coup


class Tester(Strategie):
    """D au premier tour. Si l'adversaire riposte (a déjà joué D), joue
    TIT-FOR-TAT ; sinon répète le cycle C, C, D à partir du tour 2."""

    def __init__(self, nom="TESTER"):
        super().__init__(nom)

    def jouer(self, mon_historique, historique_adverse, alea):
        tour = len(mon_historique)

        # Premier tour : on teste l'adversaire
        if tour == 0:
            return 'D'

        # L'adversaire a riposté au moins une fois -> mode TFT
        if 'D' in historique_adverse:
            return historique_adverse[-1]

        # Sinon, cycle C, C, D
        if (tour - 1) % 3 == 2:
            return 'D'
        return 'C'
