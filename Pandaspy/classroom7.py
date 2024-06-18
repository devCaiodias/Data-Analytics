import pandas as pd
import numpy as np
import re

# Numerico

np.random.seed(42)
serie = pd.Series(np.random.randint(10, size=10))
# print(serie)
# print(serie.astype("int8"))
# print(serie.astype("uint8"))
# print(serie.astype(int))
# print(serie.astype(np.uint16))

# String

ser = pd.Series(["Maçã", "Laranja", "Plano", "Python", "Dinheiro"])

print("Maçã".upper())

# print(ser.map(lambda x: x.upper()))
print(ser.str.upper())

# contains: Testa se a string contém um determinado padrão de expressão regular
# count: Conta o número de ocorrências de uma substring dentro da string
# find: Devolve o índice de ocorrência de uma substring dentro da string (devolve -1 se não for encontrado) 
# isalpha: Checa se todos os caracteres da string são letras
# isdigit: Checa se a string é um número
# len: Obtém o tamanho da string
# strip: Elimina espaços vazios nos extremos da string
# startswith: Checa se a string começa com uma determinada sub-string
# upper: Converte a string para maiúsculo
# lower: Converte a string para minúsculo
# split: Divide a string de acordo com uma sub-string (cada elemento da série passará a ser uma lista)

print(ser.str.contains("a"))
print(ser.str.replace("a", "A"))
print(ser.str.split("a"))
print(ser.str.lower())

print(ser.str[:3])
print(ser.str[::-1])
print(ser.str[0])
print(ser.str.match("^(P)"))
print(ser[ser.str.match("^(P)")])

# print(re.match("^(P)", "Piloto"))

