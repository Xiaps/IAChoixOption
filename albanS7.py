from pycsp3 import *
import numpy as np

options = LD, SE, BIO = 0, 1, 2

optionsPlaces = [1, 4, 3]

Guillaume, Maxime, Alban, Roger, Manu, Morgane, Vegeta, Clara = eleves = VarArray(size=8, dom=options)
choix = VarArray(size=8, dom=range(len(options)))

elevesChoix = [[2, 1, 0], [2, 1, 0], [2, 1, 0], [1, 2, 0], [1, 2, 0], [1, 2, 0], [0, 1, 2], [0, 1, 2]]


satisfy(
    [Count(eleves, value=options[i]) <= optionsPlaces[i] for i in range(len(options))],
    [((eleves[i] == options[elevesChoix[i][0]]) |
      (eleves[i] == options[elevesChoix[i][1]]) |
      (eleves[i] == options[elevesChoix[i][2]])) for i in range(len(eleves))],
    ##[choix[i] == (elevesChoix[i]).index(eleves[i]) for i in range(len(choix))],
    [choix[i] == (elevesChoix[i]).index(eleves[i]) for i in range(len(choix))]
)

minimize(
    Sum(choix)
)

