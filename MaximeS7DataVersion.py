from pycsp3 import *
import pandas as pd

data = pd.read_csv('testdata.csv', delimiter=";")
donnees=data.values

nbEleve = len(donnees)
eleves =[]
elevesNotes = []
elevesChoix = []

#Ajout des eleves
for i in range(nbEleve):
    eleves.append(donnees[i][0])

#Ajout des notesEleves
for i in range(nbEleve):
    elevesNotes.append([donnees[i][1],donnees[i][2]])

#Ajout des choix des eleves
#for i in range(nbEleve):
#   eleveChoix.append([donnees[i][3],donnees[i][4], donnees[i][5]])

#Ajout des choix des eleves si String
for i in range(nbEleve):
    choix=[3,3,3,3,3,3]
    for j in range(3):
        if (donnees[i][j+3]=="LD"):
            choix[0] = j
        if (donnees[i][j+3]=="SE"):
            choix[1] = j
        if (donnees[i][j + 3] == "BIO"):
            choix[2] = j
        if (donnees[i][j + 3] == "CSS"):
            choix[3] = j
        if (donnees[i][j + 3] == "EOC"):
            choix[4] = j
        if (donnees[i][j + 3] == "NRJ"):
            choix[5] = j
    elevesChoix.append(choix)

#Ajout des choix des eleves random
# choixPossibilite = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
# for i in range(nbEleve):
#    eleveChoix.append(choixPossibilite[randint(0,5)])


# Les options
options = LD, SE, BIO, CSS, EOC, NRJ = 0, 1, 2, 3, 4, 5
nbOptions = len(options)

# Les places de optionss
optionsPlaces = [50, 50, 50, 50, 50, 50]

# Les eleves
elevesV = VarArray(size=[nbEleve,nbOptions], dom={0, 1})

# Var choix
choixV = VarArray(size=nbEleve, dom=range(nbOptions))

#var moyenne
moyenneV = VarArray(size=nbEleve, dom=range(20))

#score pour optimisation
score = Var(dom=range(10000))

#Set de coefs des notes pour chaque option
coefsOptions = [[2, 1], [1, 1], [1, 3], [1, 1], [1,1], [1,1]]

#Set de moyennes coeficientés par option pour chaque eleve
elevesMoyenneOptions = []
for i in range(nbEleve):
    elevesMoyenneOptions.append([])


#Calcul des moyennes coeficcientees pour chaque eleve
for y in range(nbOptions):
    for i in range(nbEleve):
        moyenne = 0
        for x in range(len(elevesNotes[0])):
            moyenne += elevesNotes[i][x] * coefsOptions[y][x]
        moyenne = round(moyenne / sum(coefsOptions[y]), 2)
        elevesMoyenneOptions[i].append(round(moyenne))

#Le coef du choix doit etre negatif
coefChoix = -5
#Le coef du choix doit etre positif
coefMoyenne = 1

satisfy(
    [Sum(elevesV[x][i] for x in range(nbEleve)) <= optionsPlaces[i] for i in range(nbOptions)],
    [choixV[i]==Sum(elevesV[i]*elevesChoix[i]) for i in range(nbEleve)],
    [Sum(elevesV[i])==1 for i in range(nbEleve)],
    [moyenneV[i]==Sum(elevesV[i]*elevesMoyenneOptions[i]) for i in range(nbEleve)],
    score==(Sum(choixV))*coefChoix+Sum(moyenneV)*coefMoyenne
)

maximize(
    score
)