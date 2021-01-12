from random import randint

import numpy as np;
import pandas as pd;

data = pd.read_csv('testdata.csv', delimiter=";")
donnees=data.values

nbEleve = len(donnees)
eleves =[]
eleveNotes = []
eleveChoix = []

#Ajout des eleves
for i in range(nbEleve):
    eleves.append(donnees[i][0])

#Ajout des notesEleves
for i in range(nbEleve):
    eleveNotes.append([donnees[i][1],donnees[i][2]])

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
    eleveChoix.append(choix)

#Ajout des choix des eleves random
# choixPossibilite = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
# for i in range(nbEleve):
#    eleveChoix.append(choixPossibilite[randint(0,5)])


print(len(eleves))
