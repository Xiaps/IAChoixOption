import numpy as np;
import pandas as pd;

data = pd.read_csv('Options.csv', delimiter=";")
notesEleves=data.values

print("Data brutes :")
print(data)
print("\n\n Data numpy :")
print(notesEleves);
