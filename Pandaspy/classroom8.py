import pandas as pd
import numpy as no

ser1 = pd.Series([["Ola", "prazer"], ["a", "noite"], ["é", "nossa"]])
print(ser1)

ser2 = pd.Series([{"Quando": "hoje"}, {"Onde": "Meu ape"}, {"Pode": "Aparecer"}])
print(ser2)

ser3 = pd.Series([{"Festa"}, {"Festa", "Tem", "Birita"}, {"Tem", "até", "Amanhecer"}])
print(ser3)

print(["Ola", "prazer"] + ["a", "noite"])
print(ser1 + ser1)
print(ser1.sum())
print(ser1.cumsum())