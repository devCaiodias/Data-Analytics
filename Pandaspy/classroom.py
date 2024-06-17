import pandas as pd
import numpy as np

serie = pd.Series(
    data=[1,2,2, np.nan], 
    index=["p","q", "r", "s"],
    name="Data"
)

# print(serie)
# print(serie.index)
# print(serie.name)
# print(serie.values)
# print(serie.dtype)
# print(serie.shape)
# print(serie.size)

por_lista = ["a", "b", "c"]
serie_lista = pd.Series(data=por_lista)
print(serie_lista)

por_array = np.arange(1, 4)
serie_array = pd.Series(data=por_array)
print(serie_array)

por_dirc = {"a": 10, "b": 20, "c": 30}
serie_dirc = pd.Series(data=por_dirc)
print(serie_dirc)

# Execicio
serie1 = pd.Series(
    index=["Belgim", "Israel", "Chile", "Peru", "Argentina", "Espanha"],
    data=[39.152,    35.578,    27.55,   28.213,  26.593,      26.554]
)

print(serie1)