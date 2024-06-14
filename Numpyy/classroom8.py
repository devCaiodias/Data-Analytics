import numpy as np

np.random.seed(42)
a = np.random.normal(loc=5, size=(5,3))
b = np.random.choice(["A", "B", "C"], size=(5,3))
c = np.array([0, 1, 2, 0 , 4, 5])
d = np.random.normal(size=(5,3))
print(a)
print(b)
print(c)
print(d)
print()

# Agregação:
# np.mean: Calcula a média 
# np.median: Calcula a mediana
# np.min: Calcula o valor minimo 
# np.max: Calcula o valor máximo 
# np.std: Calcula o desvio-padrão 
# np.var: Calcula a variância
# np.percentile: Calcula o percentil específicado
# np.sum: Calcula a soma de todos os elementos
# np.count_nonzero: Realiza a contagem dos elementos não nulos do array
# np.unique: Obtém os valores únicos de um array

# print(np.mean(a))
# print(np.mean(a, axis=1))
# print(np.percentile(a, 0.25))
# print(np.unique(b))
# print(c.shape, np.count_nonzero(c))

# TRANSFORMAÇÔES:

# np.cell: Arredonda os valores de um array para cima.
# np.floor: Arredonda os valores de um array para baixo
# np.round: Arredonda os valores de um array para as casas decimais desejadas
# np.trunc: Remove as casas decimais do valor numérico
# np.abs: Calcula o valor absoluto dos elementos
# np.sign: Obtém os sinais dos números de um array

# print(np.ceil(a))
# print(np.round(a, 2))
# print(np.trunc(a))
# print(np.sign(d))

# Matemática:

# np.exp: Realiza a exponenciação dos elementos
# np.log: Aplica o log sobre os elementos
# np.expm1: Aplica a função exp(x) - 1 sobre os elementos
# np.log1p: Aplica a função log(x + 1) sobre os elementos
# np.power: Eleva os elementals do array a uma potência
# np.sqrt: Extraí a raiz quadrada dos números de um array
# np.sin/cos/tan: Aplica a função seno/cosseno/tangente sobre os elementos
# np.asin/acos/atan: Aplica a função de arc seno/cosseno/tangente sobre os elementos

print(np.log(a))
print(np.sin(d))

# Elemento a Elemento:

# np.diff: Obtém a diferença entre valores sequenciais do array
# np.cumsum: Obtém a soma dos valores cumulativos
# np.cummin: Obtém o valor mínimo cumulativo do array
# np.cummax: Obtém o valor máximo cumulativo do array
# np.cumprod: Obtém o valor produto cumulativo do array

print(np.diff(c))
print(np.cumsum(c))
