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
- `jouer()` reçoit tout l'historique de la partie et pas seulement le dernier coup : TESTER doit savoir si l'adversaire a déjà joué D, et certaines stratégies de l'étape 2 (GRIM, TF2T) ont besoin de plus que le dernier coup.
- `AllD` : fait toujours défection, quels que soient les coups passés de l'adversaire.
- `TFT` : coopère au premier tour, puis rejoue le dernier coup de l'adversaire.
- `Random` : joue C ou D avec une chance sur deux, sans regarder l'historique. Le tirage passe par `alea`, fourni par le moteur, pour que la graine fixe tout.
- `Joss` : hérite de `TFT`. Quand TFT coopérerait, joue D avec une probabilité de 10 %.
- `Tester` : D au premier tour pour tester l'adversaire. Si l'adversaire a déjà joué D au moins une fois, passe en TIT-FOR-TAT, sinon répète le cycle C, C, D à partir du tour 2.
- Interprétation de "riposter" pour TESTER : la diapositive est ambiguë. J'ai choisi "l'adversaire a joué D au moins une fois", comme le TESTER original d'Axelrod, plutôt que "l'adversaire répond à un D de TESTER par un D au tour suivant". Les deux lectures donnent le même résultat contre ALL-D et TFT, mais pas contre RANDOM et JOSS.
- Différence avec l'original : le TESTER d'Axelrod s'excuse en jouant C au moment de passer en TFT. La version du cours ne le fait pas, donc TESTER et TFT se punissent en écho (D C D C… contre C D C D…) et ne reviennent jamais à la coopération.

## Prédiction avant le lancement de `main.py`

Qui aura le plus de points dans chaque duel :

| | ALL-D | TFT | RANDOM | JOSS | TESTER |
|---|---|---|---|---|---|
| **ALL-D** | - | ALL-D | ALL-D | ALL-D | égalité |
| **TFT** | ALL-D | - | proche | égalité | TESTER |
| **RANDOM** | ALL-D | proche | - | proche | TESTER |
| **JOSS** | ALL-D | égalité | proche | - | TESTER |
| **TESTER** | égalité | TESTER | TESTER | TESTER | - |

ALL-D gagnera des points contre RANDOM et ne perd jamais un duel, mais la plupart du temps il ne prend que 2 points par tour. TFT et JOSS sont équilibrés l'un contre l'autre : même si JOSS trahit, il en subit les conséquences ; la plupart du temps 3 points, parfois 2. Même chose pour TESTER, qui gagne plus que les autres contre RANDOM puisqu'il a plus de chances de gagner le premier tour ; sinon, il joue comme TFT. RANDOM perdra le plus de points contre ALL-D, et moins contre TESTER, TFT et JOSS.

Classement attendu :

1. ALL-D
2. JOSS
3. TESTER
4. TFT
5. RANDOM

TFT gagnera-t-il ? Non, je pense que TFT ne finira pas 1er : ALL-D remportera le tournoi grâce à ses points contre RANDOM. Il sera difficile de départager JOSS, TESTER et TFT, car les trois se comportent presque de la même façon : JOSS hérite de TFT, et TESTER joue comme TFT dès que l'adversaire a trahi.
