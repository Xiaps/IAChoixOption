from pycsp3 import *

# letters[i] is the digit of the ith letter involved in the equation
LD, SE, BIO = options = {4, 4, 2}
Guillaume, Maxime, Alban, Roger, Manu, Vegeta, Morgane, Clara = eleves = VarArray(size=8, dom=options)

elevesNotes = {{15,15},{12,18},{20,4},{12,13},{9,8},{17,18},{5,19},{16,11}}

coefsOptions = {{2,1},{1,1},{1,3}}

elevesMoyenneOptions = {{},{},{},{},{},{},{},{}}

elevesChoix = {{0,1,2},{1,0,2},{0,1,2},{2,1,0},{1,2,0},{0,2,1},{1,0,2},{0,1,2}}

for y in range(len(options)) :
    for i in range(len(eleves)) :
        moyenne = 0
        for x in range(len(elevesNotes[0])) :
            moyenne+=elevesNotes[i][x]*coefsOptions[y][x]
        moyenne=moyenne/sum(coefsOptions[y])
        elevesMoyenneOptions[i].append(moyenne)

satisfy(
    # words cannot start with 0
    (eleves.count(i) <= options[i] for i in range(len(options))),



)
