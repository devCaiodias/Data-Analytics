import pandas as pd

df = pd.read_excel(r"C:\Users\caio\Data Analytics\ETLpy\classroom\produtos_novo.xlsx")
print(df.head())
print()

df_produto40 = df.loc[df['Produto'] == 'Produto 40']
print(df_produto40)
print()

item = ['Produto 40', 'Produto 41', 'Produto 25', 'Produto 8']
df_item = df.loc[df['Produto'].isin(item)]
print(df_item)
print()

dfMais50 = df.loc[df['Preço'] > 50]
print(dfMais50.head())

df20a50 = df.loc[(df['Preço'] > 20) & (df['Preço'] <= 50)]

print(df20a50)
