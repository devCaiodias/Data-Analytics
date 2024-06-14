import numpy as np

arr = np.array([1,2, np.nan, 4])
print(arr)

arr_nan = np.isnan(arr)
print(arr_nan)
print(np.zeros(3) / 0)
print(np.isnan(np.nan))
# print(np.isnan(None))

# np.inf > infinito
arr_inf = np.array([1,2, np.inf, 4, -np.inf]) 
print(arr_inf)
print(np.isinf(arr_inf))
print(np.ones(3) / 0)

# Constantes Numerica
pi = np.pi
print(pi)
e = np.e
print(e)