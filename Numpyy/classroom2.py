import numpy as np

arry = np.arange(1,10)
matriz = np.random.normal(1,2, (3, 3))
print(arry)
print(matriz)

# Array
print(arry[0])
print(arry[::-2])
print(arry[1:3])
print(arry[[1,2]])

# Matriz
print(matriz[2][-1])
print(matriz[1])
print(matriz[:, 1])
print(matriz[1,2])
print(matriz[:,[1,2]])

