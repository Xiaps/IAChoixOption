from pycsp3 import *

# Les options
options = LD, SE, BIO = 0, 1, 2

# Les places de optionss
optionsPlaces = [4, 4, 2]

# Les eleves
eleves = VarArray(size=[8,3], dom={0, 1})

# Var choix
choix = VarArray(size=8, dom=range(3))

# Set de choix pour chaque eleve, l'option 1ere est indiqué par 0,n la deuxieme par 1 etc etc...
elevesChoix = [[2, 1, 0], [0, 1, 2], [0, 1, 2], [1, 2, 0], [1, 2, 0], [0, 2, 1], [1, 0, 2], [1, 0, 2]]


satisfy(
    [Sum(eleves[x][i] for x in range(8)) <= optionsPlaces[i] for i in range(len(options))],
    [choix[i]==Sum(eleves[i]*elevesChoix[i]) for i in range(8)],
    [Sum(eleves[i])==1 for i in range(8)]
)

minimize(
    Sum(choix)
)

maximize(

)
