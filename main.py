import argparse

from src.strategies import AllD, TFT, Random, Joss, Tester, Grim, Pavlov
from src.moteur import tournoi, classement, GAINS_CERF

NB_PARTIES = 5
NB_TOURS = 200
GRAINE = 42

def population_etape1():

    return [AllD(), TFT(), Random(), Joss(), Tester()]


def population_etape2():

    return population_etape1() + [Grim(), Pavlov()]


POPULATIONS = {
    "etape1": population_etape1,
    "etape2": population_etape2,
}

# Modifications du tournoi (étape 3) : paramètres passés à tournoi()
MODES = {
    "normal": {},
    "cerf": {"gains": GAINS_CERF},
    "horizon": {"w": 0.99},
}


def afficher_classement(resultats):

    for rang, (score, nom) in enumerate(resultats, start=1):
        print(f"{rang}. {nom:<12} {score:>6}")


def afficher_matrice(population, matrice_scores):

    noms = [strategie.nom for strategie in population]

    print("Matrice des scores (ligne = score obtenu contre la colonne) :")

    print(" " * 12 + "".join(f"{nom:>13}" for nom in noms))

    for i, nom in enumerate(noms):
        cases = ""
        for j, score in enumerate(matrice_scores[i]):
            cases += f"{'-' if i == j else score:>13}"
        print(f"{nom:<12}{cases}")


def main():

    parser = argparse.ArgumentParser(description="Tournoi du dilemme du prisonnier itéré")
    parser.add_argument("etape", choices=POPULATIONS.keys(), help="population à utiliser")
    parser.add_argument("--mode", choices=MODES.keys(), default="normal",
                        help="modification du tournoi (défaut : normal)")
    arguments = parser.parse_args()
    etape, mode = arguments.etape, arguments.mode

    population = POPULATIONS[etape]()
    matrice_scores = tournoi(population, NB_PARTIES, NB_TOURS, GRAINE, **MODES[mode])
    resultats = classement(population, matrice_scores)

    print(f"Étape : {etape}, mode : {mode}")
    print(f"Nombre de parties : {NB_PARTIES}, nombre de tours : {NB_TOURS}, graine : {GRAINE}")
    afficher_classement(resultats)
    print()
    afficher_matrice(population, matrice_scores)


if __name__ == "__main__":
    main()