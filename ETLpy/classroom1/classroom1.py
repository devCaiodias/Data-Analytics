import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\caio\Data Analytics\ETLpy\classroom1\clientes.csv', delimiter=',')
print(df.head())

proporcao_nulos = 0.3

df = df.applymap(lambda x: x if np.random.rand() > proporcao_nulos else None)
print(df.head())

# Filtrando 1 item esoecifico do meu DataFrame
estado = df.loc[df['Estado'] == 'GO']
print(estado)
print()

# Escolhendo um estado especifico
estados = ['AP', 'GO', 'RO']
df_estados = df.loc[df['Estado'].isin(estados)]
print(df_estados)

# Tratando nulos