#0 0 1 1 0 0 1 0 0 0 0 1 1 0 0 1 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0 0 15 14 15 13 9 17 12 14 104

import numpy as np;

options =["LD","SE","BIO"]
eleve = ["Guillaume", "Maxime", "Alban", "Roger", "Manu", "Morgane", "Vegeta", "Clara"]
rawData = input();

data = rawData.split(" ");
nombreEleve = len(eleve);
nombreOptions = len(options)
optionChoisi=data[:nombreEleve*3]
choixObtenu=data[nombreEleve*3:nombreEleve*3+8]
notesOptions=data[nombreEleve*3+8:nombreEleve*3+16]

nbEleveParOption=[]
for i in range(nombreOptions):
    nbEleveParOption.append(0)

resultat=[[],[],[],[]]

for i in range(round(nombreEleve)):
    resultat[0].append(eleve[i]);
    resultat[2].append(choixObtenu[i])
    resultat[3].append(notesOptions[i])
    for j in range(nombreOptions):
        if(data[i*nombreOptions+j]== "1"):
            resultat[1].append(options[j])
            nbEleveParOption[j]+=1


resultat= np.array(resultat)
resultat=np.transpose(resultat)

for i in range(nombreOptions):
    print("Il y a "+str(nbEleveParOption[i])+" étudiant dans l'option "+ options[i])
print(resultat)


