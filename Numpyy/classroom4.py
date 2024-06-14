import numpy as np

np.random.seed(42)
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
m1 = np.random.randint(1, 10, size=(3,3))
m2 = np.random.randint(1, 10, size=(3,3))

print(m1)
print(m2)

# Soma
arr_soma = arr1 + arr2
print(arr_soma)

arr_add = np.add(arr1, arr2)
print(arr_add)

# Subtração
arr_subtracao = arr1 - arr2
print(arr_subtracao)

arr_subtract = np.subtract(arr1, arr2)
print(arr_subtract)

# Mutiplicação Escalar
arr_multiplicaoE = arr1 * 2
print(arr_multiplicaoE)

arr_multiplicaoE = arr1 * 2.1
print(arr_multiplicaoE)

arr_multiplay = np.multiply(arr1, 2)
print(arr_multiplay)

# Multiplicação elemento-winse
arr_multiplicaoElement = arr1 * arr2
print(arr_multiplicaoElement)

arr_multiplay = np.multiply(arr1, arr2)
print(arr_multiplay)

# Multiplicação Produto vetorial
arr_multiplicaoP = sum(arr1 * arr2)
print(arr_multiplicaoP)

arr_multiplicaoP = arr1.dot(arr2)
print(arr_multiplicaoP)

# Multiplicação Cruzada
arr_multiplicaoCruzado = np.cross(arr1, arr2)
print(arr_multiplicaoCruzado)

# Multiplicação Matricial
arr_multiplicaoM = np.matmul(m1, m2)
print(arr_multiplicaoM)

# Divisão
arr_divisao = arr1 / arr2
print(arr_divisao)

arr_divisao = np.divide(arr1, arr2)
print(arr_divisao)

# Exponenciação
arr_exponenciacao = arr1 ** 2
print(arr_exponenciacao)

arr_exponenciacao = arr1 ** arr2
print(arr_exponenciacao)

arr_exponenciacao = np.power(arr1, arr2)
print(arr_exponenciacao)

# Modulo de um vetor
arr_vetor = sum(arr1 * arr1) ** 0.5
print(arr_vetor)

arr_vetor = np.linalg.norm(arr1)
print(arr_vetor)

# Determinante de uma matriz
matriz_deteminante = np.linalg.det(m1)
print(matriz_deteminante)

# Matriz inversa
matriz_inversa = np.linalg.inv(m1)
print(matriz_inversa)

matriz_inversa = m1.T
print(matriz_inversa)