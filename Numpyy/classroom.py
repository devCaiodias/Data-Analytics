import numpy as np

# Um array NumPy é uma coleção multidimensional de valores do mesmo tipo de dados, armazenados em um bloco contíguo de memória
arrayy = np.array([1,2,3,4,5])
print(arrayy)
matriz = np.array([[1,2,3], [4,5,6]])
print(matriz)

print(
    f"array: dtype={arrayy.dtype} / shape= {arrayy.shape} / size={arrayy.size} / itemsize={arrayy.itemsize} / strides={arrayy.strides}"
)

print(
    f"matriz: dtype={matriz.dtype} / shape= {matriz.shape} / size={matriz.size} / itemsize={matriz.itemsize} / strides={matriz.strides}"
)

# Criando um array prenchido com zero
array_zeros = np.zeros(shape=(3,3))
print(array_zeros)

# Criando um array prenchido com one 
array_ones = np.ones(shape=(3))
print(array_ones)

# Criando matriz identidade com o tamanho especifico
matriz_identidade = np.eye(4)
print(matriz_identidade)

array_arange = np.arange(1,10,2)
print(array_arange)

# Criando um array entre dois numeros espaçados linearmente
array_linspace = np.linspace(5, 10, num=5)
print(array_linspace)

# Criando um array entre dois numeros espaçados logaritimicamente
array_logspace = np.logspace(1,3,3)
print(array_logspace)

# Criando um array aleatorio entre valores menor e maiores
array_random = np.random.randint(0,10, size=(5,5))
print(array_random)

# Criando um array aleatorio com valores baseados em uma distribuição normal
array_random_normal = np.random.normal(1,2,10)
print(array_random_normal)

# Execicio

matriz_ex = np.linspace(5,11,16).reshape(4,4)
print(matriz_ex)

armazenamento = matriz_ex.itemsize * matriz_ex.size
print("Armazenamento: ", armazenamento)