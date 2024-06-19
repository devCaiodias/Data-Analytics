import pandas as pd
import numpy as np

serie = pd.Series(np.arange(10))
# print(serie.rolling(3))
# print(serie.rolling(3).mean())
# print(serie.rolling(3, min_periods=2).mean())
# print(serie.rolling(3, min_periods=2).sum())
# print(serie.rolling(3, min_periods=2).count())

# Interpolate

np.random.seed(42)
serie = pd.Series(np.random.normal(10, size=10))
serie[np.random.randint(10, size=3)] = np.nan
print(serie)
print(serie.interpolate("linear"))
print(serie.interpolate("linear", limit_direction="both"))
