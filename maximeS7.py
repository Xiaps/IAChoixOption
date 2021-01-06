import numpy as np;
import pandas as pd;

data = pd.read_csv('Options.csv', delimiter=";")
coefsData = pd.read_csv('Coefs.csv', delimiter=";")
notesEleves=data.values
coefs = coefsData.values
coefs_LD = coefs[0]
coefs_SE = coefs[1]
coefs_OC = coefs[2]

print("Data brutes :")
print(data)

print("\n\n Data numpy :")
print(notesEleves);

print("\n\n Coefs numpy :")
print(coefs);

sommeCoefs = 28


s=0
for i in range(len(notesEleves)):
    for j in range(len(notesEleves[0])):
        s+=notesEleves[i][j]

        print("coucou")


print(len(notesEleves[0]))
print(notesEleves[0].size)



