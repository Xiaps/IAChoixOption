import pandas as pd

#Les options
options = LD, SE, BIO, CSS, EOC, NRJ = 0, 1, 2, 3, 4, 5
nbOptions = len(options)

data = pd.read_csv('testdata80.csv', delimiter=";")
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
    choix=[0,0,0,0,0,0]
    for j in range(3):
        if (donnees[i][j+3]=="LD"):
            choix[j] = 0
        if (donnees[i][j+3]=="SE"):
            choix[j] = 1
        if (donnees[i][j + 3] == "BIO"):
            choix[j] = 2
        if (donnees[i][j + 3] == "CSS"):
            choix[j] = 3
        if (donnees[i][j + 3] == "EOC"):
            choix[j] = 4
        if (donnees[i][j + 3] == "NRJ"):
            choix[j] = 5
    elevesChoix.append(choix)

#Ajout des choix des eleves random
# choixPossibilite = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
# for i in range(nbEleve):
#    eleveChoix.append(choixPossibilite[randint(0,5)])


#Les places de optionss
optionsPlaces = [18, 18, 12, 12, 18, 12]

#Set de coefs des notes pour chaque option
coefsOptions = [[1, 2], [1, 2], [2, 1], [1, 2], [2,1], [2,1]]

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

print("=====LD======"+str(len(optionsRemplis[0]))+" élèves")
print(optionsRemplis[0])
print("=====SE======"+str(len(optionsRemplis[1]))+" élèves")
print(optionsRemplis[1])
print("=====BIO======"+str(len(optionsRemplis[2]))+" élèves")
print(optionsRemplis[2])
print("=====CSS======"+str(len(optionsRemplis[3]))+" élèves")
print(optionsRemplis[3])
print("=====EOC======"+str(len(optionsRemplis[4]))+" élèves")
print(optionsRemplis[4])
print("=====NRJ======"+str(len(optionsRemplis[5]))+" élèves")
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
print("=====LD======"+str(len(optionsRemplis[0]))+" élèves")
print(optionsRemplis[0])
print("=====SE======"+str(len(optionsRemplis[1]))+" élèves")
print(optionsRemplis[1])
print("=====BIO======"+str(len(optionsRemplis[2]))+" élèves")
print(optionsRemplis[2])
print("=====CSS======"+str(len(optionsRemplis[3]))+" élèves")
print(optionsRemplis[3])
print("=====EOC======"+str(len(optionsRemplis[4]))+" élèves")
print(optionsRemplis[4])
print("=====NRJ======"+str(len(optionsRemplis[5]))+" élèves")
print(optionsRemplis[5])
print("=====RESTANT======")
print(elevesRestant)

elevesRestantAvant2 = []

#Troisieme choix
while(len(elevesRestant)!=0 and elevesRestantAvant2!=elevesRestant) :
    elevesRestantAvant2 = elevesRestant.copy()

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
print("=====LD======"+str(len(optionsRemplis[0]))+" élèves")
print(optionsRemplis[0])
print("=====SE======"+str(len(optionsRemplis[1]))+" élèves")
print(optionsRemplis[1])
print("=====BIO======"+str(len(optionsRemplis[2]))+" élèves")
print(optionsRemplis[2])
print("=====CSS======"+str(len(optionsRemplis[3]))+" élèves")
print(optionsRemplis[3])
print("=====EOC======"+str(len(optionsRemplis[4]))+" élèves")
print(optionsRemplis[4])
print("=====NRJ======"+str(len(optionsRemplis[5]))+" élèves")
print(optionsRemplis[5])
print("=====RESTANT======")
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
print("=====LD======"+str(len(optionsRemplis[0]))+" élèves")
print(optionsRemplis[0])
print("=====SE======"+str(len(optionsRemplis[1]))+" élèves")
print(optionsRemplis[1])
print("=====BIO======"+str(len(optionsRemplis[2]))+" élèves")
print(optionsRemplis[2])
print("=====CSS======"+str(len(optionsRemplis[3]))+" élèves")
print(optionsRemplis[3])
print("=====EOC======"+str(len(optionsRemplis[4]))+" élèves")
print(optionsRemplis[4])
print("=====NRJ======"+str(len(optionsRemplis[5]))+" élèves")
print(optionsRemplis[5])
print("=====RESTANT======")
print(elevesRestant)


scoreMoyenne = 0
scoreChoix = 0
coefMoyenn = 1
coefChoix = -5

for i in range(len(optionsRemplis)):
    for j in range(len(optionsRemplis[i])):
        scoreMoyenne += optionsRemplis[i][j][1][i]


for i in range(len(optionsRemplis)):
    for j in range(len(optionsRemplis[i])):
        scoreChoix += optionsRemplis[i][j][2].index(i)

score=scoreChoix*coefChoix+scoreMoyenne*coefMoyenn

print(scoreChoix)
print(scoreMoyenne)
print("¤¤¤ Score final : ¤¤¤")
print(score)

resultat=[["Prenom"],["Option attribuee"],["Rang du choix"],["Moyenne dans l'option"]]
optionsString =["LD","SE","BIO","CSS","EOC","NRJ"]
choixString = ["Premier choix","Deuxieme choix","Troisieme choix"]



for i in range(len(optionsRemplis)):
    for j in range(len(optionsRemplis[i])):
        resultat[0].append(optionsRemplis[i][j][0])
        resultat[1].append(optionsString[i])

        rangChoix= optionsRemplis[i][j][2].index(i)
        resultat[2].append(choixString[rangChoix])


        resultat[3].append(optionsRemplis[i][j][1][i])



print(resultat)
