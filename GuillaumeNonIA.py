# Les options
options = LD, SE, BIO = 0, 1, 2

# Les places de optionss
optionsPlaces = [4, 4, 2]

# Les eleves
eleves = "Guillaume", "Maxime", "Alban", "Roger", "Manu", "Morgane", "Vegeta", "Clara"

# Set de choix pour chaque eleve
#elevesChoix = [[2, 1, 0], [0, 1, 2], [0, 1, 2], [1, 2, 0], [1, 2, 0], [0, 2, 1], [1, 0, 2], [1, 0, 2]]
elevesChoix = [[2, 1, 0], [0, 1, 2], [0, 1, 2], [2, 0, 1], [2, 0, 1], [0, 2, 1], [1, 0, 2], [1, 0, 2]]

# La suite n'est pas encore utilise (jusqu'au satisfy)

# Set de notes pour chaque eleve
elevesNotes = [[15, 15], [12, 18], [20, 4], [12, 13], [9, 8], [17, 18], [5, 19], [16, 11]]

# Set de coefs des notes pour chaque option
coefsOptions = [[2, 1], [1, 1], [1, 3]]

# Set de moyennes coeficientés par option pour chaque eleve
elevesMoyenneOptions = [[], [], [], [], [], [], [], []]

# Calcul des moyennes coeficcientees pour chaque eleve
for y in range(len(options)):
    for i in range(len(eleves)):
        moyenne = 0
        for x in range(len(elevesNotes[0])):
            moyenne += elevesNotes[i][x] * coefsOptions[y][x]
        moyenne = round(moyenne / sum(coefsOptions[y]), 2)
        elevesMoyenneOptions[i].append(round(moyenne))

elevesFull = []
for i in range(len(eleves)):
    eleveData = []
    eleveData.append(eleves[i])
    eleveData.append(elevesMoyenneOptions[i])
    eleveData.append(elevesChoix[i])
    elevesFull.append(eleveData)

elevesRestant = elevesFull.copy()
optionsRemplis = [[], [], []]

# 1er tour
for i in range(len(elevesFull)):
    optionsRemplis[elevesFull[i][2][0]].append(elevesFull[i])
    elevesRestant.remove(elevesFull[i])

# On classe dans l'ordre des moyennes par options :

for op in range(len(options)):
    n = len(optionsRemplis[op])
    #    Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n - i - 1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if optionsRemplis[op][j][1][op] < optionsRemplis[op][j + 1][1][op]:
                optionsRemplis[op][j], optionsRemplis[op][j + 1] = optionsRemplis[op][j + 1], optionsRemplis[op][j]

print("=====LD======")
print(optionsRemplis[0])
print("=====SE======")
print(optionsRemplis[1])
print("=====BIO======")
print(optionsRemplis[2])
# On coupe :
for i in range(len(optionsRemplis)):
    while len(optionsRemplis[i]) > optionsPlaces[i]:
        elevesRestant.append(optionsRemplis[i].pop())

print("=====RESTANT======")
print(elevesRestant)

elevesRestantAvant = []
index = 0

# Second choix
while (len(elevesRestant) != 0 and elevesRestantAvant != elevesRestant):
    elevesRestantAvant = elevesRestant.copy()

    for index in range(len(elevesRestantAvant)):
        optionsRemplis[elevesRestantAvant[index][2][1]].append(elevesRestantAvant[index])
        elevesRestant.remove(elevesRestantAvant[index])

    # On classe dans l'ordre des moyennes par options :

    for op in range(len(options)):
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
print("=====RESTANT======")
print(elevesRestant)

# Troisieme choix
while (len(elevesRestant) != 0 and elevesRestantAvant != elevesRestant):
    elevesRestantAvant = elevesRestant.copy()

    for index in range(len(elevesRestantAvant)):
        optionsRemplis[elevesRestantAvant[index][2][2]].append(elevesRestantAvant[index])
        elevesRestant.remove(elevesRestantAvant[index])

    # On classe dans l'ordre des moyennes par options :

    for op in range(len(options)):
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