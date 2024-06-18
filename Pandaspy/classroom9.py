import numpy as np
import pandas as pd

np.random.seed(42)
serie = pd.Series(np.random.choice(["Azul", "Amarelo", "vermelho"], size=1000))
print(serie)

serieA = serie.astype("category")
print(serieA)
print(serie.memory_usage())
print(serieA.memory_usage())

print(serieA[serieA == "vermelho"])
print(serieA.str.upper())
print(serieA.str.contains("v"))

categoria = pd.Categorical(["Azul", "Amarelo", "vermelho", "Verde"])
print(serie.astype(categoria.dtype))