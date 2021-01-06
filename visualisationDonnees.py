import numpy as np;

eleve = ["Guillaume", "Maxime", "Alban", "Roger", "Manu", "Morgane", "Vegeta", "Clara"]
rawData = input();

data = rawData.split(" ");
nombreEleve = len(eleve);
optionChoisi=data[:nombreEleve*3]
choixObtenu=data[nombreEleve*3:nombreEleve*3+8]
notesOptions=data[nombreEleve*3+8:nombreEleve*3+16]

resultat=[[],[],[],[]]

for i in range(round(nombreEleve)):
    resultat[0].append(eleve[i]);
    resultat[2].append(choixObtenu[i])
    resultat[3].append(notesOptions[i])
    if(data[i*3] == "1"):
        resultat[1].append("LD")
    if (data[i * 3+1] == "1"):
        resultat[1].append("SE")
    if (data[i * 3+2] == "1"):
        resultat[1].append("BIO")

resultat= np.array(resultat)
resultat=np.transpose(resultat)

print(resultat)
