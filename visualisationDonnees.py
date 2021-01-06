eleve = ["Guillaume", "Maxime", "Alban", "Roger", "Manu", "Morgane", "Vegeta", "Clara"]
rawData = input();

data = rawData.split(" ");
nombreEleve = len(data)/3;
print(nombreEleve);

for i in range(round(nombreEleve)):
    print(eleve[i]+" est dans l'option : ")
    if(data[i*3] == "1"):
        print("LD")
    if (data[i * 3+1] == "1"):
        print("SE")
    if (data[i * 3+2] == "1"):
        print("BIO")