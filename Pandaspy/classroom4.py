import pandas as pd
import numpy as np

np.random.seed(42)
serie = pd.Series(np.random.randint(10, size=10))
serie.iloc[np.random.randint(10, size=3)] = np.nan
print(serie)
print(serie.fillna(-1))
# print(serie.fillna(-1, inplace=True))

print(serie.ffill())
