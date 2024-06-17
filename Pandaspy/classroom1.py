import pandas as pd
import numpy as np

por_dirc = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
serie_dirc = pd.Series(data=por_dirc)
print(serie_dirc)

# print(serie_dirc[1])
# print(serie_dirc[[1,2]])
print(serie_dirc["b"])
print(serie_dirc[["b", "c"]])
print(serie_dirc["b":])
print(serie_dirc["b":"c"])
print(serie_dirc["b":"e": 2])
print(serie_dirc["e":"b": -2])

print(serie_dirc)
serie_dirc["b":"c"] = 3
print(serie_dirc)

print(por_dirc)
sl = serie_dirc["b":"c"]
sl[:] = 20
print(serie_dirc)

def mudar_serie(serie):
    serie.iloc[-1] = np.inf
mudar_serie(serie_dirc)
print(serie_dirc)


serie_complex = pd.Series(
    data=[1,2,3],
    index=[3,2,1]
)
# print(serie_complex)
# print(serie_complex[3])
# print(serie_complex.iloc[0])
# print(serie_complex.iloc[[1,2]])
# print(serie_complex.iloc[1:])

