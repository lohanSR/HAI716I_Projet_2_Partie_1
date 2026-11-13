# Journal de bord : tournoi du dilemme du prisonnier itéré

## Vendredi 13/11/2026 : mise en place

- Langage : **Python**.
- Structure du projet :
  - `src/moteur.py` : matrice des gains, partie, rencontre, tournoi
  - `src/strategies.py` : les stratégies
  - `main.py` : lancement des tournois
  - `resultats/` : sorties et graphiques

## Stratégies (`src/strategies.py`)

- `Strategie` : interface qui définit les comportements de base d'une stratégie : jouer et réinitialiser (pour certaines stratégies).
- `jouer()` reçoit tout l'historique de la partie et pas seulement le dernier coup : TESTER a besoin du coup du tour 2, et certaines stratégies de l'étape 2 (GRIM, TF2T) ont besoin de plus que le dernier coup.
- `AllD` : fait toujours défection, quels que soient les coups passés de l'adversaire.
- `TFT` : coopère au premier tour, puis rejoue le dernier coup de l'adversaire.
