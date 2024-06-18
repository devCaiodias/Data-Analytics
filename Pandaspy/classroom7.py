import pandas as pd
import numpy as np

# Numerico

np.random.seed(42)
serie = pd.Series(np.random.randint(10, size=10))
print(serie)
print(serie.astype("int8"))
print(serie.astype("uint8"))
print(serie.astype(int))
print(serie.astype(np.uint16))