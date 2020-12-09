from pycsp3 import *

#Les options
options = LD, SE, BIO = 0, 1, 2

#Les places de optionss
optionsPlaces = [4, 4, 2]

#Les eleves
Guillaume, Maxime, Alban, Roger, Manu, Morgane, Vegeta, Clara = eleves = VarArray(size=8, dom=options)

#Set de choix pour chaque eleve
elevesChoix = [[2, 1, 2], [2, 1, 2], [2, 1, 2], [2, 1, 0], [1, 2, 0], [0, 2, 1], [1, 0, 2], [0, 1, 2]]

#La suite n'est pas encore utilise (jusqu'au satisfy)

#Set de notes pour chaque eleve
elevesNotes = [[15, 15], [12, 18], [20, 4], [12, 13], [9, 8], [17, 18], [5, 19], [16, 11]]

#Set de coefs des notes pour chaque option
coefsOptions = [[2, 1], [1, 1], [1, 3]]

#Set de moyennes coeficientés par option pour chaque eleve
elevesMoyenneOptions = [[], [], [], [], [], [], [], []]

#Calcul des moyennes coeficcientees pour chaque eleve
for y in range(len(options)):
    for i in range(len(eleves)):
        moyenne = 0
        for x in range(len(elevesNotes[0])):
            moyenne += elevesNotes[i][x] * coefsOptions[y][x]
        moyenne = round(moyenne / sum(coefsOptions[y]), 2)
        elevesMoyenneOptions[i].append(moyenne)

#Conditions : (Commentaires hors du satisfy sinon erreur chez moi, raison inconnue)

# Il ne peut pas y avoir plus d'eleves par option que de place disponible
#Un eleve doit être attribue dans l'option de son 1er choix sauf si celle ci est pleine. (Donc soit il valide que son opption est son choix 1 soit que cette option est pleine.)

satisfy(
    [Count(eleves, value=options[i]) <= optionsPlaces[i] for i in range(len(options))],
    [((eleves[i]==options[elevesChoix[i][0]]) or (Count(eleves, value=options[elevesChoix[i][0]]) == optionsPlaces[elevesChoix[i][0]])) for i in range(len(eleves))]
)