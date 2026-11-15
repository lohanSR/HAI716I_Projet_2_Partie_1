# HAI716I Projet 2 (partie 1) : tournoi du dilemme du prisonnier itéré

Moteur de tournoi du dilemme du prisonnier itéré, au format d'Axelrod : chaque stratégie affronte chaque autre sur 5 parties de 200 tours, et le meilleur score total gagne. La graine est fixée (42), les résultats se relancent à l'identique.

## Prérequis

Python 3.9 ou plus récent, sans dépendance externe.

## Relancer chaque tournoi

Toutes les commandes se lancent depuis la racine du dépôt.

| Tournoi | Commande |
|---|---|
| Étape 1 : tournoi de base (5 stratégies du cours) | `python3 main.py etape1` |
| Étape 2 : population élargie (+ GRIM et PAVLOV) | `python3 main.py etape2` |
| Étape 3 : bruit (5 % d'erreurs) | `python3 main.py etape2 --mode bruit` |
| Étape 3 : sélection (100 générations) | `python3 main.py etape2 --mode selection` |
| Étape 3 : autres gains (chasse au cerf) | `python3 main.py etape2 --mode cerf` |
| Étape 3 : horizon inconnu | `python3 main.py etape2 --mode horizon` |

Pour enregistrer la sortie en même temps, ajouter par exemple `| tee resultats/etape1.txt`.

`python3 main.py --help` affiche la liste des étapes et des modes disponibles.

## Structure

- `main.py` : lancement des tournois et affichage des résultats
- `src/moteur.py` : matrice des gains, partie, rencontre, tournoi, classement, sélection
- `src/strategies.py` : les stratégies (ALL-D, TIT-FOR-TAT, RANDOM, JOSS, TESTER, GRIM, PAVLOV)
- `resultats/` : sorties et captures d'écran de chaque tournoi
- `JOURNAL_MAHDI.md`, `JOURNAL_SERRE.md` : journaux de bord
