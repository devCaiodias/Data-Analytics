import pandas as pd
import numpy as np

np.random.seed(42)
serie = pd.Series(np.random.randint(10, size=10))
# print(np.sum(serie))
# print(np.diff(serie))
# print(np.unique(serie))
# print(np.linalg.norm(serie))
# print(np.sin(serie))

print(np.mean(serie), serie.mean())
print(serie.quantile(0.1))

# .describe: Gera o resumo estatístico da série
# mode: O valor da moda da série
# .count: Obtém a contagem de elementos não nulos
# .nunique: Conta o total de elementos únicos
# .value_counts: Produz o número de ocorrências de cada elemento na série
# .clip: Força os elementos da série a estarem dentro de um determinado intervalo 
# .pct_change: Variação percentual entre elementos consecutivos da série
# .shift: Desloca a série por um certo número de elementos

print(serie.describe())
print(serie.mode())
print(serie.count())
print(serie.nunique())
print(serie.value_counts())
print(serie.clip(4, 6))
print(serie.pct_change())
print(serie.shift(-1))
print(serie.diff() / serie.shift(1))

print(serie.replace({6:"OPA!"}))
print(serie.sort_values(ascending=False))