
import sys

from src.strategies import AllD, TFT, Random, Joss, Tester
from src.moteur import tournoi, classement, GAINS_CERF

NB_PARTIES = 5
NB_TOURS = 200
GRAINE = 42

def population_etape1():

    return [AllD(), TFT(), Random(), Joss(), Tester()]


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

    mode = sys.argv[1] if len(sys.argv) > 1 else "normal"

    population = population_etape1()

    if mode == "cerf":
        matrice_scores = tournoi(population, NB_PARTIES, NB_TOURS, GRAINE, gains=GAINS_CERF)
    elif mode == "horizon":
        matrice_scores = tournoi(population, NB_PARTIES, NB_TOURS, GRAINE, w=0.99)
    elif mode == "normal":
        matrice_scores = tournoi(population, NB_PARTIES, NB_TOURS, GRAINE)
    else:
        print("Mode inconnu : choisir normal, cerf ou horizon")
        return

    resultats = classement(population, matrice_scores)

    print(f"Mode : {mode}")
    print (f"Nombre de parties : {NB_PARTIES}, nombre de tours : {NB_TOURS}, graine : {GRAINE}")
    afficher_classement(resultats)
    print()
    afficher_matrice(population, matrice_scores)


if __name__ == "__main__":
    main()