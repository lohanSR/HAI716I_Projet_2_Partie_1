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

    def __init__(self):
        super().__init__("ALL-D")

    def jouer(self, mon_historique, historique_adverse, alea):
        return 'D'


class TFT(Strategie):

    def __init__(self):
        super().__init__("TIT-FOR-TAT")

    def jouer(self, mon_historique, historique_adverse, alea):
        if len(historique_adverse) == 0:
            return 'C'

        return historique_adverse[-1]

