import pandas as pd

#Les options
options = LD, SE, BIO, CSS, EOC, NRJ = 0, 1, 2, 3, 4, 5
nbOptions = len(options)

data = pd.read_csv('testdata.csv', delimiter=";")
donnees=data.values

nbEleves = len(donnees)
eleves =[]
elevesNotes = []
elevesChoix = []

#Ajout des eleves
for i in range(nbEleves):
    eleves.append(donnees[i][0])

#Ajout des notesEleves
for i in range(nbEleves):
    elevesNotes.append([donnees[i][1],donnees[i][2]])

#Ajout des choix des eleves
#for i in range(nbEleve):
#   eleveChoix.append([donnees[i][3],donnees[i][4], donnees[i][5]])

#Ajout des choix des eleves si String
for i in range(nbEleves):
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


#Les places de optionss
optionsPlaces = [50, 50, 50, 50, 50, 50]

#Set de coefs des notes pour chaque option
coefsOptions = [[2, 1], [1, 1], [1, 3], [1, 1], [1,1], [1,1]]

#Set de moyennes coeficientés par option pour chaque eleve
elevesMoyenneOptions = []
for i in range(nbEleves):
    elevesMoyenneOptions.append([])

#Calcul des moyennes coeficcientees pour chaque eleve
for y in range(nbOptions):
    for i in range(nbEleves):
        moyenne = 0
        for x in range(len(elevesNotes[0])):
            moyenne += elevesNotes[i][x] * coefsOptions[y][x]
        moyenne = round(moyenne / sum(coefsOptions[y]), 2)
        elevesMoyenneOptions[i].append(moyenne)

elevesFull=[]
for i in range(nbEleves) :
    eleveData = []
    eleveData.append(eleves[i])
    eleveData.append(elevesMoyenneOptions[i])
    eleveData.append(elevesChoix[i])
    elevesFull.append(eleveData)

elevesRestant = elevesFull.copy()
optionsRemplis = [[],[],[],[],[],[]]

#1er tour
for i in range(len(elevesFull)) :
    optionsRemplis[elevesFull[i][2][0]].append(elevesFull[i])
    elevesRestant.remove(elevesFull[i])

#On classe dans l'ordre des moyennes par options :

for op in range(len(options)) :
    n = len(optionsRemplis[op])
    #    Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n - i - 1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if optionsRemplis[op][j][1][op] < optionsRemplis[op][j+1][1][op] :
                optionsRemplis[op][j], optionsRemplis[op][j + 1] = optionsRemplis[op][j + 1], optionsRemplis[op][j]

print("=====LD======")
print(optionsRemplis[0])
print("=====SE======")
print(optionsRemplis[1])
print("=====BIO======")
print(optionsRemplis[2])
print("=====CSS======")
print(optionsRemplis[3])
print("=====EOC======")
print(optionsRemplis[4])
print("=====NRJ======")
print(optionsRemplis[5])
#On coupe :
for i in range(len(optionsRemplis)) :
    while len(optionsRemplis[i]) > optionsPlaces[i] :
        elevesRestant.append(optionsRemplis[i].pop())

print("=====RESTANT======")
print(elevesRestant)

elevesRestantAvant = []
index=0

#Second choix
while(len(elevesRestant)!=0 and elevesRestantAvant!=elevesRestant) :
    elevesRestantAvant = elevesRestant.copy()

    for index in range(len(elevesRestantAvant)) :
        optionsRemplis[elevesRestantAvant[index][2][1]].append(elevesRestantAvant[index])
        elevesRestant.remove(elevesRestantAvant[index])

    # On classe dans l'ordre des moyennes par options :

    for op in range(nbOptions):
        n = len(optionsRemplis[op])
        #    Traverser tous les éléments du tableau
        for i in range(n):
            for j in range(0, n - i - 1):
                # échanger si l'élément trouvé est plus grand que le suivant
                if optionsRemplis[op][j][1][op] < optionsRemplis[op][j + 1][1][op]:
                    optionsRemplis[op][j], optionsRemplis[op][j + 1] = optionsRemplis[op][j + 1], optionsRemplis[op][j]

    # On coupe :
    for i in range(len(optionsRemplis)):
        while len(optionsRemplis[i]) > optionsPlaces[i]:
            elevesRestant.append(optionsRemplis[i].pop())



print("___________2EME_TOUR______________")
print("=====LD======")
print(optionsRemplis[0])
print("=====SE======")
print(optionsRemplis[1])
print("=====BIO======")
print(optionsRemplis[2])
print("=====CSS======")
print(optionsRemplis[3])
print("=====EOC======")
print(optionsRemplis[4])
print("=====NRJ======")
print(optionsRemplis[5])
print(elevesRestant)

#Troisieme choix
while(len(elevesRestant)!=0 and elevesRestantAvant!=elevesRestant) :
    elevesRestantAvant = elevesRestant.copy()

    for index in range(len(elevesRestantAvant)) :
        optionsRemplis[elevesRestantAvant[index][2][2]].append(elevesRestantAvant[index])
        elevesRestant.remove(elevesRestantAvant[index])

    # On classe dans l'ordre des moyennes par options :

    for op in range(nbOptions):
        n = len(optionsRemplis[op])
        #    Traverser tous les éléments du tableau
        for i in range(n):
            for j in range(0, n - i - 1):
                # échanger si l'élément trouvé est plus grand que le suivant
                if optionsRemplis[op][j][1][op] < optionsRemplis[op][j + 1][1][op]:
                    optionsRemplis[op][j], optionsRemplis[op][j + 1] = optionsRemplis[op][j + 1], optionsRemplis[op][j]

    # On coupe :
    for i in range(len(optionsRemplis)):
        while len(optionsRemplis[i]) > optionsPlaces[i]:
            elevesRestant.append(optionsRemplis[i].pop())



print("___________3EME_TOUR______________")
print("=====LD======")
print(optionsRemplis[0])
print("=====SE======")
print(optionsRemplis[1])
print("=====BIO======")
print(optionsRemplis[2])
print("=====CSS======")
print(optionsRemplis[3])
print("=====EOC======")
print(optionsRemplis[4])
print("=====NRJ======")
print(optionsRemplis[5])
print("=====RESTANT======")
print(elevesRestant)