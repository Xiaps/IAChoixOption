#0 0 1 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 0 0 1 0 0 0 1 0 0 0 0 15 15 15 12 8 17 12 14 103

import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt


options =["LD","SE","BIO","CSS","EOC","NRJ"]

data = pd.read_csv('testdata80.csv', delimiter=";")
donnees=data.values

nbEleve = len(donnees)
eleves =[]

#Ajout des eleves
for i in range(nbEleve):
    eleves.append(donnees[i][0])

rawData = input();

data = rawData.split(" ");
nombreOptions = len(options)
optionChoisi=data[:nbEleve*nombreOptions]
choixObtenu=data[nbEleve*nombreOptions:nbEleve*nombreOptions+nbEleve]
notesOptions=data[nbEleve*nombreOptions+nbEleve:nbEleve*nombreOptions+(nbEleve*2)]

nbEleveParOption=[]
for i in range(nombreOptions):
    nbEleveParOption.append(0)

resultat=[["Prenom"],["Option attribuee"],["Rang du choix"],["Moyenne dans l'option"]]

def convertChoix(choix):
    if(choix == "0"):
        return "Premier choix"
    elif(choix == "1"):
        return "Deuxieme choix"
    elif(choix == "2"):
        return "Troisieme choix"
    elif(choix == "3"):
        return "Quatrieme choix"
    else : return "choix trop loin"

for i in range(round(nbEleve)):
    resultat[0].append(eleves[i]);
    resultat[2].append(convertChoix(choixObtenu[i]))
    resultat[3].append(notesOptions[i])
    #"Moyenne dans l'option : " +
    for j in range(nombreOptions):
        if(data[i*nombreOptions+j]== "1"):
            resultat[1].append(options[j])
            nbEleveParOption[j]+=1

resultat= np.array(resultat)
resultat=np.transpose(resultat)

for i in range(nombreOptions):
    print("Il y a "+str(nbEleveParOption[i])+" étudiant dans l'option "+ options[i])
print(resultat)

df = pd.DataFrame(resultat)
df.to_csv('choixEffectueIA.csv',index=False,header=False)

nbPremierChoix=0
nbDeuxiemeChoix=0
nbTroisiemeChoix=0


for i in range(len(choixObtenu)):
    if choixObtenu[i]=="0":
        nbPremierChoix+=1
    elif choixObtenu[i]=="1":
        nbDeuxiemeChoix+=1
    elif choixObtenu[i]=="2":
        nbTroisiemeChoix+=1

x = [nbPremierChoix,nbDeuxiemeChoix,nbTroisiemeChoix]
plt.title("Proportion d'élève ayant eu leur premier choix")
plt.pie(x, labels = ['Premier choix', 'Deuxième choix', 'Troisième choix'], normalize = True)
plt.legend()
plt.show()




