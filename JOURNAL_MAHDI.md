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

## Étape 1 : résultats

- Protocole : 5 parties de 200 tours, graine 42, sans partie contre soi-même (raison : le sujet dit que "chaque stratégie affronte chaque autre", et un duel contre son propre double ne dit rien de la façon dont une stratégie s'en sort face aux autres, mais ce choix change le vainqueur, voir "TFT gagne-t-il ?").
- Capture d'écran : ![Résultats étape 1](resultats/etape1.png)
- Classement obtenu :
  1. ALL-D :         9554
  2. TESTER :        9074
  3. TIT-FOR-TAT :   9032
  4. JOSS :          8771
  5. RANDOM :        8351

### Comparaison avec la prédiction
- Ce qui était juste : All-d en premier et Random en dernier et l'approche du score de TFT et Tester
- Ce qui était faux : le classement de JOSS, et l'idée que son score serait proche de ceux de TFT et TESTER : il est loin derrière eux. Le problème vient de son score contre TESTER, à cause de ses trahisons occasionnelles, alors que TESTER et TFT ont obtenu ensemble le meilleur résultat parmi les duels sans RANDOM ni ALL-D. J'en déduis qu'être gourmand face à un adversaire imprévisible rapporte le plus, sinon, coopérer tout en punissant la trahison rapporte aussi.

### TFT gagne-t-il ?
- Réponse : Non, All-d gagne.
- Pourquoi le résultat diffère de 1980 :
  - **La population.** En 1980, 15 programmes, dont beaucoup ne trahissaient jamais en premier. Ici, TFT est le seul : il n'a aucun partenaire de coopération durable (écho contre JOSS et TESTER), et ne dépasse jamais 2,5 points par tour.
  - **RANDOM.** ALL-D lui prend 3524 points, environ 1000 de plus que TFT. Sans la colonne RANDOM, ALL-D finirait dernier.
  - **Pas de partie contre soi-même.** En 1980, chaque programme jouait aussi contre son double. Avec ces parties (calcul à part), TFT passe 1er : TFT contre TFT rapporte 3000, ALL-D contre ALL-D 2000.
