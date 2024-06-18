import pandas as pd
import numpy as np

np.random.seed(42)

serie = pd.Series(np.random.randint(10, size=10))
print(serie)
# def calculo(x):
#     if x > 5:
#         return 1
#     else:
#          return x / 5 
print(serie.apply(lambda x: 1 if x > 5 else x / 5))

np.random.seed(42)
serie = pd.Series(np.random.randint(10, size=10))
print(serie.map(lambda x: 1 if x > 5 else x / 5))
