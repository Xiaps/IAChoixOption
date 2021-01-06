#0 0 1 1 0 0 1 0 0 0 0 1 1 0 0 1 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0 0 15 14 15 13 9 17 12 14 104

import numpy as np;

options =["LD","SE","BIO", "CSS"]
eleve = ["Guillaume", "Maxime", "Alban", "Roger", "Manu", "Morgane", "Vegeta", "Clara"]
rawData = input();

data = rawData.split(" ");
nombreEleve = len(eleve);
nombreOptions = len(options)
optionChoisi=data[:nombreEleve*nombreOptions]
choixObtenu=data[nombreEleve*nombreOptions:nombreEleve*nombreOptions+8]
notesOptions=data[nombreEleve*nombreOptions+8:nombreEleve*nombreOptions+16]

nbEleveParOption=[]
for i in range(nombreOptions):
    nbEleveParOption.append(0)

resultat=[[],[],[],[]]

def convertChoix(choix):
    if(choix == "0"):
        return "Premier choix"
    elif(choix == "1"):
        return "Deuxième choix"
    elif(choix == "2"):
        return "Troisième choix"
    elif(choix == "3"):
        return "Quatrième choix"
    else : return "choix trop loin"

for i in range(round(nombreEleve)):
    resultat[0].append(eleve[i]);
    resultat[2].append(convertChoix(choixObtenu[i]))
    resultat[3].append("Moyenne dans l'option : " +notesOptions[i])
    for j in range(nombreOptions):
        if(data[i*nombreOptions+j]== "1"):
            resultat[1].append(options[j])
            nbEleveParOption[j]+=1



resultat= np.array(resultat)
resultat=np.transpose(resultat)

for i in range(nombreOptions):
    print("Il y a "+str(nbEleveParOption[i])+" étudiant dans l'option "+ options[i])
print(resultat)


