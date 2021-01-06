from pycsp3 import *

# Les options
options = LD, SE, BIO = 0, 1, 2

# Les places de optionss
optionsPlaces = [4, 4, 2]

# Les eleves
elevesV = VarArray(size=[8,3], dom={0, 1})

# Var choix
choixV = VarArray(size=8, dom=range(3))

#var moyenne
moyenneV = VarArray(size=8, dom=range(20))

#score pour optimisation
score = Var(dom=range(10000))

# Set de choix pour chaque eleve, l'option 1ere est indiqué par 0,n la deuxieme par 1 etc etc...
elevesChoix = [[2, 1, 0], [0, 1, 2], [0, 1, 2], [1, 2, 0], [1, 2, 0], [0, 2, 1], [1, 0, 2], [1, 0, 2]]

#Set de notes pour chaque eleve
elevesNotes = [[15, 15], [12, 18], [20, 4], [12, 13], [9, 8], [17, 18], [5, 19], [16, 11]]

#Set de coefs des notes pour chaque option
coefsOptions = [[2, 1], [1, 1], [1, 3]]

#Set de moyennes coeficientés par option pour chaque eleve
elevesMoyenneOptions = [[], [], [], [], [], [], [], []]

#Calcul des moyennes coeficcientees pour chaque eleve
for y in range(len(options)):
    for i in range(8):
        moyenne = 0
        for x in range(len(elevesNotes[0])):
            moyenne += elevesNotes[i][x] * coefsOptions[y][x]
        moyenne = round(moyenne / sum(coefsOptions[y]), 2)
        elevesMoyenneOptions[i].append(round(moyenne))

coefChoix = 1
coefMoyenne = 1

satisfy(
    [Sum(elevesV[x][i] for x in range(8)) <= optionsPlaces[i] for i in range(len(options))],
    [choixV[i]==Sum(elevesV[i]*elevesChoix[i]) for i in range(8)],
    [Sum(elevesV[i])==1 for i in range(8)],
    [moyenneV[i]==Sum(elevesV[i]*elevesMoyenneOptions[i]) for i in range(8)],
    score==Sum(choixV)*coefChoix+Sum(moyenneV)*coefMoyenne
)

maximize(
    score
)