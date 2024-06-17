import pandas as pd
import numpy as np

np.random.seed(42)

serie1 = pd.Series(data=np.random.normal(size=10))
# print(serie1)
# print(serie1 > 0)
# print((serie1 > 0) & (serie1 < 1) )
# print(serie1[(serie1 > 0) & (serie1 < 1)])

serie2 = pd.Series(np.arange(10))
serie3 = pd.Series(np.arange(10))
# print(serie2[serie3 > 5])

# print(any((serie1 > 0) & (serie1 < 1)))
# print(all((serie1 > 0) & (serie1 < 1)))

serie4 = pd.Series(list("abdefghijklmnopqrstuvwyz"))
print(serie4.isin(["a", "e", "i", "o", "u"]))

serie = pd.Series([1,2, 3, np.nan, 5, np.nan, 7])
print(serie.isna())
print(serie.isnull())

serie = pd.Series(np.arange(10))
print(serie.where(lambda x: x > 5))

print(serie.where(lambda x: x > 5, "N é maior do que 5"))